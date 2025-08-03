import sublime
import sublime_plugin
import re

def load_settings():
    """
    Loads plugin settings from auto_tag_mate.sublime-settings.
    """
    return sublime.load_settings("auto_tag_mate.sublime-settings")

def is_valid_view(view):
    """
    Determines if the plugin should be active for the given view.
    Uses scope matching based on allowed selectors or allow_all_files setting.
    """
    settings = load_settings()
    allow_untitled = settings.get("allow_untitled", True)
    allow_all_files = settings.get("allow_all_files", True)
    allowed_selectors = settings.get("allowed_selectors", [])

    file_name = view.file_name()
    if file_name is None and not allow_untitled:
        return False

    # If allow_all_files is True, plugin works in all file types
    if allow_all_files:
        return True

    # Otherwise, check against allowed selectors
    if not allowed_selectors:
        return False

    for selector in allowed_selectors:
        if view.match_selector(0, selector):
            return True
    return False

class InsertAutoTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not is_valid_view(self.view):
            return

        for region in reversed(list(self.view.sel())):
            if region.empty():
                # Если нет выделения, оборачиваем только последнее слово
                word_region, word_text = self.get_last_word_region(region.begin())
                if word_text:
                    self._wrap_text_with_tags(edit, word_region, word_text)
            else:
                # Если есть выделение, оборачиваем выделенный текст
                selected_text = self.view.substr(region)
                if selected_text.strip():
                    self._wrap_text_with_tags(edit, region, selected_text)

    def _wrap_text_with_tags(self, edit, region, text):
        text = text.strip()
        tag_text = "<{0}></{0}>".format(text)
        self.view.replace(edit, region, tag_text)
        new_cursor_pos = region.begin() + len("<{0}>".format(text))
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(new_cursor_pos, new_cursor_pos))

    def get_last_word_region(self, point):
        """
        Возвращает регион и текст последнего слова в строке до курсора.
        """
        line_region = self.view.line(point)
        line_start = line_region.begin()
        
        if point <= line_start:
            return sublime.Region(point, point), ""
        
        # Получаем текст от начала строки до позиции курсора
        text_to_cursor = self.view.substr(sublime.Region(line_start, point))
        
        # Находим все слова в этом тексте
        words = re.findall(r'\S+', text_to_cursor)
        
        if not words:
            return sublime.Region(point, point), ""
        
        # Берем последнее слово
        last_word = words[-1]
        
        # Находим позицию последнего слова в строке
        # Ищем последнее вхождение этого слова в тексте
        last_word_pattern = re.escape(last_word) + r'(?=\s*$)'
        match = None
        for match in re.finditer(last_word_pattern, text_to_cursor):
            pass  # Берем последнее совпадение
        
        if match:
            word_start = line_start + match.start()
            word_end = line_start + match.end()
            word_region = sublime.Region(word_start, word_end)
            return word_region, last_word
        
        # Если по какой-то причине не нашли, возвращаем пустой регион
        return sublime.Region(point, point), ""

class OpenAutoTagMateSettingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("edit_settings", {
            "base_file": "${packages}/AutoTagMate/auto_tag_mate.sublime-settings",
            "default": sublime.load_resource("Packages/AutoTagMate/auto_tag_mate.sublime-settings")
        })
