#!/usr/bin/env python3

import sys
import google.generativeai as genai

def main():
    # Expected arguments: mode (operation type), code (input code snippet), and API key.
    if len(sys.argv) < 4:
        print("Usage: python3 gemini_helper.py <mode> <code> <api_key>")
        sys.exit(1) 

    # Extract command-line arguments.
    mode, code, api_key = sys.argv[1], sys.argv[2], sys.argv[3]

    # Configure the Generative AI client with the provided API key.
    genai.configure(api_key=api_key)

    prompts = {
        "generate": f"Generate code for this request:\n{code}",
        "debug": f"Debug and provide the corrected version of this code:\n{code}", 
        "suggest": f"Suggest improvements for this code:\n{code}" 
    }

    # Validate the selected mode.
    if mode not in prompts:
        print("Invalid mode. Use 'generate', 'debug', or 'suggest'.")
        sys.exit(1) 

    response = genai.GenerativeModel("gemini-1.5-pro-latest").generate_content(prompts[mode])

    print(response.text.strip())

if __name__ == "__main__":
    main()

