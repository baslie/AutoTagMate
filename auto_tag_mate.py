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
    Uses scope matching based on allowed selectors.
    """
    settings = load_settings()
    allow_untitled = settings.get("allow_untitled", True)
    allowed_selectors = settings.get("allowed_selectors", ["text.plain"])

    file_name = view.file_name()
    if file_name is None and not allow_untitled:
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
                phrase_region, phrase_text = self.get_phrase_region(region.begin())
                if phrase_text:
                    self._wrap_text_with_tags(edit, phrase_region, phrase_text)
            else:
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

    def get_phrase_region(self, point):
        # Returns a tuple: (region, text)
        line_region = self.view.line(point)
        line_start = line_region.begin()
        if point <= line_start:
            return sublime.Region(point, point), ""
        phrase_region = sublime.Region(line_start, point)
        phrase_text = self.view.substr(phrase_region).strip()
        if not phrase_text:
            return sublime.Region(point, point), ""
        if " " not in phrase_text:
            word_region = self.view.word(point)
            word_text = self.view.substr(word_region)
            return word_region, word_text
        else:
            return phrase_region, phrase_text

class AutoCloseTagListener(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        if not is_valid_view(view):
            return

        if view.settings().get("auto_close_tag_in_progress", False):
            return

        for region in view.sel():
            pos = region.begin()
            if pos == 0:
                continue
            if pos < view.size() and view.substr(sublime.Region(pos, pos + 1)) == "<":
                continue
            last_char = view.substr(sublime.Region(pos - 1, pos))
            if last_char != ">":
                continue

            line_region = view.line(pos)
            line_text = view.substr(sublime.Region(line_region.begin(), pos))
            lt_index = line_text.rfind("<")
            if lt_index == -1:
                continue

            tag_candidate = line_text[lt_index:]
            pattern = r"<([a-zA-Z0-9_\-\s]+)>$"
            match = re.match(pattern, tag_candidate)
            if match:
                tag_name = match.group(1).strip()
                if not tag_name:
                    continue

                view.settings().set("auto_close_tag_in_progress", True)
                sublime.set_timeout(lambda: self.insert_closing_tag(view, pos, tag_name), 0)
                break

    def insert_closing_tag(self, view, pos, tag_name):
        try:
            view.run_command("insert_text", {"position": pos, "text": "</{0}>".format(tag_name)})
            view.sel().clear()
            view.sel().add(sublime.Region(pos, pos))
        except Exception as e:
            print("AutoTagMate Error in insert_closing_tag:", e)
        finally:
            view.settings().set("auto_close_tag_in_progress", False)

class InsertTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, position, text):
        try:
            self.view.insert(edit, position, text)
        except Exception as e:
            print("AutoTagMate Error in InsertTextCommand:", e)

class OpenAutoTagMateSettingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("edit_settings", {
            "base_file": "${packages}/AutoTagMate/auto_tag_mate.sublime-settings",
            "default": sublime.load_resource("Packages/AutoTagMate/auto_tag_mate.sublime-settings")
        })
