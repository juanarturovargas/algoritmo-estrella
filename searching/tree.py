from node import Node

#Clase arbol que permite registrar los nodos de busqueda
class Tree:
  root = Node
  countNode = 0
  isFinish = False
  
  #Constructor
  def __init__(self):
    pass
  
  #Permite agregar un nodo hijo
  def addChild(self,dad,child):
    dad.children.append(child)

  #Marca un nodo como padre
  def setRoot(self,node):
    self.root = node

  #Permite crear un nuevo nodo
  def createNode(self,object):
    self.countNode = self.countNode + 1
    return Node(object,self.countNode)

  #Realiza la impresion del arbol 
  def showTree(self,root):
    length = len(root.children)
    
    if(length<0):
      return ""
    for x in root.children:
      if(x.object["object"]== None):
        continue
      print(
         " Mover robot desde " +'('+
        str(root.object["object"].x)+", "+
        str(root.object["object"].y)+')'
        " hacia"+
        '('+
        str(x.object["object"].x)+", "+
        str(x.object["object"].y)+')'
      )        
    
      self.showTree(x)
    