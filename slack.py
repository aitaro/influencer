import requests, json
import os
import config

def slack_notify(text):
    requests.post(config.SLACK_WEBHOOK_URL, data = json.dumps({
        'text': text,  #通知内容
        'channel': '#twitter',
        'username': u'Python-Bot',  #ユーザー名
        'icon_emoji': u':smile_cat:',  #アイコン
        'link_names': 1  #名前をリンク化
    }))

if __name__ == '__main__':
    slack_notify('example notification')
