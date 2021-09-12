from object.object import Object
class Obstacle (Object):
  def __init__(self,object=None):
    super().__init__()
    self.name = "obstacle"
    self.type = 2
    print(self.name)