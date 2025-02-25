" Gemini AI integration for Vim
" Commands for code generation, debugging, and suggestions

if exists('g:loaded_gemini_commands')
  finish
endif
let g:loaded_gemini_commands = 1

" Define commands
command! GemiGenerate call gemini#GenerateCode()
command! -range GemiDebug <line1>,<line2>call gemini#DebugCode()
command! -range GemiSuggest <line1>,<line2>call gemini#SuggestPractices()
