import sublime
import sublime_plugin
import re

def is_valid_view(view):
    """
    Checks if the plugin is allowed to run on the given view.
    Settings are loaded from the "auto_tag_mate.sublime-settings" file.

    Settings:
      - allowed_extensions: a list of allowed file extensions (e.g., [".txt"])
      - allow_untitled: whether to allow the plugin to work in untitled files.
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
        Command that handles the Tab key press.
        When the cursor is in an empty selection, it examines the text
        from the beginning of the line to the cursor:
          - If the text is a single word (without spaces), it wraps that word.
          - If the text is a phrase containing spaces (e.g., "Transcription with timecodes"),
            it wraps the entire phrase.
        If text is selected, the selected text is wrapped.
        After replacement, the cursor is placed between the opening and closing tags.
        """
        if not is_valid_view(self.view):
            return

        for region in self.view.sel():
            if region.empty():
                phrase_region, phrase_text = self.get_phrase_region(region.begin())
                if phrase_text == "":
                    continue
                tag_text = "<{0}></{0}>".format(phrase_text)
                self.view.replace(edit, phrase_region, tag_text)
                new_cursor_pos = phrase_region.begin() + len("<" + phrase_text + ">")
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(new_cursor_pos, new_cursor_pos))
            else:
                # If there is a selection, wrap the selected text with tags.
                selected_text = self.view.substr(region)
                tag_text = "<{0}></{0}>".format(selected_text)
                self.view.replace(edit, region, tag_text)
                new_cursor_pos = region.begin() + len("<" + selected_text + ">")
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(new_cursor_pos, new_cursor_pos))

    def get_phrase_region(self, point):
        """
        Determines the region to be wrapped with tags when the cursor is in an empty selection.
        It takes the text from the start of the line to the cursor position.
        If that text contains spaces, it is considered a phrase.
        Returns a tuple (region, text):
          - region: the region from the beginning of the line to the cursor.
          - text: the trimmed text to be used as the tag.
        If no spaces are found, the default word (using view.word()) is returned.
        """
        line_region = self.view.line(point)
        phrase_region = sublime.Region(line_region.begin(), point)
        phrase_text = self.view.substr(phrase_region).strip()
        if " " not in phrase_text:
            word_region = self.view.word(point)
            phrase_text = self.view.substr(word_region)
            return word_region, phrase_text
        else:
            return phrase_region, phrase_text

class AutoCloseTagListener(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        """
        Event listener that automatically inserts a closing tag when the user
        finishes typing an opening tag with the '>' character.
        """
        if not is_valid_view(view):
            return

        if view.settings().get("auto_close_tag_in_progress", False):
            return

        for region in view.sel():
            pos = region.begin()
            if pos == 0:
                continue

            # If there is a '<' immediately after the cursor, assume a tag is already inserted.
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
                # Update regex to allow spaces in the tag name.
                m = re.match(r"<(.+)>$", tag_candidate)
                if m:
                    # Trim any extra spaces from the captured tag name.
                    tag_name = m.group(1).strip()
                    if tag_name == "":
                        continue
                    view.settings().set("auto_close_tag_in_progress", True)
                    sublime.set_timeout(lambda: self.insert_closing_tag(view, pos, tag_name), 0)
                    break

    def insert_closing_tag(self, view, pos, tag_name):
        """
        Inserts the corresponding closing tag at the specified position and
        places the cursor between the opening and closing tags.
        """
        view.run_command("insert_text", {"position": pos, "text": "</" + tag_name + ">"})
        view.sel().clear()
        view.sel().add(sublime.Region(pos, pos))
        view.settings().set("auto_close_tag_in_progress", False)

class InsertTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, position, text):
        """
        Helper command to insert the specified text at a given position.
        Used for inserting the closing tag.
        """
        self.view.insert(edit, position, text)
