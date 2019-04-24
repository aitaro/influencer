#!/bin/bash
PATH=/home/aitaro/.anyenv/envs/pyenv/shims:/home/aitaro/.anyenv/envs/pyenv/bin:/home/aitaro/.anyenv/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
echo $PATH
$(echo date)
pipenv run python main.py >> /home/aitaro/influencer/stdout.log
echo 'finish'
