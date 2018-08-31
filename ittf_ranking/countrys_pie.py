#!/usr/bin/python3
# 卓球個人世界ランキング上位５０位の国別総数
import requests, bs4, collections
import ittfWRwhichOpen
import pie_grap


def number_of_people():
    # ITTFのサイトから男子か女子の個人世界ランクのページを選択取得
    url = ittfWRwhichOpen.men_women()
    res = requests.get(url, stream=True, verify=False)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # データから国名をリストで取り出す
    elem = soup.select('table td img.fabrikLightBoxImage')
    countrys = [imgtag.get('title') for imgtag in elem]

    # dictの国別の人数を降順にソート
    cnt_countrys = collections.Counter(countrys)
    sort_dic = collections.OrderedDict(sorted(cnt_countrys.items(), key=lambda x: x[1], reverse=True))

    return sort_dic


def display(dic):
    # pie_grap用データ
    label = []
    data = []
    for country, num in dic.items():
        label.append(country)
        data.append(num)

    # displayと円グラフで出力
    for country, i in dic.items():
        print('{}: {}名'.format(country, i))
    pie_grap.pie(label, data)


if __name__ == '__main__':
    display(number_of_people())
