import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/statuses/update.json" #ツイートポストエンドポイント
url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# print("内容を入力してください。")
# tweet = input('>> ') #キーボード入力の取得
# print('*******************************************')

# params = {"status" : tweet}

# res = twitter.post(url, params = params) #post送信

files = {"media" : open('videos/w7IM4kxPjFCwf-4L.mp4', 'rb')}
req_media = twitter.post(url_media, files = files)

import pdb; pdb.set_trace()
if req_media.status_code != 200:
    print ("画像アップデート失敗: %s", req_media.text)
    exit()

media_id = json.loads(req_media.text)['media_id']
print ("Media ID: %d" % media_id)

# if req_media.status_code == 200: #正常投稿出来た場合
#     print("Success.")
# else: #正常投稿出来なかった場合
#     print("Failed. : %d"% res.status_code)
