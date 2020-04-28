#!/bin/sh
tmux new-session \; \
  send-keys "printf '\033]2;%s\033\\' 'telegram'" C-m \; \
  send-keys 'python tg_dispatcher.py' C-m \; \
  split-window -v -p 66 \; \
  send-keys "printf '\033]2;%s\033\\' 'teamspeak'" C-m \; \
  send-keys 'python ts_dispatcher.py' C-m \; \
  split-window -v -p 50 \; \
  send-keys "printf '\033]2;%s\033\\' 'twitter'" C-m \; \
  send-keys 'python tw_dispatcher.py' C-m \; \
  # send-keys "printf '\033]2;%s\033\\' 'telegram'" C-m \; \
  # send-keys 'free -m' C-m \; \
  # send-keys ' ' C-m \; \
  # split-window -v \; \
  # send-keys "printf '\033]2;%s\033\\' 'teamspeak'" C-m \; \
  # # send-keys 'python ts_dispatcher.py' C-m \; \
  # split-window -v \; \
  # send-keys "printf '\033]2;%s\033\\' 'twitter'" C-m \; \
  # # send-keys 'python tw_dispatcher.py' C-m \; \