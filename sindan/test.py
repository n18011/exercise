#!/usr/bin/python3
#クイズで診断　あなたのタイプは？

import random

#質問データ
head = 'あなたの今の心を表すと...'
ll = ['あなたが最も大事にしていることは？', '人に傷つけられたら、どう反応する？', 'あなたが最も惹かれる要素は？', '周りの人はあなたのことどうおもっている？', 'イライラしたとき何して気を紛らわす？', 'リラックスするためになにする？', '子供についてどう思う？', '好きなTV番組のジャンルは？', '好きな映画のジャンルは？', '好きな色は？']
ls = [{'成功': 1, 'ロマンス': 5, '知識': 2, '安定性': 4, '自由': 3}, {'攻撃的になる': 4, '落ち着いて考えない': 1, '許して忘れる': 2, '復讐': 5, '状況を理解しようとする': 3}, {'地': 1, '水': 3, '空気': 5, '火': 4, '雷': 2}, {'仕切りたがり': 4, '慈悲深い': 1, 'カリスマ性のある': 5, '何も恐れない': 3, '頑固な': 2}, {'物を壊す': 4, '散歩する': 1, '話をする': 5, '誰かにあたる': 3, '問題解決にあたる': 2}, {'瞑想': 4, '読書': 2, 'とりあえずなにかする': 1, '寝る': 3, '遊ぶ': 5}, {'生き生き': 3, 'かわいい': 1, 'ピュア': 2, 'うざい': 4, '泣き虫': 5}, {'リアリティ': 4, 'ドラマ': 2, '昼ドラ': 5, '犯罪物': 3, 'その他': 1}, {'アクション': 4, 'ヒューマンドラマ': 1, 'コメディ': 2, 'SF': 3, 'ロマンス/恋愛': 5}, {'赤': 4, '黄色': 5, '緑': 1, '青': 3, '白': 2}]
l = {1: ["A", "B", "C", "D", "E"], 2: ["A", "B", "C", "D", "E"]}

#選択合計
sec_sum = 0
#質問を表示
print(head)
print('これから{0}問質問します。1~{1}の内もっとも当てはまるものを選択してください'.format(len(ll), len(ls[0])))
for ques in range(len(ll)):
    print('-' * 10)
    print('Q{0} {1}'.format(ques + 1, ll[ques]))
    test = []
    for num, sec in enumerate(ls[ques].keys()):
        test.append(sec)
        print(num + 1, sec, sep=': ')
    #質問を選択
    def usr_pick(ans):
        global sec_sum
        take_sec = input('Please input number:').lower()
        if take_sec == '1':
            sec_sum += ls[ques][ans[0]]
        elif take_sec == '2':
            sec_sum += ls[ques][ans[1]]
        elif take_sec == '3':
            sec_sum += ls[ques][ans[2]]
        elif take_sec == '4':
            sec_sum += ls[ques][ans[3]]
        elif take_sec == '5':
            sec_sum += ls[ques][ans[4]]
        else:
            print('keyが間違っています。')
            usr_pick(ans)
    usr_pick(test)

#選択合計による診断結果表示
print('-' * 30)
print('+' * 10)
print('+', end='')
if 10 <= sec_sum <= 17:
    print('慈悲の心', end='')
elif 18 <= sec_sum <= 27:
    print('希望の心', end='')
elif 28 <= sec_sum <= 36:
    print('共感の心', end='')
elif 37 <= sec_sum <= 44:
    print('怒りの心', end='')
elif 45 <= sec_sum <= 50:
    print('愛の心', end='')
print('+')
print('+' * 10)
