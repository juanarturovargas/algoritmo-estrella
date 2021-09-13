from node import Node

class Tree:
  root = Node
  countNode = 0
  isFinish = False
  
  def __init__(self):
    pass
  
  def addChild(self,dad,child):
    dad.children.append(child)

  def setRoot(self,node):
    self.root = node

  def createNode(self,object):
    self.countNode = self.countNode + 1
    return Node(object,self.countNode)

  def showTree(self,root):
    length = len(root.children)
    
    if(length<0):
      return ""
    for x in root.children:
      print(str(root.id)+root.object["name"]+"->"+str(x.id)+x.object["name"])
      self.showTree(x)
    print(str(root.id)+root.object["name"])