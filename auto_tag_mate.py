import sublime
import sublime_plugin
import re
from typing import Tuple, Optional

def load_settings() -> sublime.Settings:
    """
    Loads and returns plugin settings.
    Creates default settings file if it doesn't exist.
    """
    settings = sublime.load_settings("auto_tag_mate.sublime-settings")
    
    # Set default values if settings are empty
    if len(settings.to_dict()) == 0:
        settings.set("allowed_extensions", [".txt"])
        settings.set("allow_untitled", True)
        sublime.save_settings("auto_tag_mate.sublime-settings")
    
    return settings

def is_valid_view(view: sublime.View) -> bool:
    """
    Checks if the plugin is allowed to run on the given view.
    
    Args:
        view: The current view to check
    
    Returns:
        bool: Whether the plugin should be active for this view
    """
    try:
        settings = load_settings()
        allowed_extensions = settings.get("allowed_extensions", [".txt"])
        allow_untitled = settings.get("allow_untitled", True)
        
        file_name = view.file_name()
        
        # Check for untitled files
        if file_name is None:
            return allow_untitled
            
        # Check file extension
        return any(file_name.lower().endswith(ext.lower()) for ext in allowed_extensions)
        
    except Exception as e:
        print(f"AutoTagMate Error in is_valid_view: {str(e)}")
        return False

class InsertAutoTagCommand(sublime_plugin.TextCommand):
    def run(self, edit: sublime.Edit) -> None:
        """
        Handles the tag insertion command.
        Wraps selected text or current word/phrase with XML-style tags.
        """
        try:
            if not is_valid_view(self.view):
                return

            selections = list(self.view.sel())
            
            # Handle multiple selections in reverse order to preserve positions
            for region in reversed(selections):
                if region.empty():
                    # No selection - get phrase or word
                    phrase_region, phrase_text = self.get_phrase_region(region.begin())
                    if not phrase_text:
                        continue
                        
                    self._wrap_text_with_tags(edit, phrase_region, phrase_text)
                else:
                    # Handle selected text
                    selected_text = self.view.substr(region)
                    if not selected_text.strip():
                        continue
                        
                    self._wrap_text_with_tags(edit, region, selected_text)
                    
        except Exception as e:
            print(f"AutoTagMate Error in InsertAutoTagCommand: {str(e)}")

    def _wrap_text_with_tags(self, edit: sublime.Edit, region: sublime.Region, text: str) -> None:
        """
        Wraps the given text with tags and positions the cursor.
        
        Args:
            edit: The edit object
            region: The region to replace
            text: The text to wrap in tags
        """
        text = text.strip()
        tag_text = f"<{text}></{text}>"
        
        self.view.replace(edit, region, tag_text)
        
        # Position cursor between tags
        new_cursor_pos = region.begin() + len(f"<{text}>")
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(new_cursor_pos, new_cursor_pos))

    def get_phrase_region(self, point: int) -> Tuple[sublime.Region, str]:
        """
        Determines the region and text to be wrapped with tags.
        
        Args:
            point: The cursor position
            
        Returns:
            Tuple containing the region and the text to be wrapped
        """
        try:
            line_region = self.view.line(point)
            line_start = line_region.begin()
            
            # Check if cursor is at valid position
            if point <= line_start:
                return sublime.Region(point, point), ""
                
            # Get text from line start to cursor
            phrase_region = sublime.Region(line_start, point)
            phrase_text = self.view.substr(phrase_region).strip()
            
            if not phrase_text:
                return sublime.Region(point, point), ""
                
            if " " not in phrase_text:
                # Single word - use word boundaries
                word_region = self.view.word(point)
                word_text = self.view.substr(word_region)
                return word_region, word_text
            else:
                # Multi-word phrase
                return phrase_region, phrase_text
                
        except Exception as e:
            print(f"AutoTagMate Error in get_phrase_region: {str(e)}")
            return sublime.Region(point, point), ""

class AutoCloseTagListener(sublime_plugin.EventListener):
    def on_modified_async(self, view: sublime.View) -> None:
        """
        Automatically inserts closing tags when '>' is typed.
        """
        try:
            if not is_valid_view(view):
                return

            if view.settings().get("auto_close_tag_in_progress", False):
                return

            for region in view.sel():
                pos = region.begin()
                if pos == 0:
                    continue

                # Check for existing closing tag
                if pos < view.size() and view.substr(sublime.Region(pos, pos + 1)) == "<":
                    continue

                last_char = view.substr(sublime.Region(pos - 1, pos))
                if last_char != ">":
                    continue

                # Find opening tag
                line_region = view.line(pos)
                line_text = view.substr(sublime.Region(line_region.begin(), pos))
                lt_index = line_text.rfind("<")
                
                if lt_index == -1:
                    continue

                tag_candidate = line_text[lt_index:]
                
                # Improved regex pattern for tag matching
                pattern = r"<([a-zA-Z0-9_\-\s]+)>$"
                match = re.match(pattern, tag_candidate)
                
                if match:
                    tag_name = match.group(1).strip()
                    if not tag_name:
                        continue
                        
                    view.settings().set("auto_close_tag_in_progress", True)
                    sublime.set_timeout(
                        lambda: self.insert_closing_tag(view, pos, tag_name),
                        0
                    )
                    break
                    
        except Exception as e:
            print(f"AutoTagMate Error in on_modified_async: {str(e)}")
            view.settings().set("auto_close_tag_in_progress", False)

    def insert_closing_tag(self, view: sublime.View, pos: int, tag_name: str) -> None:
        """
        Inserts the closing tag and positions the cursor.
        
        Args:
            view: The current view
            pos: Position to insert the closing tag
            tag_name: Name of the tag to close
        """
        try:
            view.run_command(
                "insert_text",
                {"position": pos, "text": f"</{tag_name}>"}
            )
            view.sel().clear()
            view.sel().add(sublime.Region(pos, pos))
            
        except Exception as e:
            print(f"AutoTagMate Error in insert_closing_tag: {str(e)}")
        finally:
            view.settings().set("auto_close_tag_in_progress", False)

class InsertTextCommand(sublime_plugin.TextCommand):
    def run(self, edit: sublime.Edit, position: int, text: str) -> None:
        """
        Inserts text at the specified position.
        
        Args:
            edit: The edit object
            position: Position to insert the text
            text: Text to insert
        """
        try:
            self.view.insert(edit, position, text)
        except Exception as e:
            print(f"AutoTagMate Error in InsertTextCommand: {str(e)}")