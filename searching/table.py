from object.object import Object

class Table:

  '''
  height=altura del tablerero
  weight=anchura del tablero
  '''
  table = []
  objects = []
  countObjects = 0

  def __init__(self,height, weight):
    self.table = [[Object for _ in range(0, weight) ] for _ in range(0, height)]

  def addObject(self,x,y,object):
    self.table[x][y].carry = object
    object.setPoint(x,y)
    self.countObjects += 1
    self.objects.append({id:self.countObjects, object:object})

  def getNameObject(self,x,y):
    if (self.table[x][y].carry == None):
      return "no Object"
    
    return self.table[x][y].carry.name

  def getNameObject(self,x,y):
    if (self.table[x][y].carry == None):
      return -1
    
    return self.table[x][y].carry.type

    

