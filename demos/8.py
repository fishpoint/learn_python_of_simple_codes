# -*- coding: utf-8 -*-
__author__ = "YuDian"
'''
    python中@property的应用。具体对property的解释：http://python.jobbole.com/81967/
'''
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, input_width):
        self._width = input_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, input_height):
        self._height = input_height

    @property
    def resolution(self):
        return str(self._height)+'*'+ str(self._width)

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)