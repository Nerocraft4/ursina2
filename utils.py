from ursina import *
from math import atan2
from agent import Agent
from copy import deepcopy

def generateMap(n, top_point, bot_point):
    for i in range(n):
        #c = Entity(model='sphere', position=top_point, color=color.blue, scale=0.5)
        #generar punt superior aleatori
        t_newx=6+2*random.random()-1 #ens movem cap a la dreta
        t_newy=(5-top_point.y)*random.random()-2 #ens movem cap a dalt o a baix
        t_angle=atan2(t_newy,t_newx)/(6.2830)*360 #angle d'inclinacio, pel rectangle
        t_midpoint = Vec2(t_newx+2*top_point.x,t_newy+2*top_point.y)
        t_size=sqrt(t_newx*t_newx+t_newy*t_newy) #mòdul
        w1 = Entity(model='cube', texture= 'mytexture', collider='box', position=t_midpoint/2, rotation_z=-t_angle, scale=(t_size,1,0.5), eternal=False)
        top_point=Vec2(t_newx+top_point.x,t_newy+top_point.y)#reassignem el top_point

        #generar punt inferior, relacionat amb el superior
        b_newx=t_newx
        b_newy=top_point.y-bot_point.y-4*random.random()-1.5
        b_angle=atan2(b_newy,b_newx)/(6.2830)*360 #angle d'inclinacio, pel rectangle
        b_midpoint = Vec2(b_newx+2*bot_point.x,b_newy+2*bot_point.y)
        b_size=sqrt(b_newx*b_newx+b_newy*b_newy) #mòdul
        w2 = Entity(model='cube', texture= 'mytexture', collider='box', position=b_midpoint/2, rotation_z=-b_angle, scale=(b_size,1,0.5),eternal=False)
        bot_point=Vec2(b_newx+bot_point.x,b_newy+bot_point.y)#reassignem el bot_point

    return top_point, bot_point

def generateAgents(bgen):
    enti=Sprite('asset1demo.png', scale=2)
    enti.x = -8 + 0.7*(random.random()-0.35)
    enti.y = 1*(random.random()-0.55)
    enti.collider = 'box'
    enti.color=color.yellow
    enti.rotation_z = 90
    agent = Agent(enti,mutate(bgen))
    agent.setGenome()
    #animal.setrepro(initial_genome)
    #animal.setpos([-2,-2])
    return agent


def mutate(genome):
    newGenome = deepcopy(genome)
    for i in range(len(newGenome)):
        newGenome[i]+=random.random()*0.01-0.005
        newGenome[i]=round(newGenome[i],4)
    return newGenome
