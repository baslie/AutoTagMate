# AutoTagMate: Your Universal AI Prompt Structuring Tool

Want to level up your prompts for ChatGPT, Claude AI, or any other neural network-based system? **AutoTagMate** is a lightweight Sublime Text plugin that helps you quickly wrap text in XML-style tags—enhancing clarity and focus for your AI queries. Now works in **ALL file types** out of the box, making it perfect for any workflow.

---

## Why It's Perfect for AI Work

- **Boost Prompt Clarity**  
  Clearly separate instruction sections, examples, or code snippets in your AI prompts by automatically wrapping text in tags—making it easier for the model to understand your intent.

- **Universal File Support**  
  Works in ALL file types by default—Python, HTML, Markdown, plain text, code files, and even unsaved documents without extensions.

- **Zero Hassle**  
  Set a hotkey (default: `Ctrl+\` / `Cmd+\`) to instantly wrap your text in a tag pair.

- **No Configuration Required**  
  Works immediately after installation across all your files and projects.

---

## Also Great for HTML & Code Wrapping

While AutoTagMate is ideal for structuring AI prompts, it's still a powerful companion for developers and content creators who need to wrap text in HTML tags, XML markup, or custom tags. Whether you're editing a website, writing documentation, or adding markup to any file type, AutoTagMate has you covered.

---

## Key Features

- **Instant Tag Wrapping**  
  Automatically wraps a selected word or phrase in `<tag></tag>` with a single hotkey press.

- **Auto-insert Closing Tags**  
  Type an opening tag (e.g., `<Header>`), and the plugin automatically adds the corresponding closing tag.

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
3. AutoTagMate wraps it: `` or ``.

### Auto-closing Tags

- Start typing an opening tag, like ``.
- AutoTagMate automatically inserts ``.

### Works Everywhere

- **Python files**: Perfect for docstring structuring and comments
- **HTML/CSS**: Quick tag creation and markup
- **Markdown**: Enhanced structure for documentation
- **Plain text**: AI prompt organization
- **Any file type**: Universal text wrapping solution

---

## Configuration

AutoTagMate settings are stored in the **auto_tag_mate.sublime-settings** file:

