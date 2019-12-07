# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/30

import sys
from class_equipment import Equipment


class eq_mana(Equipment):

    restore_mamn_power=0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +魔法:%0.2f' % (self.restore_mana_power))
        print('-----------------')
        return


if __name__ == '__main__':
    eq=eq_mana()
    eq.show_me()
    eq.show_me_unique()
