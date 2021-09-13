from table import Table
from object.object import Object
from tree import Tree
from memory import Memory 

class Star:
  ''' Aqui se encuentra el algoritmo estrella'''
  table = Table
  tree = Tree
  memory = Memory
  openList = Memory

  sPoint={"x":int,"y":int}
  fPoint={"x":int,"y":int}
  currentPoint={"x":int,"y":int}
  def __init__(self,table):
    self.table = table
    
    self.tree = Tree()
    self.memory = Memory(table.size["x"], table.size["y"])
    self.openList = Memory(table.size["x"], table.size["y"])
  def start(self):

    tree = self.tree
    table = self.table 
    init = table.table[self.sPoint["x"]][self.sPoint["y"]]
    memory = self.memory
  
    s = self.calculateManhattanDistance(init,self.fPoint,"start node")
    tree.setRoot(s)
    memory.add(s)
    self.analysis(tree.root)
    return self.currentPoint['x'],self.currentPoint['y']


  def showCloseList(self):
    tree = self.tree
    tree.showTree(tree.root)

  def showOpenList(self):
    openList = self.openList
    openList.showMemory()

  
  def analysis(self, root):
    
    if self.isfound(root.object):
       
        self.tree.isFinish = True
        x = root.object["object"].x
        y = root.object["object"].y
        self.currentPoint={"x":x,"y":y}
        print("found",x,y)
        return True
    else:
        x = root.object["object"].x
        y = root.object["object"].y
        print("continue",x,y)
    
    distances = self.getDistances(root.object["object"])

    for x in distances:
      
      newNode = x
      self.tree.addChild(root,newNode)
      
      
      if(self.tree.isFinish == False ):
        if(self.memory.possIsNone(newNode)):
          self.memory.add(newNode)
          _x = root.object["object"].x
          _y = root.object["object"].y
          print("padre",_x,_y)
          found = self.analysis(newNode)
          return found
        continue
            
    return False
      

  def isfound(self,object):
    
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
    distance.append(self.calculateManhattanDistance(ways['left'],self.fPoint,"left"))
    distance.append(self.calculateManhattanDistance(ways['down'],self.fPoint,"down"))
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
    if(_up != -1 and not self.existObstacule(x,_up)):
      up = table.table[x][_up]
    if(_down != table.size["y"] and not self.existObstacule(x,_down)):
      down = table.table[x][_down]
    if(_left != -1 and not self.existObstacule(_left,y)):
      left = table.table[_left][y]
    if(_right != table.size["x"] and not self.existObstacule(_right,y)):
      right = table.table[_right][y]

    return {"up": up, "down": down, "left": left, "right":right}

  def existObstacule(self,x,y):
    table = self.table
    obstacule = table.table[x][y]
    if(obstacule.carry == None):
      return False
    
    if(obstacule.carry.name == "obstacle"):
      return True

    return False
    
  def calculateManhattanDistance(self, currentPoint, finalPoint, name=""):

    if(currentPoint == None ):
      distance =  self.tree.createNode({"manhata":None, "object":currentPoint,"name":name})
      self.openList.add(distance)
      return distance  
    
    x = abs(currentPoint.x - finalPoint["x"])
    y = abs(currentPoint.y - finalPoint["y"])
    h = x+y
    distance = self.tree.createNode({"manhata":h, "object":currentPoint, "name":name})
    self.openList.add(distance)
    return distance


  def setPointToStart(self,x,y):
    self.x_0 = x
    self.y_0 = y
    self.sPoint={"x":x,"y":y}

  def setPointToFinish(self,x,y):
    self.x_1 = x
    self.y_1 = y
    self.fPoint={"x":x,"y":y}