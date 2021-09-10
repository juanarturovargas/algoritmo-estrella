from object.object import Object

class Table:

  '''
  height=altura del tablerero
  weight=anchura del tablero
  table= contiene el tablero con objetos, los objetos tienen la posicion del tablero

  '''
  table = []
  objects = []
  countObjects = 0
  size={"x":int,"y":int}
  def __init__(self,height, weight):
    self.table = [[Object(x,y) for x in range(0, weight) ] for y in range(0, height)]
    self.size={"x":height,"y":weight}

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

    

