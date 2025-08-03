# AutoTagMate: Your Universal AI Prompt Structuring Tool

Want to level up your prompts for ChatGPT, Claude AI, or any other neural network-based system? **AutoTagMate** is a lightweight Sublime Text plugin that helps you quickly wrap text in XML-style tags—enhancing clarity and focus for your AI queries. Now works in **ALL file types** out of the box, making it perfect for any workflow.

---

## Why It's Perfect for AI Work

- **Boost Prompt Clarity**  
  Clearly separate instruction sections, examples, or code snippets in your AI prompts by automatically wrapping text in tags—making it easier for the model to understand your intent.

- **Universal File Support**  
  Works in ALL file types by default—Python, HTML, Markdown, plain text, code files, and even unsaved documents without extensions.

- **Manual Control**  
  Use the hotkey (`Ctrl+\` / `Cmd+\`) to instantly wrap your text in a tag pair exactly when you need it—no automatic tag insertion interruptions.

- **No Configuration Required**  
  Works immediately after installation across all your files and projects.

---

## Also Great for HTML & Code Wrapping

While AutoTagMate is ideal for structuring AI prompts, it's still a powerful companion for developers and content creators who need to wrap text in HTML tags, XML markup, or custom tags. Whether you're editing a website, writing documentation, or adding markup to any file type, AutoTagMate has you covered.

---

## Key Features

- **Instant Tag Wrapping**  
  Automatically wraps a selected word or phrase in `<tag></tag>` with a single hotkey press.

- **Manual Operation Only**  
  Tags are created only when you press the hotkey—no automatic interruptions while typing.

- **Smart Cursor Positioning**  
  After wrapping text, the cursor is placed between the opening and closing tags for seamless editing.

- **Universal File Type Support**  
  Works in Python, HTML, Markdown, JavaScript, CSS, plain text, and any other file type—including unsaved files.

- **Conflict-Free Hotkey**  
  Default `Ctrl+\` (Windows/Linux) or `Cmd+\` (macOS) doesn't interfere with Sublime Text's built-in functionality.

- **Customizable Settings**  
  Full control over file type support and behavior through easy-to-use settings.

---

## Installation

### Via Package Control

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Choose **Package Control: Install Package**.
3. Search for **AutoTagMate** and install it.

### Manual Installation

1. [Download the repository](https://github.com/baslie/AutoTagMate) or clone it.
2. Place the files in your Sublime Text `Packages/AutoTagMate` directory.
3. Restart Sublime Text.

---

## Usage

### Creating a Tag

1. Type a word or phrase (e.g., `Header` or `Main Content`).
2. Press the hotkey (`Ctrl+\` / `Cmd+\` by default).
3. AutoTagMate wraps it: `<Header></Header>` or `<Main Content></Main Content>`.

### Manual Tag Creation Only

- AutoTagMate operates exclusively via hotkey activation—no automatic tag completion while typing.
- This ensures full control over when tags are created and prevents interruptions during normal text editing.

### Works Everywhere

- **Python files**: Perfect for docstring structuring and comments
- **HTML/CSS**: Quick tag creation and markup
- **Markdown**: Enhanced structure for documentation
- **Plain text**: AI prompt organization
- **Any file type**: Universal text wrapping solution

---

## Configuration

AutoTagMate settings are stored in the **auto_tag_mate.sublime-settings** file:

```
{
    "allow_all_files": true,
    "allowed_selectors": [],
    "allow_untitled": true
}
```


- **allow_all_files**: If `true` (default), AutoTagMate works in all file types. Set to `false` to use selector-based filtering.
- **allowed_selectors**: A list of CSS selectors that define specific file types where the plugin is active (only used when `allow_all_files` is `false`).
- **allow_untitled**: If `true`, AutoTagMate works in unsaved (untitled) files as well.

### Example Custom Configuration

To limit the plugin to only HTML and plain text files:

```
{
    "allow_all_files": false,
    "allowed_selectors": ["text.html", "text.plain"],
    "allow_untitled": true
}
```


---

## Hotkeys

### Default Assignment

- **Windows/Linux**: `Ctrl+\`
- **macOS**: `Cmd+\`

### Changing the Hotkey

1. Open **Preferences → Key Bindings**.
2. In the user key bindings file (the right-hand side), add:

    ```
    [
        {
            "keys": ["ctrl+shift+t"],
            "command": "insert_auto_tag"
        }
    ]
    ```
3. Save the file. Your new key binding will take effect immediately.

---

## Additional Commands

- **Open Plugin Settings**: Use `AutoTagMate: Open Settings` command in the Command Palette to easily access and modify plugin settings.

---

## What's New in 1.0.7

- **Hotkey-Only Operation**: Tag creation now occurs exclusively via hotkey activation—no automatic tag completion interruptions
- **Cleaner Workflow**: Focus on manual control for precise tag placement when you need it
- **Simplified Codebase**: Streamlined plugin architecture for better performance and reliability

---

## Perfect for Modern Workflows

AutoTagMate is designed for the modern developer and content creator who works across multiple file types and needs quick, reliable text structuring with complete control. Whether you're:

- Crafting detailed AI prompts with clear section markers
- Quickly adding HTML tags to web content
- Structuring documentation with custom markup
- Adding XML-style tags to configuration files
- Organizing code comments with structured tags

AutoTagMate provides the speed and precision you need across all your projects with full manual control.

---

## Support and Contact

For questions, feature requests, or technical support, please visit [roman-purtow.ru](https://roman-purtow.ru).

---

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
