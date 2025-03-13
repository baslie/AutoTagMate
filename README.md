# AutoTagMate: Your Essential AI Prompt Structuring Tool

Want to level up your prompts for ChatGPT, Claude AI, or any other neural network-based system? **AutoTagMate** is a lightweight Sublime Text plugin that helps you quickly wrap text in XML-style tags—enhancing clarity and focus for your AI queries. It’s also perfect for developers, content creators, or anyone who frequently needs to wrap text in tags.

---

## Why It’s Perfect for AI Work

- **Boost Prompt Clarity**  
  Clearly separate instruction sections, examples, or code snippets in your AI prompts by automatically wrapping text in tags—making it easier for the model to understand your intent.

- **Zero Hassle**  
  Set a hotkey (default: `Tab`) to instantly wrap your text in a tag pair, or rely on auto-insertion of the closing tag after typing `>`.

- **Excluded Files/Selectors**  
  Configure file type support via `allowed_selectors` so that the plugin only works where you want it to.

---

## Also Great for HTML Wrapping

While AutoTagMate is ideal for structuring AI prompts, it’s still a powerful companion for developers and content creators who need to wrap text in HTML tags. Whether you’re editing a website or adding simple markup, AutoTagMate has you covered.

---

## Key Features

- **Instant Tag Wrapping**  
  Automatically wraps a selected word or phrase in `<tag></tag>` with a single hotkey press.

- **Auto-insert Closing Tags**  
  Type an opening tag (e.g., `<Header>`), and the plugin automatically adds the corresponding closing tag.

- **Smart Cursor Positioning**  
  After wrapping text, the cursor is placed between the opening and closing tags for seamless editing.

- **Customizable Hotkey**  
  Default is `Tab`, but you can easily change it to another key (e.g., `Ctrl+~`).

- **Configurable File Types**  
  Control in which file types the plugin is active via the `allowed_selectors` setting.

- **Works on Unsaved Files**  
  Enable or disable tag insertion in unsaved (untitled) files through the `allow_untitled` setting.

---

## Installation

### Via Package Control

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Choose **Package Control: Install Package**.
3. Search for **AutoTagMate** and install it.

### Manual Installation

1. [Download the repository](https://packagecontrol.io/packages/AutoTagMate) or clone it.
2. Place the files in your Sublime Text `Packages/User` directory.
3. Restart Sublime Text.

---

## Usage

### Creating a Tag

1. Type a word or phrase (e.g., `Header` or `Main Content`).
2. Press the hotkey (`Tab` by default).
3. AutoTagMate wraps it: `<Header></Header>` or `<Main Content></Main Content>`.

### Auto-closing Tags

- Start typing an opening tag, like `<Header>`.
- AutoTagMate automatically inserts `</Header>`.

---

## Configuration

AutoTagMate settings are stored in the **auto_tag_mate.sublime-settings** file:

```json
{
    "allowed_selectors": ["text.plain"],
    "allow_untitled": true
}
```

- **allowed_selectors**: A list of CSS selectors that define the file types where the plugin is active.  
- **allow_untitled**: If `true`, AutoTagMate works in unsaved (untitled) files as well.

---

## Hotkeys

### Default Assignment

By default, `Tab` is used to trigger the `insert_auto_tag` command.

### Changing the Hotkey

1. Open **Preferences → Key Bindings**.
2. In the user key bindings file (the right-hand side), add:

    ```json
    [
        {
            "keys": ["ctrl+~"],
            "command": "insert_auto_tag",
            "context": [
                { "key": "selector", "operator": "equal", "operand": "text.plain" }
            ]
        }
    ]
    ```
3. Save the file. Your new key binding will take effect immediately.

*(If the `Tab` key is already bound to this command, you can remove or override it in your user key bindings.)*

---

## Additional Commands

- **Open Plugin Settings**: Launch via the `open_auto_tag_mate_settings` command in the Command Palette.

---

## Support and Contact

For questions, feature requests, or technical support, please visit [roman-purtow.ru](https://roman-purtow.ru).

---

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
