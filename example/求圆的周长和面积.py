'''创建类求圆的面积：'''
import math
class Circle:
    def __init__(self,r):
        self._r=r

    def setR(self,r):
        self._r = r

    def Circle_C(self):
        C = 2*math.pi*r
        print('圆的周长为：',C)

    def Circle_S(self):
        S = math.pi*r**2
        print('圆的面积为',S)

if __name__=='__main__':
    r=float(input('请输入圆的半径r:'))
    circle=Circle(r)
    circle.Circle_C()
    circle.Circle_S()
    print('='*30)
