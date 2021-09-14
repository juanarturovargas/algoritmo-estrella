from node import Node

#Permite el registro de los nodos recorridos
class Memory:
  countNode = 0
  memory = []
 
 #constructor
  def __init__(self,weight,height):
    self.memory = [[None for y in range(0, height) ] for x in range(0,weight )]

  def add(self,nodeTree):
    memory = self.memory
    if(nodeTree.object["object"]!= None):
      x = nodeTree.object["object"].x
      y = nodeTree.object["object"].y
      if(memory[x][y]==None):
        memory[x][y]= nodeTree
        return x,y
    return -1,-1

  #Verifica si el nodo es None
  def possIsNone(self,nodeTree):
    memory = self.memory
    if nodeTree.object["object"] == None:
      return False
    x = nodeTree.object["object"].x
    y = nodeTree.object["object"].y
    if(memory[x][y]==None):
      return True

    return False

  #Retorna el nodo, especificado
  def getNode(self, x, y):
    self.memory[x][y].isUse = True
    return self.memory[x][y]

  #Marca el nodo como en uso
  def isUsed(self,x,y):
    node = self.memory[x][y]
    return node.isUse 

  #Realiza la impresion de la lista contenida en la memoria
  def showMemory(self):
    for list in self.memory:
      for node in list:
          if node == None:
            continue
          else:
            print("(", node.object["object"].x ,",", node.object["object"].y, ")")

