#!/bin/sh
tmux new-session -s Dispatchers \; \
  send-keys "printf '\033]2;%s\033\\' 'telegram'" C-m \; \
  send-keys 'python tg_dispatcher.py' C-m \; \
  split-window -v -p 75 \; \
  send-keys "printf '\033]2;%s\033\\' 'teamspeak'" C-m \; \
  send-keys 'python ts_dispatcher.py' C-m \; \
  split-window -v -p 75 \; \
  send-keys "printf '\033]2;%s\033\\' 'twitter'" C-m \; \
  send-keys 'python tw_dispatcher.py' C-m \; \
  split-window -v -p 50 \; \
  send-keys "printf '\033]2;%s\033\\' 'bfxpulse'" C-m \; \
  send-keys 'python pulse_dispatcher.py' C-m \; \