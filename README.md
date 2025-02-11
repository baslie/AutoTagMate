# AutoTagMate
AutoTagMate is a Sublime Text plugin designed to automatically generate closing tags in specific files. It enhances your workflow by reducing the need for manual tag closure—whether you're typing a plain text word and pressing Tab or finishing an opening tag with the `>` character.

## Features

- **Automatic Tag Completion:**  
  - Type a plain text word (e.g., `Transcription`) and press **Tab** to automatically convert it to `<Transcription></Transcription>`, with the cursor positioned between the tags.
  - When you type an opening tag (e.g., `<Transcription`) and finish it with `>`, the corresponding closing tag is auto-inserted.

- **Customizable Scope:**  
  - The plugin operates in untitled files and files with extensions specified in the settings. By default, it works in `.txt` files and untitled documents.

- **Easy Configuration:**  
  - Adjust the list of allowed file extensions and toggle the functionality for untitled files via the `auto_tag.sublime-settings` file.

## Installation

### Manual Installation

1. **Download the Plugin:**  
   Clone or download the repository containing the plugin files.

2. **Copy Files to the Packages Folder:**  
   - Open Sublime Text.
   - Go to **Preferences → Browse Packages…** to open the packages folder.
   - Place the following files in the **User** folder:
     - `auto_tag.py` – the main plugin code.
     - `auto_tag.sublime-settings` – the settings file.

3. **Reload Sublime Text:**  
   Restart Sublime Text or use **Tools → Developer → Reload Plugins** to activate the plugin.

### Installation via Package Control

Once the plugin is published through Package Control, simply open the Command Palette (using `Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS), select **Install Package**, and then search for **AutoTagMate**.

## Configuration

The plugin’s behavior is controlled via the `auto_tag.sublime-settings` file. A sample configuration is provided below:

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

- **Using the Tab Key:**  
  When editing an eligible file, type a plain text word (e.g., `ExampleTag`) and press **Tab**. AutoTagMate will convert it into `<ExampleTag></ExampleTag>` with the cursor positioned between the tags.

- **Automatic Tag Closure on '>':**  
  If you type an opening tag (e.g., `<ExampleTag`) and finish it with `>`, the plugin automatically inserts the corresponding closing tag and positions the cursor appropriately.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
