#!/usr/bin/env python3
import sys
import google.generativeai as genai
import re

def extract_code_and_message(text):
    """Separate code blocks from explanatory text in the response."""
    # Find code blocks (text between triple backticks)
    code_blocks = re.findall(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    
    if code_blocks:
        # Join multiple code blocks if present
        code = "\n\n".join(code_blocks).strip()
        
        # Remove code blocks from original text to get the message
        message = re.sub(r"```(?:\w+)?\n.*?```", "", text, flags=re.DOTALL).strip()
        return code, message
    
    # If no code blocks found, return empty code and full text as message
    return "", text.strip()

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 gemini_helper.py <mode> <code> <api_key>")
        sys.exit(1)

    mode, code, api_key = sys.argv[1], sys.argv[2], sys.argv[3]
    genai.configure(api_key=api_key)

    prompts = {
        "generate": f"Generate code for this request:\n{code}",
        "debug": f"Debug and provide the corrected version of this code:\n{code}",
        "suggest": f"Suggest improvements for this code:\n{code}"
    }

    if mode not in prompts:
        print("Invalid mode. Use 'generate', 'debug', or 'suggest'.")
        sys.exit(1)

    response = genai.GenerativeModel("gemini-pro").generate_content(prompts[mode])
    
    # Extract code and message from the response
    code, message = extract_code_and_message(response.text)
    
    # Output in a format that can be parsed by Vim
    print("CODE_START")
    print(code)
    print("CODE_END")
    print("MESSAGE_START")
    print(message)
    print("MESSAGE_END")

if __name__ == "__main__":
    main()
