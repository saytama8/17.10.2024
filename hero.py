class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel("skater_guy.egg")
        self.hero.setTexture(loader.loadTexture("M0CM0.tif"))
       
        #self.hero.setColor(1,0.5,0)
        self.hero.setScale(0.03)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
    def cameraBind(self):
        
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos( -pos[0], -pos[1], -pos[2] -3 )
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
