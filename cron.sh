#!/bin/bash
PATH=/home/aitaro/.anyenv/envs/pyenv/shims:/home/aitaro/.anyenv/envs/pyenv/bin:/home/aitaro/.anyenv/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
SLACK_WEBHOOK_URL='https://hooks.slack.com/services/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'
echo $PATH
$(echo date)
pipenv run python main.py
echo 'finish'
