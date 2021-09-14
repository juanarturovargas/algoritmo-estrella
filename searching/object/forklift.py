from object.object import Object

#Clase que define el robot
class Forklift (Object):
  def __init__(self,object=None):
    super().__init__()
    self.name = "Forklift"
    self.type = 1