from node import Node

class Tree:
  root = Node
  
  def __init__(self):
    pass
  
  def addChild(self,dad,child):
    dad.children.append(child)

  def setRoot(self,node):
    self.root = node

  def createNode(self,object):
    return Node(object)
