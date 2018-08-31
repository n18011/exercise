#!/usr/bin/python3
# 登録済のGitHubアカウント上で目的の場所へ(下にしか行けない)

import webbrowser
import operator as op
from web_open import *

# 登録済みアカウントの表示
print('登録済みのアカウントを表示します。（入力時qで終了）')
csv_list = open_csv('url.csv')
every_dic = {csv_list[i][0]: csv_list[i][1] for i in range(len(csv_list))}
print('\n'.join([k for k in every_dic.keys()]))

# アカウントを選択させ、リポジトリを表示
tabkey_option_for_input(every_dic)
user = exit_ifq_input('>>> 表示したい人の名前を入力してください: ')
user_repo = every_dic[user] + '?tab=repositories'
repo_dic = nameandurl_repo(user_repo)
print('\n'.join([k for k in repo_dic.keys()]))

# 下層のリポジトリを見たい場合ループ、その後、ブラウザを開く
if not watch_dir_True():
    webbrowser.open(user_repo)
else:
    while True:
        tabkey_option_for_input(repo_dic)
        repo_name = exit_ifq_input('>>> 表示したいリポジトリを入力してください: ')
        child_dic = treeCheck(repo_dic[repo_name])
        if op.eq(len(child_dic), 0):
            print('ファイルです。ブラウザを開きます。')
        else:
            print('\n'.join([k for k in child_dic.keys()]))
            if watch_dir_True():
                repo_dic = child_dic
                continue
        webbrowser.open('https://github.com' + repo_dic[repo_name])
        break
