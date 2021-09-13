
from node import Node

class Memory:
  
  countNode = 0
  memory = []

  
  def __init__(self,weight,height):
    self.memory = [[None for y in range(0, height) ] for x in range(0,weight )]

  def add(self,nodeTree):
    memory = self.memory
    if(nodeTree.object["object"]!= None):
      x = nodeTree.object["object"].x
      y = nodeTree.object["object"].y
      memory[x][y]= nodeTree
      return x,y
    return -1,-1

  def possIsNone(self,nodeTree):
    memory = self.memory
    x = nodeTree.object["object"].x
    y = nodeTree.object["object"].y
    if(memory[x][y]==None):
      return True

    return False

  def showMemory(self):
    pass

