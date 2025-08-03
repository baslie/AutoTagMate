import sublime
import sublime_plugin

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

class OpenAutoTagMateSettingsCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("edit_settings", {
            "base_file": "${packages}/AutoTagMate/auto_tag_mate.sublime-settings",
            "default": sublime.load_resource("Packages/AutoTagMate/auto_tag_mate.sublime-settings")
        })
