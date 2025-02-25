" Gemini AI integration functions
" Autoloaded functions for Gemini AI in Vim

" Function to generate code using Gemini API
function! gemini#GenerateCode()
    let code = input("Enter your prompt: ")
    let api_key = $GEMINI_API_KEY
    let result = systemlist("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " generate " . shellescape(code) . " " . shellescape(api_key))
    
    " Display result in a new buffer
    vnew
    setlocal buftype=nofile
    setlocal noswapfile
    file GeminiMessages
    call setline(1, result)
endfunction

" Function to debug selected code (multi-line support)
function! gemini#DebugCode() range
    let api_key = $GEMINI_API_KEY
    let start_line = a:firstline
    let end_line = a:lastline
    let code = join(getline(start_line, end_line), "\n")

    let result = systemlist("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " debug " . shellescape(code) . " " . shellescape(api_key))
    
    " Display result in a new buffer
    vnew
    setlocal buftype=nofile
    setlocal noswapfile
    file GeminiMessages
    call setline(1, result)
endfunction

" Function to suggest better code practices (multi-line support)
function! gemini#SuggestPractices() range
    let api_key = $GEMINI_API_KEY
    let start_line = a:firstline
    let end_line = a:lastline
    let code = join(getline(start_line, end_line), "\n")

    let result = systemlist("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " suggest " . shellescape(code) . " " . shellescape(api_key))
    
    " Display result in a new buffer
    vnew
    setlocal buftype=nofile
    setlocal noswapfile
    file GeminiMessages
    call setline(1, result)
endfunction
