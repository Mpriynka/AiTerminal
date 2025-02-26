#!/bin/bash

echo "Setting up Gemini Vim Plugin..."

# The script expects the presence of 'autoload', 'plugin', and 'pythonx' directories.
if [ ! -d "autoload" ] || [ ! -d "plugin" ] || [ ! -d "pythonx" ]; then
    echo "Error: Please run this script from the cloned repository's root directory."
    exit 1
fi

mkdir -p ~/.vim

# Copy essential plugin components to the Vim configuration directory (~/.vim/).
cp -r autoload ~/.vim/
cp -r plugin ~/.vim/
cp -r pythonx ~/.vim/

echo "Plugin files moved to ~/.vim/ successfully."

# Set up a dedicated Python virtual environment for the plugin.
echo "Creating a Python virtual environment for the plugin..."
python3 -m venv ~/.vim/gemini_vim_env

# Activate the virtual environment.
echo "Activating the virtual environment..."
source ~/.vim/gemini_vim_env/bin/activate

echo "Installing dependencies..."
pip install google-generativeai

# Inform the user about API key setup and append the necessary environment variable
echo "Please set your Gemini API key:"
echo "export GEMINI_API_KEY='your_api_key_here'" >> ~/.bashrc
echo "export GEMINI_API_KEY='your_api_key_here'" >> ~/.zshrc

echo "Run 'source ~/.bashrc' or 'source ~/.zshrc' to apply changes."

echo "Setup complete! You can now use Gemini commands inside Vim."

