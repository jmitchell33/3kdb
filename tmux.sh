#!/bin/sh 
tmux new-session -d
tmux split-window -h
tmux select-pane -t 0

tmux send-keys -t 0 'cd /mud && tt++ main.tin' Enter
tmux send-keys -t 1 'cd /mud && tail -fs .5 logs/*.log' Enter

tmux resize-pane -R 20

tmux -2 attach-session -d 
