from table import Table
from object.object import Object
from tree import Tree
from memory import Memory 

#Clase que realiza la ejecucion del algoritmo A*
class Star:

  #Definimos las propiedades
  table = Table
  tree = Tree
  memory = Memory
  openList = Memory
  openList2 = []

  sPoint={"x":int,"y":int}
  fPoint={"x":int,"y":int}
  currentPoint={"x":int,"y":int}

 #constructor que inicializa las propiedades
  def __init__(self,table):
    self.table = table    
    self.tree = Tree()
    self.memory = Memory(table.size["x"], table.size["y"])
    self.openList = Memory(table.size["x"], table.size["y"])
    self.g_value = 0

  #Ejecucion del algoritmo A*
  # obtenmos los nodos de toda la tabla y los recorremos para identificar donde se encuentra cada punto
  # Calculamos y obtenemos la distancia de Manhattan
  # agregamos cada nodo recorrido a la memoria para posteriormente imprimirlos
  # se realiza el analisis de los nodos para obtener el que posee la menor distancia
  # se retorna la posicion en la cual quedo el robot que sera utilizada por el siguiente problema como posicion inicial
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


  #Permite la impresion de la lista Cerrada
  def showCloseList(self):
    tree = self.tree
    tree.showTree(tree.root)

  #Permite la impresion de la lista abierta
  def showOpenList(self):
    f =  True
    for l in self.openList2:
      if f:
        f=False
        continue

      if l["name"] == "root":
        print("----------------------------------------")
        
      print( l["name"], " (",l["current"].x, ",", l["current"].y, ")")

  #Funcion que nos permite identificar cual de los nodos es el óptimo para que el robot se mueva
  def analysis(self, root):   
    text = "" 
    if self.isfound(root.object):
        self.tree.isFinish = True
        x = root.object["object"].x
        y = root.object["object"].y
        self.currentPoint={"x":x,"y":y}
        return True
    else:
        x = root.object["object"].x
        y = root.object["object"].y
    
    distances = self.getDistances(root.object["object"])

    for x in distances:      
      newNode = x
      self.tree.addChild(root,newNode) 
      if(self.tree.isFinish == False ):
        if(self.memory.possIsNone(newNode)):
          self.memory.add(newNode)
          _x = root.object["object"].x
          _y = root.object["object"].y
          found = self.analysis(newNode)
          return found
        continue
            
    return False
      

  #Funcion que nos permite identificar si el robot llego a la posicion objetivo
  def isfound(self,object):    
    if(object["manhata"] == 0):
      return True
    return False

  #Obtiene las distancias de las pociciones vecinas
  def getDistances(self,root):
    ways = self.whereMoved(root)
    self.openList2.append({"name":"root", "current":root})
    #encuentra las posiciones del tablero para moverse
    #print(ways)
    #un ejemplo de la nueva posicions que se puede agregar
    #print(ways['up'].x, ways['up'].y)

    #a las nuevas posiciones es de evaluar la distancia manhata al punto final,
    #ordenar las distacias menoneros
    #colocar los nodos al arbol con addChild
    #continuar el proceso  whereMoved
 
    distance = []
    distance.append(self.calculateManhattanDistance(ways['up'],self.fPoint, "up"))
    distance.append(self.calculateManhattanDistance(ways['right'],self.fPoint,"right"))
    distance.append(self.calculateManhattanDistance(ways['down'],self.fPoint,"down"))
    distance.append(self.calculateManhattanDistance(ways['left'],self.fPoint,"left"))

    distance.sort(key=lambda d:(d.object['manhata']is None, d.object['manhata']))
 
    return distance

  #Este metodo identifica el que movimientos pueden realizarse dentro de la posicion actual
  def whereMoved(self,node):
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

  #Identifica si hay un obstaculo en la posición marcada
  def existObstacule(self,x,y):
    table = self.table
    obstacule = table.table[x][y]
    if(obstacule.carry == None):
      return False
    
    if(obstacule.carry.name == "obstacle"):
      return True

    return False
    
  #Realiza el calculo de la distancia de Manhattan
  def calculateManhattanDistance(self, currentPoint, finalPoint, name=""):
    if(currentPoint == None ):
      distance =  self.tree.createNode({"manhata":None, "object":currentPoint,"name":name})
      self.openList.add(distance)
      return distance  
    
    x = abs(currentPoint.x - finalPoint["x"])
    y = abs(currentPoint.y - finalPoint["y"])
    h = x + y
    f = h + self.g_value
    self.openList2.append({"name":"   child", "current":currentPoint})
    distance = self.tree.createNode({"manhata":f, "object":currentPoint, "name":name})
    self.openList.add(distance)    
    return distance

  # MArca la posicion inicial
  def setPointToStart(self,x,y):
    self.x_0 = x
    self.y_0 = y
    self.sPoint={"x":x,"y":y}

  #Marca la posicion final
  def setPointToFinish(self,x,y):
    self.x_1 = x
    self.y_1 = y
    self.fPoint={"x":x,"y":y}