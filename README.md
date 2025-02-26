# 📖 Gemini AI Vim Plugin 

A **powerful Vim plugin** that integrates **Google Gemini AI** to assist with **code generation, debugging, and suggestions**. 🚀 

---

## ✨ Features

* ✅ **Code Generation** – Generate code snippets from natural language prompts.
* ✅ **Code Debugging** – Detect and fix issues in selected code blocks.
* ✅ **Code Suggestions** – Get best practices and improvements for your code.

---

## 📥 Installation

1.  Clone the repository:

    ```sh
    git clone [https://github.com/Mpriynka/AiTerminal.git](https://github.com/Mpriynka/AiTerminal.git)
    cd AiTerminal
    ```

### ⚙️ Setup

1.  Make the setup script executable and run it:

    ```sh
    chmod +x setup.sh
    ./setup.sh
    ```

2.  Set up your API key:

    ```sh
    export GEMINI_API_KEY='your-api-key-here'
    ```

3.  (Optional) Activate the virtual environment manually if needed:

    ```sh
    source ~/.vim/gemini_vim_env/bin/activate
    ```

4.  (Optional) To make the API key persistent, add the following line to your `~/.bashrc` or `~/.zshrc` file:

    ```sh
    echo "export GEMINI_API_KEY='your-api-key-here'" >> ~/.bashrc
    source ~/.bashrc
    ```

    (Replace `.bashrc` with `.zshrc` if you are using Zsh.)

## 🛠 Usage

### 📌 Available Commands

| Command        | Description                                  |
| -------------- | -------------------------------------------- |
| `:GemiGenerate` | Prompts for input and generates relevant code. |
| `:GemiDebug`    | Debugs selected lines of code.              |
| `:GemiSuggest`  | Suggests improvements for selected code.       |

### 📌 Example Usage

1.  Open a Vim buffer and write some code.
2.  Select lines to debug or improve using Visual mode (`V`).
3.  Run `:GemiDebug` or `:GemiSuggest`.
4.  The AI response will appear in a new buffer.

## 💡 Troubleshooting

### 🔹 Vim says "command not found"

* ➡ Ensure Vim detects the plugin:

    ```vim
    :scriptnames
    ```

    Look for `gemini.vim` in the list. If it is missing, restart Vim or re-run the setup script.

### 🔹 Plugin not working?

* ➡ Ensure your virtual environment is activated:

    ```sh
    source ~/.vim/gemini_vim_env/bin/activate
    ```
