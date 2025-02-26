#!/bin/bash

echo "Setting up Gemini Vim Plugin..."

# Ensure the script is run from the repository root
if [ ! -d "autoload" ] || [ ! -d "plugin" ] || [ ! -d "pythonx" ]; then
    echo "Error: Please run this script from the cloned repository's root directory."
    exit 1
fi

# Create ~/.vim directory if not exists
mkdir -p ~/.vim

# Move autoload, plugin, and pythonx to ~/.vim/
cp -r autoload ~/.vim/
cp -r plugin ~/.vim/
cp -r pythonx ~/.vim/

echo "Plugin files moved to ~/.vim/ successfully."

# Ask user to set up a virtual environment
echo "Creating a Python virtual environment for the plugin..."
python3 -m venv ~/.vim/gemini_vim_env
echo "Activating the virtual environment..."
source ~/.vim/gemini_vim_env/bin/activate

# Install required dependencies
echo "Installing dependencies..."
pip install google-generativeai

# Prompt user to set up the API key
echo "Please set your Gemini API key:"
echo "export GEMINI_API_KEY='your_api_key_here'" >> ~/.bashrc
echo "export GEMINI_API_KEY='your_api_key_here'" >> ~/.zshrc
echo "Run 'source ~/.bashrc' or 'source ~/.zshrc' to apply changes."

echo "Setup complete! You can now use Gemini commands inside Vim."

