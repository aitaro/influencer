#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import json

from time import sleep
from googleapiclient.discovery import build

GOOGLE_API_KEY          = "AIzaSyAKZJlNWc5fc0AR0fFy_SWJ3WV2ts-yXEk"
CUSTOM_SEARCH_ENGINE_ID = "004824719477391694589:_w09q_fo_c0"

DATA_DIR = 'data'

def makeDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def getSearchResponse(keyword):
    today = datetime.datetime.today().strftime("%Y%m%d")
    timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    # makeDir(DATA_DIR)s

    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

    page_limit = 1
    start_index = 1
    response = []
    for n_page in range(0, page_limit):
        try:
            sleep(1)
            response.append(service.cse().list(
                q=keyword,
                cx=CUSTOM_SEARCH_ENGINE_ID,
                lr='lang_ja',
                num=10,
                start=start_index
            ).execute())
            start_index = response[n_page].get("queries").get("nextPage")[0].get("startIndex")
        except Exception as e:
            print(e)
            break

    # レスポンスをjson形式で保存
    # save_response_dir = os.path.join(DATA_DIR, 'response')
    # makeDir(save_response_dir)
    out = {'snapshot_ymd': today, 'snapshot_timestamp': timestamp, 'response': []}
    out['response'] = response
    return out
    # jsonstr = json.dumps(out, ensure_ascii=False)
    # with open(os.path.join(save_response_dir, 'response_' + today + '.json'), mode='w') as response_file:
    #     response_file.write(jsonstr)

if __name__ == '__main__':

    target_keyword = 'ア・ラ・カンパーニュ池袋店 tabelog'
    getSearchResponse(target_keyword)
