# Gemini AI Vim Plugin

A Vim plugin that integrates Google Gemini AI for code generation, debugging, and suggestions.

## Features
- **Code Generation**: Generate code snippets based on natural language prompts.
- **Code Debugging**: Detect and fix issues in selected code blocks.
- **Code Suggestions**: Receive best practices and improvements for your code.

## Installation

### Using Vim Plug
Add the following line to your `~/.vimrc`:

```vim
Plug 'your-username/gemini-vim'
```

Then restart Vim and run:
```vim
:PlugInstall
```

### Manual Installation
Clone the repository into your Vim configuration directory:

```sh
git clone https://github.com/your-username/gemini-vim.git ~/.vim/pack/plugins/start/gemini-vim
```

## Setup
Set your Gemini API key as an environment variable:

```sh
export GEMINI_API_KEY='your-api-key-here'
```

You can add this line to your `.bashrc` or `.zshrc` to make it persistent.

## Usage

### Commands
- `:GemiGenerate` - Prompts for input and generates relevant code.
- `:GemiDebug` - Debugs selected lines of code.
- `:GemiSuggest` - Suggests improvements for selected code.

### Example Usage
1. Open a Vim buffer and type a code snippet.
2. Select the lines to debug or improve using `V` (visual mode).
3. Run `:GemiDebug` or `:GemiSuggest`.
4. The response will open in a new buffer.

