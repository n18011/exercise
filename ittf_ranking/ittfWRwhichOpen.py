#!/usr/bin/python3
# ITTFの卓球（男子or女子）個人世界ランクを開く

import bs4, webbrowser, requests
import operator as op


def men_women():
    '''
    男子か女子のurlを返す
    '''
    url = 'https://www.ittf.com/rankings/'
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    elems = soup.select('p a')
    url_dic = {tag.text.strip().split()[1]: tag.get('href') for tag in elems[:2]}
    while True:
        try:
            sex_put = input('[Men] or [Women]?: ').lower()
            return url_dic[sex_put]
        except KeyError:
            print('キーが違います。')
            continue
        break


if __name__ == '__main__':
    webbrowser.open(men_women())
