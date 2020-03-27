from vpython import canvas,arrow,vector,label,color,sphere,box,rate,rotate,mag,wtext,button
from math import pi,sin,cos,radians

class bloch_base:
    def __init__(self):
        self.scene  = canvas(title='Examples of Vector Rotations',width=500, height=500, center=vector(0,0,0), background=color.white)
        self.scene.camera.pos = vector(-2.48,1.31,5.28)
        self.scene.camera.axis = vector(2.48,-1.31,-5.28)
        self.cbut = button(text='Camera',color=color.black,pos = self.scene.caption_anchor, bind = self.cameraLeg )
     
    def SetupSpace(self):
        arrow(pos = vector(-2,0,0),axis=vector(1,0,0),length = 4,shaftwidth = 0.01,headwidth = 0.1, color = color.red)
        arrow(pos = vector(0,-2,0),axis=vector(0,1,0),length = 4,shaftwidth = 0.01,headwidth = 0.1, color = color.green)
        arrow(pos = vector(0,0,-2),axis=vector(0,0,1),length = 4,shaftwidth = 0.01,headwidth = 0.1, color = color.blue)
        #box(pos = vector(0,0,0),axis=vector(1,0,0),length = 10,width = 10,height = 0.01,opacity=0.1,color = color.red)
        #box(pos = vector(0,0,0),axis=vector(0,1,0),length = 10,width = 10,height = 0.01,opacity=0.1,color=color.green)
        #box(pos = vector(0,0,0),axis=vector(0,0,1),length =0.01,width = 10,height = 10,opacity=0.1,color=color.blue)
        label(pos=vector(0,2,0),text='|0>',height=20,color = color.black,box = False,opacity = 0,align = 'right')
        label(pos=vector(0,-2,0),text='|1>',height=20,color = color.black,box = False,opacity = 0,align = 'right')
        sphere(pos = vector(0,0,0),radius=1,color=color.yellow,opacity=0.2)
                
    def PlotforAngles(self,theta,phi):
        vec = self.angTovec(theta, phi)
        Varrow = arrow(pos = vector(0,0,0), axis = vector(0,0,0),length = 5,shaftwidth = 0.01,headwidth = 0.05,color = color.black)
        Varrow.axis.x = round(vec.x,2)
        Varrow.axis.y = round(vec.y,2)
        Varrow.axis.z = round(vec.z,2)
        self.legends(vec)
        
    def legends(self,vec):
        strM ="Magnitude : " + str(round(mag(vec),2))
        strC ="Coordinates : " + "({},{},{})".format(round(vec.x,2),round(vec.y,2),round(vec.z,2))
        wtext(text="\n")
        wtext(text = strM +"      "+ strC)
        label(pos=vec,text=str(vec),height=20,color = color.black,box = False,opacity = 0,align = 'right')
    
    def cameraLeg(self):
        CPos = str(self.scene.camera.pos)
        CAx  = str(self.scene.camera.axis)
        wtext(text="\n")
        wtext(text = CPos +"      "+ CAx)

    def angTovec(self,theta,phi):
        theta = radians(theta)
        phi =  radians(phi)
        a = (round(sin(theta)*cos(phi),2),round(sin(theta)*sin(phi),2),round(cos(theta),2))
        v1 = vector(a[0],a[1],a[2]) 
        return(v1)
        

bloch = bloch_base()
bloch.SetupSpace()
bloch.PlotforAngles(theta=30,phi=60)



        