from object.object import Object

#Clase que identifica un obstaculo
class Obstacle (Object):
  def __init__(self,object=None):
    super().__init__()
    self.name = "obstacle"
    self.type = 2
    print(self.name)