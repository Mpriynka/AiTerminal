import vim
import openai
import os

def load_api_key():
    """Load API key from environment variable or config file."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        try:
            with open(os.path.expanduser("~/.gemini_api_key"), "r") as f:
                api_key = f.read().strip()
        except FileNotFoundError:
            api_key = ""
    return api_key

API_KEY = load_api_key()
openai.api_key = API_KEY


def get_selected_text():
    """Retrieve selected text in Vim."""
    vim.command('let g:selected_text = @"')  # Copy selection to register
    return vim.eval('g:selected_text')

def generate_code():
    """Generate code using Gemini AI."""
    prompt = vim.eval('input("Enter prompt: ")')
    response = openai.ChatCompletion.create(
        model="gemini",
        messages=[{"role": "user", "content": prompt}]
    )
    vim.command(f'echo "{response["choices"][0]["message"]["content"]}"')

def debug_code():
    """Debug selected code using Gemini AI."""
    selected_text = get_selected_text()
    prompt = f"Debug the following code:\n{selected_text}"
    response = openai.ChatCompletion.create(
        model="gemini",
        messages=[{"role": "user", "content": prompt}]
    )
    vim.command(f'echo "{response["choices"][0]["message"]["content"]}"')
def suggest_code():
    """Suggest better alternatives for selected code."""
    selected_text = get_selected_text()
    prompt = f"Suggest a better alternative for this code:\n{selected_text}"
    response = openai.ChatCompletion.create(
        model="gemini",
        messages=[{"role": "user", "content": prompt}]
    )
    vim.command(f'echo "{response["choices"][0]["message"]["content"]}"')

# Vim commands
vim.command('command! GenCode py3 generate_code()')
vim.command('command! DebugCode py3 debug_code()')
vim.command('command! SuggestCode py3 suggest_code()')
