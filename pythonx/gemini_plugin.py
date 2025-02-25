import vim
import google.generativeai as genai
import os

# Load API key
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAnrC2zhLOOcvA0R9_QGNU11OwhfiEHWwk")
genai.configure(api_key=API_KEY)

def get_selected_text():
    """Retrieve selected text in Vim."""
    vim.command('let g:line_start = line("'<")')
    vim.command('let g:line_end = line("'>")')

    start = int(vim.eval("g:line_start")) - 1
    end = int(vim.eval("g:line_end"))

    return "\n".join(vim.current.buffer[start:end])

def show_message_in_buffer(message):
    """Displays messages in a separate Vim buffer."""
    vim.command('vnew GeminiMessages | setlocal buftype=nofile | setlocal noswapfile')
    vim.current.buffer[:] = message.split("\n")

def suggest_improvements():
    """Suggest improvements for the selected code using Gemini AI."""
    selected_text = get_selected_text()
    prompt = f"Suggest improvements for this code:\n{selected_text}"

    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
        # Display the full response in a separate buffer
        show_message_in_buffer(response.text)

    except Exception as e:
        vim.command(f'echo "Error: {str(e)}"')

def debug_code():
    """Debug code using Gemini AI and show results."""
    selected_text = get_selected_text()
    prompt = f"Debug and provide the corrected version of this code:\n{selected_text}"

    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
        # Display the full response in a separate buffer
        show_message_in_buffer(response.text)

    except Exception as e:
        vim.command(f'echo "Error: {str(e)}"')
