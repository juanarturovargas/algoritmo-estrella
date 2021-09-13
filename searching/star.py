from table import Table
from object.object import Object
from tree import Tree
from memory import Memory 

class Star:
  ''' Aqui se encuentra el algoritmo estrella'''
  table = Table
  tree = Tree
  memory = Memory

  sPoint={"x":int,"y":int}
  fPoint={"x":int,"y":int}
  
  def __init__(self,table):
    self.table = table
    
    self.tree = Tree()
    self.memory = Memory(table.size["x"], table.size["y"])

  def start(self):

    tree = self.tree
    table = self.table 
    init = table.table[self.sPoint["x"]][self.sPoint["y"]]
    memory = self.memory
  
    s = self.calculateManhattanDistance(init,self.fPoint,"start node")
    tree.setRoot(s)
    memory.add(s)
    self.analysis(tree.root)
    tree.showTree(tree.root)
    
  def analysis(self, root):
    
    if self.isfound(root.object):
        print("found")
        self.tree.isFinish = True
        return True
    else:
        print("continue")
    
    distances = self.getDistances(root.object["object"])

    for x in distances:
      newNode = x
      self.tree.addChild(root,newNode)
      self.memory.add(newNode)
      
      if(self.tree.isFinish == False ):
        if(self.memory.possIsNone):
          self.analysis(newNode)
            
    return False
      

  def isfound(self,object):
    print(object["name"])
    if(object["manhata"] == 0):
      return True
    return False

  def getDistances(self,root):
    ways = self.whereMoved(root)
    
    #encuentra las posiciones del tablero para moverse
    #print(ways)
    #un ejemplo de la nueva posicions que se puede agregar
    #print(ways['up'].x, ways['up'].y)

    #a las nuevas posiciones es de evaluar la distancia manhata al punto final,
    #ordenar las distacias menoneros
    #colocar los nodos al arbol con addChild
    #continuar el proceso  whereMoved
    #  
    distance = []
    distance.append(self.calculateManhattanDistance(ways['up'],self.fPoint, "up"))
    distance.append(self.calculateManhattanDistance(ways['down'],self.fPoint,"down"))
    distance.append(self.calculateManhattanDistance(ways['left'],self.fPoint,"left"))
    distance.append(self.calculateManhattanDistance(ways['right'],self.fPoint,"right"))

    distance.sort(key=lambda d:(d.object['manhata']is None, d.object['manhata']))

    return distance
    #

  def whereMoved(self,node):
    ''' 
      Este metodo identifica el que movimientos pueden realizarse dentro de la posicion actual
    '''
    table = self.table
    x = node.x
    y = node.y
    _up = y -  1
    _down = y + 1
    _left = x - 1
    _right = x + 1

    up = None
    down = None
    left = None
    right = None
    # se debe evaluar si en la posicion donde se movió existe un obstaculo con table.table[x][y].carry si es == none es porque no existe nada
    if(_up != -1 ):
      up = table.table[x][_up]
    if(_down != table.size["y"] ):
      down = table.table[x][_down]
    if(_left != -1 ):
      left = table.table[_left][y]
    if(_right != table.size["x"]):
      right = table.table[_right][y]

    return {"up": up, "down": down, "left": left, "right":right}

  def calculateManhattanDistance(self, currentPoint, finalPoint, name=""):

    if(currentPoint == None ):
      distance =  self.tree.createNode({"manhata":None, "object":currentPoint,"name":name})
      return distance  
    
    x = abs(currentPoint.x - finalPoint["x"])
    y = abs(currentPoint.y - finalPoint["y"])
    h = x+y
    distance = self.tree.createNode({"manhata":h, "object":currentPoint, "name":name})
    
    return distance


  def setPointToStart(self,x,y):
    self.x_0 = x
    self.y_0 = y
    self.sPoint={"x":x,"y":y}

  def setPointToFinish(self,x,y):
    self.x_1 = x
    self.y_1 = y
    self.fPoint={"x":x,"y":y}