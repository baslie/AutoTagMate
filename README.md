# AutoTagMate

AutoTagMate is a lightweight Sublime Text plugin that automatically generates XML-style closing tags with smart cursor positioning. It's perfect for quickly wrapping text in tags and auto-completing tag pairs.

---

## Features

- Convert words or phrases into tags using a hotkey (default: `Tab`)
- Auto-insert closing tags when typing `>`
- Support for both single-word and multi-word phrases
- Smart cursor positioning inside the generated tag pair
- Configurable file type support via `allowed_selectors`
- Ability to customize the hotkey through Sublime Text key bindings

---

## Installation

### Via Package Control

1. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Choose **Package Control: Install Package**
3. Search for **AutoTagMate** and install it

### Manual Installation

1. Download the repository
2. Place the files in your Sublime Text `Packages/User` directory
3. Restart Sublime Text

---

## Usage

### Creating a Tag

1. Type a word (e.g., `Header`)
2. Press the hotkey (default: `Tab`)
3. Result: `<Header></Header>` with the cursor positioned between the tags

### Creating a Tag from a Multi-word Phrase

1. Type a phrase (e.g., `Main Content`)
2. Press the hotkey
3. Result: `<Main Content></Main Content>`

### Auto-closing Tags

1. Type an opening tag (e.g., `<Header>`)
2. The plugin automatically adds the corresponding closing tag: `<Header></Header>`

---

## Configuration

The plugin settings are stored in the **auto_tag_mate.sublime-settings** file:

```json
{
    "allowed_selectors": ["text.plain"],
    "allow_untitled": true
}
```

- **allowed_selectors**: A list of CSS selectors that define in which file types the plugin is active (default: `["text.plain"]`).
- **allow_untitled**: If set to `true`, the plugin will work in unsaved (untitled) files.

---

## Hotkeys

### Default Assignment

By default, the plugin uses the `Tab` key to trigger the `insert_auto_tag` command.

### Changing the Hotkey

If you wish to change the default hotkey (for example, to `Ctrl+~`), follow these steps:

1. Open **Preferences → Key Bindings**.
2. In the user key bindings file (the right-hand side file), add the following block:

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

3. Save the file — the new key binding will take effect immediately.

> **Note:** If the `Tab` key is already bound to this command, you may need to remove or override that binding in your user key bindings.

---

## Additional Commands

- **Open Plugin Settings:**  
  You can open the plugin settings via the `open_auto_tag_mate_settings` command available in the Command Palette.

---

## Support and Contact

For questions, feature requests, or technical support, please visit [roman-purtow.ru](https://roman-purtow.ru).

---

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.