" Function to create a stylized output buffer
function! gemini#OpenBuffer(title)
    " Open a new split window for the response
    belowright new
    setlocal buftype=nofile
    setlocal noswapfile
    setlocal nowrap
    setlocal modifiable
    setlocal number
    file [Gemini] " Set buffer title

    " Add a stylish header
    call setline(1, repeat("=", 40))
    call setline(2, " Gemini AI - " . a:title)
    call setline(3, repeat("=", 40))
    call setline(4, "")

    " Return the buffer number for further modifications
    return bufnr('%')
endfunction

" Function to format and display output
function! gemini#DisplayResult(title, result)
    let buf = gemini#OpenBuffer(a:title)
    call setline(5, a:result)
    setlocal modifiable
    normal gg
endfunction

" Updated Generate function with better formatting
function! gemini#GenerateCode()
    let code = input("Enter your prompt: ")
    let api_key = $GEMINI_API_KEY
    let result = systemlist("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " generate " . shellescape(code) . " " . shellescape(api_key))

    " Display result with formatting
    call gemini#DisplayResult("Generated Code", result)
    setlocal filetype=python
endfunction

" Updated Debug function with better formatting
function! gemini#DebugCode() range
    let api_key = $GEMINI_API_KEY
    let start_line = a:firstline
    let end_line = a:lastline
    let code = join(getline(start_line, end_line), "\n")
    let result = systemlist("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " debug " . shellescape(code) . " " . shellescape(api_key))

    " Display result with formatting
    call gemini#DisplayResult("Debugged Code", result)
    setlocal filetype=python
endfunction

" Updated Suggest function with better formatting
function! gemini#SuggestPractices() range
    let api_key = $GEMINI_API_KEY
    let start_line = a:firstline
    let end_line = a:lastline
    let code = join(getline(start_line, end_line), "\n")
    let result = systemlist("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " suggest " . shellescape(code) . " " . shellescape(api_key))

    " Display result with formatting
    call gemini#DisplayResult("Suggestions", result)
    setlocal filetype=markdown
endfunction

