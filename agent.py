from ursina import *
from copy import deepcopy

def softmax(z):
    z_exp = [math.exp(i) for i in z]
    softmax = [round((i / sum(z_exp)), 4) for i in z_exp]
    return softmax

class Agent():
    def __init__(self,base,genome):
        self.genome = genome
        self.alive = 1
        #base skin (hardcoded)
        self.body = base
        #currently useless

    def setGenome(self):
        # self.genome = softmax(self.genome)#normalize
        self.ry=self.genome[0] #right eye
        self.ly=self.genome[1] #left eye
        self.sp=self.genome[2] #speed
        self.sz=self.genome[3] #size

    def getGenome(self):
        return self.genome

    def update(self):
        if(self.alive==1):
            s = self.body
            hit_left = raycast(s.position , direction=s.left+s.up, ignore=(s,), distance=1*self.sz, debug=False)
            if hit_left.hit and hit_left.entity.name!="sprite":
                s.rotation_z += 36*random.random()*(self.ly-0.10)
            hit_right = raycast(s.position , direction=s.right+s.up, ignore=(s,), distance=1*self.sz, debug=False)
            if hit_right.hit and hit_right.entity.name!="sprite":
                s.rotation_z -= 36*random.random()*(self.ry-0.10)
            hit_front = raycast(s.position , direction=s.up, ignore=(s,), distance=5*self.sz, debug=True)
            if hit_front.hit and hit_front.entity.name!="sprite":
                s.position += s.up*time.dt*30*self.sp
            else:
                s.position += s.up*time.dt*60*self.sp

            hit_info = s.intersects()
            if hit_info.hit and hit_info.entity.name!="sprite":
                self.alive=0
