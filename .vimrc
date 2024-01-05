call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')
  Plug 'preservim/nerdtree'
  Plug 'vim-scripts/indentpython.vim'	
  Plug 'Valloric/YouCompleteMe'
  Plug 'tmsvg/pear-tree'
call plug#end()
au BufNewFile, BufRead *.py
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix
au BufNewFile, BufRead *.js, *.html, *.css
    \ set tabstop=2
    \ set softtabstop=2
    \ set shiftwidth=2
au BufRead, BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-h> <C-w>h
nnoremap <C-l> <C-w>l
filetype plugin on

set shiftwidth=4

set tabstop=4
set expandtab

set expandtab

set smartindent
set autoindent
set smarttab

set number
autocmd FileType c,python,java,javascript set number
