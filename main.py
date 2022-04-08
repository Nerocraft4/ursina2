from ursina import *
import random
from utils import generateMap, generateAgents, mutate
from agent import Agent, softmax
#from copy import copy,deepcopy

app = Ursina()
window.color = color.black
N=4

agents=[]
bgen = [round(random.random(), 4) for i in range(4)]
bgen = softmax(bgen)
for i in range(N):
    agents.append(generateAgents(bgen))

Entity(model='cube', collider='mesh', texture='mytexture', position=(-9,0), scale=(1,4,0.5), eternal=True)
Entity(model='cube', collider='mesh', texture='mytexture', position=(-6,2), scale=(6,1,0.5), eternal=True)
Entity(model='cube', collider='mesh', texture='mytexture', position=(-6,-2), scale=(6,1,0.5), eternal=True)

global top_point
global bot_point
top_point = Vec2(-3, 2)
bot_point = Vec2(-3,-2)
top_point, bot_point = generateMap(20, top_point, bot_point)
posi = (top_point+bot_point)/2
Entity(model='sphere', position=posi, color=color.blue)

camera.position = (-4,0,-30)
camera.rotation_y = 45
camera.rotation_z = 90

txt1 = Text(text=str(len(agents)), scale=2,x=-0.85,y=0.45, eternal=True)
txt2 = Text(text=str(bgen), scale=2,x=-0.85,y=0.4, eternal=True)
txt3 = Text(text=str("High score: "+str(0)), scale=2,x=-0.85,y=0.35, eternal=True)
txt4 = Text(text="Generation: 1", scale=2,x=-0.85,y=0.3, eternal=True)

global generation
generation = 0
global highscore
highscore = 0

def update():
    global generation, highscore
    if 'bestagent' not in locals():
        if generation == 0:
            bestagent=agents[0]
            generation+=1
            print("generation: ",generation)

    if len(agents)>1:
        bestagent=agents[0]
        mytext  = "Agents left: " + str(len(agents))
        txt1.text = mytext
        mytext3 = round((highscore),3)
        txt3.text = str("High score: "+str(mytext3))
        for agent in agents:
            if agent.alive!=1:
                agents.remove(agent)
            if agent.body.x+8>highscore:
                highscore=agent.body.x+8
            agent.update()
        camera.position = bestagent.body.position+(-16,0,-15)
        #camera.position = bestagent.body.position+(0,0,-25)
    else:
        generation+=1
        txt4.text = str("Generation: "+str(generation))
        scene.clear()
        top_point, bot_point = generateMap(20, Vec2(-3, 2), Vec2(-3, -2))
        newGenome=mutate(agents[0].getGenome())
        txt2.text = str(newGenome)
        for i in range(N):
            agents.append(generateAgents(newGenome))
        bestagent=agents[0]
        agents.remove(bestagent)
        bestagent=agents[0]


def input(key):
    pass

app.run()
