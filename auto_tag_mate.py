import sublime
import sublime_plugin
import re

def is_valid_view(view):
    """
    Функция проверяет, разрешён ли плагин для данного файла.
    Настройки загружаются из файла auto_tag_mate.sublime-settings.
    Параметры:
      - allowed_extensions: список разрешённых расширений (например, [".txt"])
      - allow_untitled: разрешено ли работать в неименованных (untitled) файлах.
    """
    settings = sublime.load_settings("auto_tag_mate.sublime-settings")
    allowed_extensions = settings.get("allowed_extensions", [".txt"])
    allow_untitled = settings.get("allow_untitled", True)
    file_name = view.file_name()
    if file_name is None:
        return allow_untitled
    else:
        for ext in allowed_extensions:
            if file_name.lower().endswith(ext.lower()):
                return True
        return False


class InsertAutoTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """
        Команда, обрабатывающая нажатие клавиши Tab.
        Если курсор находится в слове (без символа '<'), то слово заменяется
        на пару тегов вида: <Слово></Слово>
        Курсор перемещается между открывающим и закрывающим тегами.
        """
        if not is_valid_view(self.view):
            return

        for region in self.view.sel():
            if region.empty():
                word_region = self.view.word(region)
                word_text = self.view.substr(word_region)
                # Если слово уже содержит символ '<', ничего не делаем
                if not word_text.startswith("<"):
                    tag_text = "<{0}></{0}>".format(word_text)
                    self.view.replace(edit, word_region, tag_text)
                    new_cursor_pos = word_region.begin() + len("<" + word_text + ">")
                    self.view.sel().clear()
                    self.view.sel().add(sublime.Region(new_cursor_pos, new_cursor_pos))


class AutoCloseTagListener(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        """
        Обработчик, который автоматически вставляет закрывающий тег,
        если пользователь завершил ввод открывающего тега символом '>'.
        """
        if not is_valid_view(view):
            return

        # Если в данный момент уже происходит автодополнение, выходим (чтобы избежать рекурсии)
        if view.settings().get("auto_close_tag_in_progress", False):
            return

        for region in view.sel():
            pos = region.begin()
            if pos == 0:
                continue

            # Если после курсора уже стоит символ '<', значит тег уже вставлен – выходим
            if pos < view.size() and view.substr(sublime.Region(pos, pos + 1)) == "<":
                continue

            last_char = view.substr(sublime.Region(pos - 1, pos))
            if last_char == ">":
                line_region = view.line(pos)
                line_text = view.substr(sublime.Region(line_region.begin(), pos))
                lt_index = line_text.rfind("<")
                if lt_index == -1:
                    continue
                tag_candidate = line_text[lt_index:]
                m = re.match(r"<([^\s/>]+)>$", tag_candidate)
                if m:
                    tag_name = m.group(1)
                    view.settings().set("auto_close_tag_in_progress", True)
                    sublime.set_timeout(lambda: self.insert_closing_tag(view, pos, tag_name), 0)
                    break

    def insert_closing_tag(self, view, pos, tag_name):
        """
        Вставляет закрывающий тег в позицию pos и перемещает курсор между тегами.
        """
        view.run_command("insert_text", {"position": pos, "text": "</" + tag_name + ">"})
        view.sel().clear()
        view.sel().add(sublime.Region(pos, pos))
        view.settings().set("auto_close_tag_in_progress", False)


class InsertTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, position, text):
        """
        Вспомогательная команда для вставки заданного текста по указанной позиции.
        Используется для вставки закрывающего тега.
        """
        self.view.insert(edit, position, text)
