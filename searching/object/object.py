#Clase que define un objeto, con sus tipos, nombre y posicion
class Object:
  carry = None
  name = str
  type = int
  x = 0
  y = 0

  #Constructore
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
  
  #Asigna la posicion en X
  def setX(self,x):
    self.x = x
  
  #Asigna la posicion en Y
  def setY(self,y):
    self.y = y

  #Asigna la posicion en X, y
  def setPoint(self,x,y):
    self.x = x
    self.y = y

  #Retorna las posiciones X, Y
  def getCurrentPoint(self):
    return self.x, self.y

  #Retorna la posicion en X
  def getX(self):
    return self.x
  
  #Retorna la posicion en Y
  def getY(self):
    return self.y