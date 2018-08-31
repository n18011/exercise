#!/usr/bin/python3
import random


class Player:
    def __init__(self, name, job, justu):
        self.name = name
        self.job = job
        self.justu = justu

    def set_hp(self):
        if self.job == '人':
            self.hp = 10
        elif self.job == '下忍':
            self.hp = 15
        elif self.job == '中忍':
            self.hp = 18
        elif self.job == '上忍':
            self.hp = 20
        elif self.job in ('火影', '風影', '水影', '土影', '雷影'):
            self.hp = 23
        return self.hp

    def attck(self):
        justu, power = random.choice(list(self.justu.items()))
        self.power = power
        return justu


def diff_hp(deffender, attcker):
    deffender.hp = deffender.hp - attcker.power
    if deffender.hp >= 0:
        print(f'{deffender.name}の残り体力{deffender.hp}')
    else:
        print(f'{deffender.name}の残り体力0')


def display_attck(name, attck):
    print(f'{name}は{attck}を発動！')


def display_damage(name, power):
    print(f'{name}は{power}のダメージ！')


def display_hp(name, hp):
    print(f'{name}の残り体力{hp}')


if __name__ == '__main__':
    naruto_justu = {"変化": 1, "影分身の術": 3, "うずまきナルト連弾": 4, "口寄せの術": 7, "螺旋丸": 8}
    sasuke_justu = {"業火球": 4, "鳳仙花": 3, "龍火": 3, "写輪眼": 3, "獅子連弾": 4, "千鳥": 8}
    ryuya_justu = {"パンチ": 2, "キック": 3, "天和": 20}
    sasuke = Player('サスケ', '下忍', sasuke_justu)
    naruto = Player('ナルト', '火影', naruto_justu)
