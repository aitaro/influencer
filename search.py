#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import json
import yaml

from time import sleep
from googleapiclient.discovery import build

GOOGLE_API_KEY          = os.environ['GOOGLE_API_KEY']
CUSTOM_SEARCH_ENGINE_ID = os.environ['CUSTOM_SEARCH_ENGINE_ID']

DATA_DIR = 'data'

def makeDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def getSearchResponse(keyword):
    today = datetime.datetime.today().strftime("%Y%m%d")
    timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

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

    out = {'snapshot_ymd': today, 'snapshot_timestamp': timestamp, 'response': []}
    out['response'] = response

    # レスポンスを格納
    f = open(f"response/text/{keyword}.yml", "w+")
    f.write(yaml.dump(out, allow_unicode=True))

    return out

def getRelatedImg(keyword):
    today = datetime.datetime.today().strftime("%Y%m%d")
    timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    page_limit = 2
    start_index = 1
    response = []
    img_list = []

    for nPage in range(0, page_limit):
        print("Reading page number:", nPage + 1)

        try:
            response.append(service.cse().list(
                q=keyword,     # Search words
                cx=CUSTOM_SEARCH_ENGINE_ID,        # custom search engine key
                lr='lang_ja',      # Search language
                num=10,            # Number of images obtained by one request (Max 10)
                start=start_index,
                searchType='image' # search for images
            ).execute())

            start_index = response[nPage].get("queries").get("nextPage")[0].get("startIndex")

        except Exception as e:
            print(e)

    print(type(response))

    # with open(os.path.join(save_res_path, 'api_response.pickle'), mode='wb') as f:
    #     pickle.dump(response, f)

    for one_res in range(len(response)):
        if len(response[one_res]['items']) > 0:
            for i in range(len(response[one_res]['items'])):
                img_list.append(response[one_res]['items'][i]['link'])

    out = {'snapshot_ymd': today, 'snapshot_timestamp': timestamp, 'response': []}
    out['response'] = response

    # レスポンスを格納
    f = open(f"response/image/{keyword}.yml", "w+")
    f.write(yaml.dump(out, allow_unicode=True))

    return out


if __name__ == '__main__':

    target_keyword = 'IDÉE CAFÉ PARC'
    print(getRelatedImg(target_keyword))
