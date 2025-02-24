#!/bin/bash
# Install the Gemini Vim Plugin

# Clone the repo
git clone https://github.com/your-username/gemini-vim-plugin.git ~/.vim/pack/plugins/start/gemini-vim-plugin

# Install dependencies
pip install google-generativeai

# Set API key instruction
echo "✅ Installation complete! Don't forget to set your API key:"
echo '   export GEMINI_API_KEY="your-api-key-here"'

