# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/23


from pacageKOG.hero import Hero
from eq_attack import eq_attack
from eq_defense import eq_defense
from eq_mana import eq_mana
from eq_move import eq_move
cjsh=Hero('苍狼末裔','成吉思汗','射手ARCHER')

print(cjsh.name)
print(cjsh.position)
print(cjsh.ab_difficulity)

cjsh.ab_difficulity=999
print(cjsh.ab_difficulity)



if __name__ == '__main__':
    eq=eq_attack()
    eq.show_me()
    eq.show_me_unique()

if __name__ == '__main__':
    eq=eq_defense()
    eq.show_me()
    eq.show_me_unique()

if __name__ == '__main__':
    eq=eq_move()
    eq.show_me()
    eq.show_me_unique()

if __name__ == '__main__':
    eq=eq_mana()
    eq.show_me()
    eq.show_me_unique()
