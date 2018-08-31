#!/usr/bin/python3
# 世界ランクの順位と選手名からプロフィールを開く

import requests, bs4, re, webbrowser
import ittfWRwhichOpen


def profile():
    # ITTFのサイトから男子か女子の個人世界ランクのページを選択取得
    url = ittfWRwhichOpen.men_women()
    res = requests.get(url, stream=True, verify=False)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # 名前とリンクの辞書を作成
    links = soup.select('td.fab_rnk___player_id a')
    playerlink = {' '.join(link.text.strip().split()[:-1]).upper(): link.get('href') for link in links}

    # 順位出力し、rankとnameの辞書作成
    rank = {}
    print('rank: playername')
    for i, name in enumerate(playerlink.keys()):
        print('{}: {}'.format(i + 1, name))
        rank[i + 1] = name

    # リンクURLを返す
    while True:
        try:
            put = input('調べたい選手の名前かランクを入力してください：').upper()
            src = 'http://results.ittf.link'
            return '{0}{1}'.format(src, playerlink[rank[int(put)]] if put.isalnum() else playerlink[put])
        except IndexError:
            print('キーが違います。')
            continue
        break


if __name__ == '__main__':
    webbrowser.open(profile())
