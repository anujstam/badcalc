import pygame
from pygame.locals import *
import sys
import random
import math
import sys

##deg=int(raw_input('enter degree : '))
##l=[]
##for i in range(deg+1):
##    print 'coef of degree ',i
##    l=l+[float(raw_input(''))]
##
###print l
##def fn(l,x):
##    y=0
##    #print l
##    for i in range(0,len(l)):
##         y=y+(x**i)*l[i]
##    return y
##
##m=fn(l,500)
##min=math.fabs(350/fn(l,-500))
def not_diverge(c):
    a= c
    for i in range(255):
        try:
            a = a**2+c
        except OverflowError or MemoryError:
            return False,0

        if str(a) =="(nan+nanj)":

            return False,i
    return True,255
    
        

screen = pygame.display.set_mode((1000,700))

for x in range(-200,100):
    for y in range(-150,150):
        c = complex(x*0.01,y*0.01)
        bl,val =not_diverge(c)
        if bl:
            pygame.draw.line(screen,(255,255, 0),(500+x+.1,350+y+.1),(500+x,350+y),1)
        else:
            alpha = val
            pygame.draw.line(screen,(alpha,alpha,0),(500+x+.1,350+y+.1),(500+x,350+y),1)

    pygame.display.update()
        



    
##    y=fn(l,x)
##    ##y=y*min
##    print x,y
##    pygame.draw.line(screen,(255,0,255),(500+prevx,-350+700-prevy),(500+x,-350+700-y),1)
##    pygame.draw.line(screen,(c1,c2,c3),(1000,700),(500+x,-350+700-y),1)
##    prevy=y
##    prevx=x
##    x=x+1
##    pygame.display.update()
    

