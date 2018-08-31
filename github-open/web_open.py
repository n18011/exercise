#!/usr/bin/python3
# main.pyのための関数群

import webbrowser, csv, requests, bs4, readline, sys
import operator as op


def open_csv(file_csv):
    '''
    　csvデータのリスト
    '''
    return list(csv.reader(open(file_csv)))


def tabkey_option_for_input(dic):
    '''
    input()の前に使うと
    Tabでkeyを補完する
    '''
    def completer(text, state):
        options = [x for x in dic.keys() if x.startswith(text)]
        try:
            return options[state]
        except IndexError:
            return None

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")


def treeCheck(url):
    '''
    url下のリポジトリ一覧を辞書で返す
    '''
    res = requests.get('https://github.com' + url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    tags = soup.select('a.js-navigation-open')
    return {tags[i].text: tags[i].get('href') for i in range(len(tags)) if op.gt(i, 1)}


def exit_ifq_input(string):
    '''
    'q'を入力したらプログラム終了
    '''
    ans = input(string)
    if op.eq(ans.lower(), 'q'):
        print('終了します。')
        sys.exit()
    else:
        return ans


def watch_dir_True():
    while True:
        check = exit_ifq_input('>>> リポジトリも確認しますか？[y/n]: ').lower()
        if op.eq(check, 'y'):
            return True
        elif op.eq(check, 'n'):
            return False
        else:
            print('keyが違います')
            continue
        break


def nameandurl_repo(url):
    '''
    リポジトリ名とそのurlの辞書を返す
    '''
    res = requests.get(url, verify=False)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    tags = soup.select('h3 a')

    return {tag.text.strip(): tag.get('href') for tag in tags}
