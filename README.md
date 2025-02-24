# ✨ Gemini AI Vim Plugin

A Vim plugin powered by Gemini AI that helps you:
- **Generate code** based on prompts.
- **Debug selected code** to identify errors.
- **Suggest better alternatives** for code improvements.

## 📌 Features
- `:GenCode` → Generate code from a text prompt.
- `:DebugCode` → Debug selected code.
- `:SuggestCode` → Suggest improvements for selected code.

## 🚀 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/AiTerminal.git
cd AiTerminal
```

### **2️⃣ Run the Install Script**
```bash
bash install.sh
```
This will:
- Install dependencies.
- Copy the Vim plugin to `~/.vim/plugin/`.
- Set up the required API key.

### **3️⃣ Set Up Your API Key**
Create an environment variable for the Gemini AI API key:
```bash
export GEMINI_API_KEY="your_api_key_here"
```
To make this persistent, add it to your `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

## 🛠️ Usage
After installation, restart Vim and use the following commands:

- **Generate Code** → `:GenCode` → Enter a prompt, and AI generates code.
- **Debug Code** → `:DebugCode` → Debugs the currently selected code.
- **Suggest Improvements** → `:SuggestCode` → Suggests better alternatives.

## 📁 Project Structure
```
AiTerminal/
│── install.sh            # Installation script
│── plugin/               # Contains the Vim plugin
│   ├── gemini_plugin.py  # The main Vim plugin logic
│── README.md             # Documentation
│── test.py               # (Optional) Test cases
```
