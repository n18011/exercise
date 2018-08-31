#!/usr/bin/python3
# 選手情報を出力する
import search_profile, requests, bs4


def player_data():
    '''
    選手のプロフィールデータを辞書で返す
    '''
    # 選手のプロフィールがあるURLを取得
    url = search_profile.profile()
    res = requests.get(url, stream=True, verify=False)
    res.raise_for_status()

    # ラベルとデータのテキストを選択,リスト化
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    elems = soup.select('.fabrikElementReadOnly')
    rabels = soup.select('.fabrikLabel')

    elemslist = [elem.text.strip() for elem in elems]
    rabelslist = [rabel.text.strip() for rabel in rabels]

    # 辞書で紐付け
    data_dic = {rabel: elem for rabel, elem in zip(rabelslist, elemslist)}

    # 画像のリンクを辞書に追加
    src = soup.select('.fabrikLightBoxImage')
    for img in src:
        data_dic['Photo'] = img.get('src')

    return data_dic


def display(dic):
    for k, v in dic.items():
        print('-' * 30)
        print(k)
        print()
        print(v)
        print()


if __name__ == '__main__':
    display(player_data())
