# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/23

import random

class Hero():
    '''
    skin='英雄的原始皮肤'
    name='英雄的姓名'
    position='英雄的定位'
'''

    ab_viability=0
    ab_damage=0
    ab_effect=0
    ab_difficulity=0

    def __init__(self,s,n,p):
        '初始化英雄'
        self.skin=s
        self.__name=n
        self.__position=p

        self.ab_viability=random.randint(1,100)
        self.ab_damage=random.randint(1,100)
        self.ab_effect=random.randint(1,100)
        self.ab_difficulity=random.randint(1,100)
        return

    @property
    def name(self__name):
            return self__name

    @property
    def position(self__position):
            return self__position
