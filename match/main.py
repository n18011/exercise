#!/usr/bin/python3
import Ninja_funcs


def main(player1, player2):
    print(f'{player1.name}の体力: {player1.set_hp()} クラス:{player1.job}')
    print(f'{player2.name}の体力: {player2.set_hp()} クラス:{player2.job}')

    turn = 1
    while True:
        input()
        if player1.hp >= 1 and player2.hp >= 1:
            print()
            print('Turn{}'.format(turn))
            print()
            Ninja_funcs.display_attck(player1.name, player1.attck())
            Ninja_funcs.display_damage(player2.name, player1.power)
            Ninja_funcs.diff_hp(player2, player1)
            Ninja_funcs.display_attck(player2.name, player2.attck())
            Ninja_funcs.display_damage(player1.name, player2.power)
            Ninja_funcs.diff_hp(player1, player2)
            turn += 1
        else:
            break

    print('Winner: {}'.format(player1.name if player1.hp > player2.hp else player2.name))


if __name__ == '__main__':
    naruto_justu = {"変化の術": 1, "影分身の術": 3, "うずまきナルト連弾": 4, "口寄せの術": 7, "螺旋丸": 8}
    sasuke_justu = {"業火球の術": 4, "鳳仙花の術": 3, "龍火の術": 3, "写輪眼": 3, "獅子連弾": 4, "千鳥": 8}
    ryuya_justu = {"パンチ": 2, "キック": 3, "役満！天和！！": 20}
    sasuke = Ninja_funcs.Player('サスケ', '下忍', sasuke_justu)
    naruto = Ninja_funcs.Player('ナルト', '火影', naruto_justu)
    ryuya = Ninja_funcs.Player('りゅーや', '人', ryuya_justu)

    main(ryuya, naruto)
