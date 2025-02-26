Here’s the full README.md code with proper formatting:

# 📖 Gemini AI Vim Plugin  

A **powerful Vim plugin** that integrates **Google Gemini AI** to assist with **code generation, debugging, and suggestions**. 🚀  

---

## ✨ Features
✅ **Code Generation** – Generate code snippets from natural language prompts.  
✅ **Code Debugging** – Detect and fix issues in selected code blocks.  
✅ **Code Suggestions** – Get best practices and improvements for your code.  

---

## 📥 Installation
Clone the repository:  
```sh
git clone https://github.com/Mpriynka/AiTerminal.git
cd AiTerminal

⚙️ Setup

The setup.sh script will move plugin files, set up a virtual environment, and install dependencies automatically.

chmod +x setup.sh  
./setup.sh  

🔹 After installation, set up your API key:

export GEMINI_API_KEY='your-api-key-here'

🔹 Activate the virtual environment manually if needed:

source ~/.vim/gemini_vim_env/bin/activate

🔹 To make the API key persistent, add this line to your .bashrc or .zshrc:

echo "export GEMINI_API_KEY='your-api-key-here'" >> ~/.bashrc
source ~/.bashrc

(Replace .bashrc with .zshrc if using Zsh.)
🛠 Usage
📌 Available Commands
Command	Description
:GemiGenerate	Prompts for input and generates relevant code.
:GemiDebug	Debugs selected lines of code.
:GemiSuggest	Suggests improvements for selected code.
📌 Example Usage

1️⃣ Open a Vim buffer and write some code.
2️⃣ Select lines to debug or improve using Visual mode (V).
3️⃣ Run :GemiDebug or :GemiSuggest.
4️⃣ The AI response will appear in a new buffer.
💡 Troubleshooting

🔹 Vim says "command not found"
➡ Ensure Vim detects the plugin:

:scriptnames

Look for gemini.vim in the list. If missing, restart Vim or re-run the setup script.

🔹 Plugin not working?
➡ Ensure your virtual environment is activated:

source ~/.vim/gemini_vim_env/bin/activate

