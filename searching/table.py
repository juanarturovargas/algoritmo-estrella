from object.object import Object

#Clase que define el contenedor por donde se movera el robot marcando los inventarios y los obstaculos
class Table:
  #height=altura del tablerero
  #weight=anchura del tablero
  #table= contiene el tablero con objetos, los objetos tienen la posicion del tablero´

  table = []
  objects = []
  countObjects = 0
  size={"x":int,"y":int}

  #constructor
  def __init__(self, weight,height):
    self.table = [[Object(x,y) for y in range(0, height) ] for x in range(0,weight )]
    self.size={"x":weight,"y":height}

  #Permite agregar un objeto al tablero
  def addObject(self,x,y,object):
    self.table[x][y].carry = object
    object.setPoint(x,y)
    self.countObjects += 1
    self.objects.append({id:self.countObjects, object:object})

  #Imprime el tablero
  def printTable(self):
    print('--->')
    print('Tamaño de la tabla: ',self.size)
    tableLength = len(self.table);
    tableHigth = len(self.table[0])
    print('-------------' * tableLength)
    for i in range(len(self.table)):
        row = ''
        for j in range(len(self.table[i])):
            obj = self.table[i][j]
            if obj.carry != None:
              row = row + '|' + obj.carry.name + '('+str(obj.getX())+','+str(obj.getY())+')'+'\t|'
            else:
              row = row + '|('+str(obj.getX())+','+str(obj.getY())+')'+'\t\t|'
        print(row)
        print('-------------'*tableLength)
        print()    

