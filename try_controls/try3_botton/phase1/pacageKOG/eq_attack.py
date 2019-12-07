# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/23


from class_equipment import Equipment

class eq_attack(Equipment):
    critical_strike=0.0
    physical_suck=0.0


    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +暴击率:%0.2f' % (self.critical_strike))
        print('     +物理吸血:%0.2f' % (self.physical_suck))
        print('-----------------')
        return

if __name__ == '__main__':
    eq=eq_attack()
    eq.show_me()
    eq.show_me_unique()
