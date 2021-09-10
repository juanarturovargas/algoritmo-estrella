from table import Table
from object.object import Object
from tree import Tree

class Star:
  ''' Aqui se encuentra el algoritmo estrella'''
  table = Table
  x_0 = int
  x_1 = int
  y_0 = int
  y_1 = int
  tree = Tree

  sPoint={"x":int,"y":int}
  fPoint={"x":int,"y":int}
  
  def __init__(self,table):
    self.table = table
    
    self.tree = Tree()

  def start(self):
    tree = self.tree
    table = self.table 
    root = table.table[self.sPoint["x"]][self.sPoint["y"]]
    tree.setRoot(root)
    ways = self.whereMoved(tree.root)
    
    #encuentra las posiciones del tablero para moverse
    print(ways)
    #un ejemplo de la nueva posicions que se puede agregar
    print(ways['up'].x, ways['up'].y)

    #a las nuevas posiciones es de evaluar la distancia manhata al punto final,
    #ordenar las distacias menoneros
    #colocar los nodos al arbol con addChild
    #continuar el proceso  whereMoved 

    #distance = self.calculateManhattanDistance(x_0,y_0,x_1,y_1)

  def whereMoved(self,node):
    ''' 
      Este metodo identifica el que movimientos pueden realizarse dentro de la posicion actual
    '''
    table = self.table
    x = node.object.x
    y = node.object.y
    _up = x -  1
    _down = x + 1
    _left = y - 1
    _right = y + 1

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

  def calculateManhattanDistance(self,x_0,y_0,x_1,y_1):
    return 0



  def setPointToStart(self,x,y):
    self.x_0 = x
    self.y_0 = y
    self.sPoint={"x":x,"y":y}

  def setPointToFinish(self,x,y):
    self.x_1 = x
    self.y_1 = y
    self.fPoint={"x":x,"y":y}