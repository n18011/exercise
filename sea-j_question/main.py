#!/usr/bin/python3

import csv

path = 'sea_j02'
csv_content = list(csv.reader(open(path + '.csv')))

print('{} #選択肢から一つ'.format(''.join(csv_content[2])))
print('-' * 10)

try:
    with open(path + 'save.txt', mode='x') as f:
        f.write('0 0')
except FileExistsError:
    pass
with open(path + 'save.txt') as f:
    l_strip = [s.strip().split() for s in f.readlines()]

con_YorN = input('続きから？[y/n]: ')
if con_YorN.lower() == 'y':
    n = int(l_strip[-1][0]) + 3
    point = int(l_strip[-1][1])
else:
    n = 3
    point = 0

while True:
    try:
        print('問題{} {}'.format(n - 2, csv_content[n][0]))
        for i, v in enumerate(csv_content[n][2:]):
            print('{}: {}'.format(i + 1, v))
        ans = input('答えを入力: ')
        if csv_content[n][1] == ans:
            print('正解')
            point += 1
        elif ans == 'q':
            which_save = input('保存しますか？[y/n]: ')
            if which_save.lower() == 'y':
                with open(path + 'save.txt', mode='a') as f:
                    f.write('\n{} {}'.format(n - 3, point))
                print('完了')
            else:
                with open(path + 'save.txt', mode='a') as f:
                    f.write('\n0 0')
                print('終了します。')
            break
        else:
            print('不正解')
            print('正答　{}'.format(csv_content[n][1]))
        n += 1
    except IndexError:
        break

    with open(path + 'save.txt', mode='a') as f:
        f.write('\n0 0')
    print('-' * 10)

print('-' * 20)
print('{0:8}結果'.format(' '))
print('-' * 20)
print('{}問中　{}問正解'.format(n - 3, point))
print('正答率　{}%'.format(point / (n - 3) * 100))
print('-' * 20)
