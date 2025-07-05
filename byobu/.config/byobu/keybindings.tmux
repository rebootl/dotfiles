unbind-key -n C-a
set -g prefix ^A
set -g prefix2 F12
bind a send-prefix

# setting these in profile instead
# actually profile didn't work setting them here
bind-key -n M-h previous-window
bind-key -n M-l next-window
bind-key -n M-j switch-client -p
bind-key -n M-k switch-client -n
