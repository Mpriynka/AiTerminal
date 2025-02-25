" Gemini AI integration functions
" Autoloaded functions for Gemini AI in Vim

" Function to create a stylized buffer for messages
function! s:CreateMessageBuffer(title)
    " Create a vertical split for the message buffer
    vnew
    let bufnr = bufnr('%')
    setlocal buftype=nofile
    setlocal noswapfile
    setlocal nowrap
    execute 'file ' . a:title
    
    " Add some styling with syntax highlighting
    syntax clear
    syntax match GeminiHeader /^=.*=$/
    syntax match GeminiSubHeader /^==.*==$/
    syntax match GeminiHighlight /\*\*.*\*\*/
    syntax match GeminiCode /`.*`/
    
    " Set colors (adjust these colors to match your color scheme)
    highlight GeminiHeader ctermfg=39 guifg=#61afef cterm=bold gui=bold
    highlight GeminiSubHeader ctermfg=170 guifg=#c678dd
    highlight GeminiHighlight ctermfg=142 guifg=#98c379 cterm=bold gui=bold
    highlight GeminiCode ctermfg=209 guifg=#e5c07b cterm=italic gui=italic
    
    return bufnr
endfunction

" Function to pretty-print the message text
function! s:FormatMessage(message, mode)
    let mode_icons = {
        \ 'generate': '✨',
        \ 'debug': '🐛',
        \ 'suggest': '💡'
        \ }
    
    let icon = get(mode_icons, a:mode, '🤖')
    let title = toupper(a:mode)
    let separator = repeat('-', 50)
    
    let header = [
        \ '=' . repeat(' ', 5) . icon . ' GEMINI AI ' . title . ' ' . icon . repeat(' ', 5) . '=',
        \ separator
        \ ]
    
    let footer = [
        \ separator,
        \ '=== End of Gemini Response ==='
        \ ]
    
    return header + split(a:message, '\n') + footer
endfunction

" Function to generate code using Gemini API
function! gemini#GenerateCode()
    let code = input("Enter your prompt: ")
    let api_key = $GEMINI_API_KEY
    let output = system("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " generate " . shellescape(code) . " " . shellescape(api_key))
    
    " Extract code and message from the output
    let code_start = stridx(output, "CODE_START") + 10
    let code_end = stridx(output, "CODE_END")
    let message_start = stridx(output, "MESSAGE_START") + 13
    let message_end = stridx(output, "MESSAGE_END")
    
    " Display message with formatting
    if message_start > 13 && message_end > 0
        let message_content = output[message_start:message_end-1]
        let buf = s:CreateMessageBuffer('✨ Gemini:Generate')
        call setline(1, s:FormatMessage(message_content, 'generate'))
    endif
    
    " Insert code at cursor position in the current buffer
    if code_start > 10 && code_end > 0
        let code_content = output[code_start:code_end-1]
        if len(code_content) > 0
            call append(line('.'), split(code_content, '\n'))
        endif
    endif
endfunction

" Function to debug selected code (multi-line support)
function! gemini#DebugCode() range
    let api_key = $GEMINI_API_KEY
    let start_line = a:firstline
    let end_line = a:lastline
    let code = join(getline(start_line, end_line), "\n")

    let output = system("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " debug " . shellescape(code) . " " . shellescape(api_key))
    
    " Extract code and message from the output
    let code_start = stridx(output, "CODE_START") + 10
    let code_end = stridx(output, "CODE_END")
    let message_start = stridx(output, "MESSAGE_START") + 13
    let message_end = stridx(output, "MESSAGE_END")
    
    " Display message with formatting
    if message_start > 13 && message_end > 0
        let message_content = output[message_start:message_end-1]
        let buf = s:CreateMessageBuffer('🐛 Gemini:Debug')
        call setline(1, s:FormatMessage(message_content, 'debug'))
    endif
    
    " Replace selected text with debugged code
    if code_start > 10 && code_end > 0
        let code_content = output[code_start:code_end-1]
        if len(code_content) > 0
            execute start_line . "," . end_line . "delete"
            call append(start_line - 1, split(code_content, "\n"))
        endif
    endif
endfunction

" Function to suggest better code practices (multi-line support)
function! gemini#SuggestPractices() range
    let api_key = $GEMINI_API_KEY
    let start_line = a:firstline
    let end_line = a:lastline
    let code = join(getline(start_line, end_line), "\n")

    let output = system("python3 " . expand('~/.vim/plugin/gemini_helper.py') . " suggest " . shellescape(code) . " " . shellescape(api_key))
    
    " Extract code and message from the output
    let code_start = stridx(output, "CODE_START") + 10
    let code_end = stridx(output, "CODE_END")
    let message_start = stridx(output, "MESSAGE_START") + 13
    let message_end = stridx(output, "MESSAGE_END")
    
    " Display message with formatting
    if message_start > 13 && message_end > 0
        let message_content = output[message_start:message_end-1]
        let buf = s:CreateMessageBuffer('💡 Gemini:Suggest')
        call setline(1, s:FormatMessage(message_content, 'suggest'))
    endif
    
    " Replace selected text with suggested code
    if code_start > 10 && code_end > 0
        let code_content = output[code_start:code_end-1]
        if len(code_content) > 0
            execute start_line . "," . end_line . "delete"
            call append(start_line - 1, split(code_content, "\n"))
        endif
    endif
endfunction

" Add keyboard mappings for quick access (optional)
" You can add these to your vimrc or keep them here
" nnoremap <leader>gg :GemiGenerate<CR>
" vnoremap <leader>gd :GemiDebug<CR>
" vnoremap <leader>gs :GemiSuggest<CR>
