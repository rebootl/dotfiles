#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

alias hx=helix
alias lg=lazygit
alias ld=lazydocker
alias rn=ranger

export EDITOR=helix

# export PATH=$HOME/.local/bin:$PATH
# alias zed=~/.local/bin/zed

# tt() {
#     kgx --tab --working-directory="$(pwd)"
# }

alias kivi-env="BYOBU_WINDOWS=kivi byobu"

# node globally in home
NPM_PACKAGES="${HOME}/.npm-packages"
export PATH="$PATH:$NPM_PACKAGES/bin"
# Preserve MANPATH if you already defined it somewhere in your config.
# Otherwise, fall back to `manpath` so we can inherit from `/etc/manpath`.
export MANPATH="${MANPATH-$(manpath)}:$NPM_PACKAGES/share/man"

. "$HOME/.cargo/env"

# eval "$(perl -I$HOME/.perl5/lib/perl5 -Mlocal::lib=$HOME/.perl5)"

# when building something using go it creates a go/ directory in my home
# this should set it to a hidden directory
export GOPATH="$HOME/.go"

export PATH="$PATH:${HOME}/.nix-profile/bin"
