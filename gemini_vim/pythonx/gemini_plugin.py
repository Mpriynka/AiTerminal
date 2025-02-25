import vim
import google.generativeai as genai
import os
import re

# Load API key
API_KEY = os.getenv("GEMINI_API_KEY", "your-gemini-api-key")
genai.configure(api_key=API_KEY)

def get_selected_text():
    """Retrieve selected text in Vim."""
    vim.command('let g:line_start = line("'<")')
    vim.command('let g:line_end = line("'>")')

    start = int(vim.eval("g:line_start")) - 1
    end = int(vim.eval("g:line_end"))

    return "\n".join(vim.current.buffer[start:end])

def extract_code_from_response(text):
    """Extract only the code block from AI response."""
    code_pattern = r"```(?:\w+)?\n(.*?)```"  # Matches code blocks
    matches = re.findall(code_pattern, text, re.DOTALL)

    if matches:
        return "\n\n".join(matches).strip()
    return ""  # If no code block found, return empty string

def extract_message_from_response(text):
    """Extract explanatory text from AI response by removing code blocks."""
    message = re.sub(r"```(?:\w+)?\n.*?```", "", text, flags=re.DOTALL).strip()
    return message

def format_message(message, mode="response"):
    """Format message with headers and styling."""
    icons = {
        "generate": "✨",
        "debug": "🐛",
        "suggest": "💡",
        "response": "🤖"
    }
    
    icon = icons.get(mode, "🤖")
    title = mode.upper()
    separator = "-" * 50
    
    header = [
        f"={' ' * 5}{icon} GEMINI AI {title} {icon}{' ' * 5}=",
        separator
    ]
    
    footer = [
        separator,
        "=== End of Gemini Response ==="
    ]
    
    return header + message.split("\n") + footer

def show_message_in_buffer(message, mode="response"):
    """Displays formatted messages in a separate Vim buffer."""
    mode_icons = {
        "generate": "✨",
        "debug": "🐛", 
        "suggest": "💡",
        "response": "🤖"
    }
    
    icon = mode_icons.get(mode, "🤖")
    title = f"{icon} Gemini:{mode.capitalize()}"
    
    vim.command(f'vnew {title} | setlocal buftype=nofile | setlocal noswapfile')
    
    # Set buffer content
    formatted_lines = format_message(message, mode)
    vim.current.buffer[:] = formatted_lines
    
    # Add syntax highlighting
    vim.command('syntax clear')
    vim.command('syntax match GeminiHeader /^=.*=$/') 
    vim.command('syntax match GeminiSubHeader /^==.*==$/') 
    vim.command('syntax match GeminiHighlight /\*\*.*\*\*/')
    vim.command('syntax match GeminiCode /`.*`/')
    
    # Set colors
    vim.command('highlight GeminiHeader ctermfg=39 guifg=#61afef cterm=bold gui=bold')
    vim.command('highlight GeminiSubHeader ctermfg=170 guifg=#c678dd') 
    vim.command('highlight GeminiHighlight ctermfg=142 guifg=#98c379 cterm=bold gui=bold')
    vim.command('highlight GeminiCode ctermfg=209 guifg=#e5c07b cterm=italic gui=italic')

def suggest_improvements():
    """Suggest improvements for the selected code using Gemini AI."""
    selected_text = get_selected_text()
    prompt = f"Suggest improvements for this code:\n{selected_text}"

    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
        
        # Extract code and explanatory message
        improved_code = extract_code_from_response(response.text)
        message = extract_message_from_response(response.text)
        
        # Display explanatory message in a separate buffer
        show_message_in_buffer(message, "suggest")
        
        # Replace selected text with code if code was found
        if improved_code:
            vim.command('let g:line_start = line("'<")')
            vim.command('let g:line_end = line("'>")')

            start = int(vim.eval("g:line_start")) - 1
            end = int(vim.eval("g:line_end"))

            vim.current.buffer[start:end] = improved_code.split("\n")

    except Exception as e:
        vim.command(f'echo "Error: {str(e)}"')

def debug_code():
    """Replace selected code with debugged version from Gemini AI."""
    selected_text = get_selected_text()
    prompt = f"Debug and provide the corrected version of this code:\n{selected_text}"

    try:
        response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
        
        # Extract code and explanatory message
        corrected_code = extract_code_from_response(response.text)
        message = extract_message_from_response(response.text)
        
        # Display explanatory message in a separate buffer
        show_message_in_buffer(message, "debug")
        
        # Replace selected text with code if code was found
        if corrected_code:
            vim.command('let g:line_start = line("'<")')
            vim.command('let g:line_end = line("'>")')

            start = int(vim.eval("g:line_start")) - 1
            end = int(vim.eval("g:line_end"))

            vim.current.buffer[start:end] = corrected_code.split("\n")

    except Exception as e:
        vim.command(f'echo "Error: {str(e)}"')
