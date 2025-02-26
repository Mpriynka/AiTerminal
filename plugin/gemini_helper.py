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
        "generate": f"Generate code only (no explanation) for this request. If the request is not related to programming, respond with 'Invalid request: Please provide a programming-related prompt.':\n{code}",
        "debug": f"Debug and provide the corrected version of this code and if required, short explanation. If the input is not code, respond with 'Invalid request: Please provide a code snippet to debug.':\n{code}", 
        "suggest": f"Suggest improvements for this code only (no explanation). If the input is not code, respond with 'Invalid request: Please provide a code snippet to improve.':\n{code}" 
    }

    # Validate the selected mode.
    if mode not in prompts:
        print("Invalid mode. Use 'generate', 'debug', or 'suggest'.")
        sys.exit(1) 

    response = genai.GenerativeModel("gemini-1.5-pro-latest").generate_content(prompts[mode])

    print(response.text.strip())

if __name__ == "__main__":
    main()

