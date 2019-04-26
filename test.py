# from janome.tokenizer import Tokenizer
#
# t = Tokenizer()
#
# s = '東新宿のコトカフェ。女子会やパーティー、イベントに使える東新宿のカフェです。伊勢丹や花園神社から近いので、お近くに寄った際は是非お立ち寄りください。結婚式の2次会、3次会にも使えます。'
#
# print(type(t.tokenize(s)))
# # <class 'list'>
#
# print(type(t.tokenize(s)[0]))
# # <class 'janome.tokenizer.Token'>
#
# for token in t.tokenize(s, stream=True):
#     print(token)


import oseti

analyzer = oseti.Analyzer()
print(analyzer.analyze('東新宿のコトカフェ。女子会やパーティー、イベントに使える東新宿のカフェです。伊勢丹や花園神社から近いので、お近くに寄った際は是非お立ち寄りください。結婚式の2次会、3次会にも使えます。'))
print(analyzer.analyze('コトカフェ/coto cafe (新宿三丁目/カフェ)の店舗情報は食べログでチェック！１人でも仲間とでも行きつけにしたいとっておきの場所！ 【分煙 / 飲み放題あり / ネット予約可】口コミや評価、写真など、ユーザーによるリアルな情報が満載です！地図や料理メニューなどの詳細情報も充実。'))
# client = language.LanguageServiceClient()
#
# if isinstance(text, six.binary_type):
#     text = text.decode('utf-8')
#
# document = types.Document(
#     content=text.encode('utf-8'),
#     type=enums.Document.Type.PLAIN_TEXT)
#
# # Detect and send native Python encoding to receive correct word offsets.
# encoding = enums.EncodingType.UTF32
# if sys.maxunicode == 65535:
#     encoding = enums.EncodingType.UTF16
#
# result = client.analyze_entity_sentiment(document, encoding)
# set_trace()
#
# for entity in result.entities:
#     print('Mentions: ')
#     print(u'Name: "{}"'.format(entity.name))
#     for mention in entity.mentions:
#         print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
#         print(u'  Content : {}'.format(mention.text.content))
#         print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
#         print(u'  Sentiment : {}'.format(mention.sentiment.score))
#         print(u'  Type : {}'.format(mention.type))
#     print(u'Salience: {}'.format(entity.salience))
#     print(u'Sentiment: {}\n'.format(entity.sentiment))
