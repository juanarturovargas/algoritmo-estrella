from node import Node

class Tree:
  root = Node
  
  def __init__(self):
    pass
  
  def addChild(self,dad,child):
    dad.children.append(child)

  def setRoot(self,node):
    self.root = Node(node) 