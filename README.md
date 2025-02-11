# AutoTagMate

AutoTagMate is a Sublime Text plugin designed to automatically generate closing tags in specific files. It enhances your workflow by reducing the need for manual tag closure—whether you're typing a plain text word, a multi-word phrase, or finishing an opening tag with the `>` character.

## Features

- **Automatic Tag Completion:**  
  - Type a plain text word (e.g., `Text`) or a phrase with spaces (e.g., `Some extra text`) and press the activation key (default is **Tab**) to automatically wrap the text in matching opening and closing tags. For example, the phrase will be converted into `<Some extra text></Some extra text>`, with the cursor positioned between the tags.
  - When you type an opening tag (e.g., `<Text`) and finish it with `>`, the corresponding closing tag is auto-inserted.

- **Customizable Scope:**  
  - The plugin operates in untitled files and files with extensions specified in the settings. By default, it works in `.txt` files and untitled documents.

- **Easy Configuration:**  
  - Adjust the list of allowed file extensions and toggle the functionality for untitled files via the `auto_tag_mate.sublime-settings` file.

- **Flexible Key Bindings:**  
  - The default key binding for AutoTagMate is **Tab**, but you can easily change it by customizing your key bindings. See the [Key Bindings](#key-bindings) section for instructions.

## Installation

### Manual Installation

1. **Download the Plugin:**  
   Clone or download the repository containing the plugin files.

2. **Copy Files to the Packages Folder:**  
   - Open Sublime Text.
   - Go to **Preferences → Browse Packages…** to open the packages folder.
   - Place the following files in the **User** folder:
     - `auto_tag_mate.py` – the main plugin code.
     - `auto_tag_mate.sublime-settings` – the settings file.
     - *(Optional)* `auto_tag_mate.sublime-keymap` – a sample key binding file for easy customization.

3. **Reload Sublime Text:**  
   Restart Sublime Text to activate the plugin.

### Installation via Package Control

Once the plugin is published through Package Control, simply open the Command Palette (using `Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS), select **Install Package**, and then search for **AutoTagMate**.

## Configuration

The plugin’s behavior is controlled via the `auto_tag_mate.sublime-settings` file. A sample configuration is provided below:

```json
{
    "allowed_extensions": [".txt"],
    "allow_untitled": true
}
```

- **allowed_extensions:**  
  Define the file extensions (e.g., `.txt`) where AutoTagMate is active.

- **allow_untitled:**  
  Set to `true` to allow the plugin to work in new (untitled) files.

Feel free to modify these settings to match your workflow.

## Usage

- **Using the Activation Key:**  
  When editing an eligible file, type a plain text word (e.g., `ExampleTag`) or a multi-word phrase (e.g., `Some extra text`) and press the activation key (default is **Tab**). AutoTagMate will wrap the text with matching opening and closing tags, placing the cursor between them.
  
- **Automatic Tag Closure on '>':**  
  If you type an opening tag (e.g., `<ExampleTag`) and finish it with `>`, the plugin automatically inserts the corresponding closing tag and positions the cursor appropriately.

## Key Bindings

By default, AutoTagMate is bound to the **Tab** key. If you wish to change this, you can customize the key binding in your User key bindings file:

1. Open Sublime Text and navigate to **Preferences → Key Bindings**.
2. In your User key bindings file, add or modify an entry like the following:

```json
[
    {
        "keys": ["ctrl+alt+t"],
        "command": "insert_auto_tag",
        "context": [
            { "key": "selector", "operator": "equal", "operand": "text.plain" }
        ]
    }
]
```

Replace `["ctrl+alt+t"]` with your desired key combination.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
