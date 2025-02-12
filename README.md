# AutoTagMate

A lightweight Sublime Text plugin that automatically generates XML-style closing tags with smart cursor positioning. Perfect for quick text wrapping and tag completion.

---

## Features

- Convert words or phrases into tags using Tab
- Auto-close tags when typing '>'
- Works with both single words and multi-word phrases
- Smart cursor positioning
- Configurable file type support

---

## Installation

### Via Package Control

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Select `Package Control: Install Package`
3. Search for `AutoTagMate`

### Manual Installation

1. Download the repository
2. Place files in your Sublime Text Packages/User folder
3. Restart Sublime Text

---

## Usage

### Basic Tag Creation
1. Type a word: `Header`
2. Press `Tab`
3. Result: `<Header></Header>` (cursor in between)

### Multi-word Tags
1. Type a phrase: `Main Content`
2. Press `Tab`
3. Result: `<Main Content></Main Content>`

### Auto-closing
1. Type: `<Header>`
2. Result: `<Header></Header>`

---

## Configuration

Settings file (`auto_tag_mate.sublime-settings`):
```json
{
    "allowed_extensions": [".txt"],
    "allow_untitled": true
}
```

---

## Key Bindings

Default: `Tab`

To customize, add to your key bindings file:

```json
{
    "keys": ["your_key_combo"],
    "command": "insert_auto_tag",
    "context": [
        { "key": "selector", "operator": "equal", "operand": "text.plain" }
    ]
}
```

---

## Support and Contact

For any questions, feature requests, or technical support, please reach out using the contact information available at [roman-purtow.ru](https://roman-purtow.ru).
