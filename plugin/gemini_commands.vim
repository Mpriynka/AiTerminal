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

" Create a Gemini menu in Vim
if has('gui_running') || has('nvim')
  amenu Plugin.Gemini.Generate\ Code :GemiGenerate<CR>
  vmenu Plugin.Gemini.Debug\ Selected\ Code :GemiDebug<CR>
  vmenu Plugin.Gemini.Suggest\ Improvements :GemiSuggest<CR>
endif
