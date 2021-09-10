class Object:
  carry = None
  name = str
  type = int
  x = 0
  y = 0

  def __init__(self,object=None):
    self.carry = object
    self.name = "Object"
    self.type = 0

  def __init__(self,x=0, y=0):
    self.carry = None
    self.name = "Object"
    self.type = 0
    self.x = x
    self.y = y
  
  def setX(self,x):
    self.x = x
  
  def setY(self,y):
    self.y = y

  def setPoint(self,x,y):
    self.x = x
    self.y = y

  def getCurrentPoint(self):
    return self.x, self.y

  def getX(self):
    return self.x
  
  def getY(self):
    return self.y