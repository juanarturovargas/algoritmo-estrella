from object.object import Object

#clase que identifica un inventario
class Package (Object):
  def __init__(self,object=None):
    super().__init__()
    self.name = "package"
    self.type = 3