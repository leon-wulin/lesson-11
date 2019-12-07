# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/30

import sys
from class_equipment import Equipment


class eq_move(Equipment):



    def show_me_unique(self):
        print('-----独有加成-----')
        print('                 无')
        print('-----------------')
        return


if __name__ == '__main__':
    eq=eq_move()
    eq.show_me()
    eq.show_me_unique()
