#!/usr/bin/env python
#coding:utf-8

import requests
import re

# 翻訳実行
def trenslator(key, text, lang, **kwargs):

    query = {
        'key': key,
        'text': text,
        'lang': lang,
        'format': 'html'
    }

    response = requests.request('GET', 'https://translate.yandex.net/api/v1.5/tr.json/translate?', params=query)
    traslated = re.sub("<.*?>", '', response.text)
    return traslated

def translate_ru_en(input_text, from_to_lang):
    '''入力文字列を翻訳する
        input_text: 入力文字列
        from_to_lang: 翻訳言語のペア（'ru-en'のように記載する）
    '''

    # APIキー
    api_key = 'trnsl.1.1.20171119T064344Z.e64c1b81753e2ed3.ed8428f7d95d72ac1a4106d4126c1b5188a0e17d' #APIキー

    # 翻訳対象
    text = input_text #翻訳する文章
    #text = 'Российская Федерация' #翻訳する文章
    to_lang = from_to_lang #翻訳先の言語
    #to_lang = 'ru-en' #翻訳先の言語

    #token = get_access_token(to_lang, api_key)

    print(trenslator(api_key, text, to_lang))

def main():

    input_text = 'Российская Федерация'
    from_to_lang = 'ru-en'

    translate_ru_en(input_text, from_to_lang)

if __name__ == '__main__':
    main()
