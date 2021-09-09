from object.object import Object
class Package (Object):
  def __init__(self,object=None):
    super().__init__()
    self.name = "package"
    self.type = 3