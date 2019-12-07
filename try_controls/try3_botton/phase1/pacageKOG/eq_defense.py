# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/30

import sys
from class_equipment import Equipment


class eq_defense(Equipment):

    restore_life_force=0.0

    def show_me_unique(self):
        print('----------独有加成-------------')
        print('          +回血:%0.2f'%(self.restore_life_force))
        print('------------------------------')
        return


if __name__ == '__main__':
    eq=eq_defense()
    eq.show_me()
    eq.show_me_unique()
