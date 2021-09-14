from os import startfile
from table import Table
from object.obstacle import Obstacle
from object.package import Package
from object.forklift import Forklift
from star import Star
if __name__ == "__main__":

  #Inicialización de objetos  
  table = Table(4,4)
  package1 = Package()
  package2 = Package()
  package3 = Package()
  forklift = Forklift()

  #Carga de las posiciones y objetos(inventarios y obstaculos)
  table.addObject(0,0, package1)
  table.addObject(2,0, package2)
  table.addObject(0,3, package3)
  table.addObject(0,1, Obstacle())
  table.addObject(1,1, Obstacle())

  table.addObject(2,2, forklift)
  table.printTable()

  #Primer Problema, llegada al Primer Inventario
  print("Proceso de llegada al inventario M1")

  #Obtenemos la posición Inicial del Robot
  x_0, y_0 = forklift.getCurrentPoint()
  #Obtenemos la posición del inventario M1
  x_1, y_1 = package1.getCurrentPoint()

  #Inicializamos nuestra clase para realizar la operación del Algoritmo A*
  #Le indicamos los puntos iniciales y finales
  star = Star(table)
  star.setPointToStart(x_0,y_0)
  star.setPointToFinish(x_1,y_1)

  #Obtenemos la posicion final del Robot
  x_0, y_0 = star.start()

  #Imprimimos la lista abierta y cerrada del recorrido
  star.showCloseList()
  print("Recoger a inventario M1 en (", str(x_0), ",", str(y_0), ")")
  star.showOpenList()
  
  #Comenzamos el proceso de entrega, es similar a la llegada 
  print("------------------------------------")
  print("Proceso de entrega del inventario M1")
  x_1, y_1 = 3,3
  star2 = Star(table)
  star2.setPointToStart(x_0,y_0)
  star2.setPointToFinish(x_1,y_1)
  x_0, y_0 = star2.start()
  star2.showCloseList()
  print("Dejar inventario M1 en (", str(x_0), ",", str(y_0), ")")
   
  #-----------------------------------------------------------------------------------------------------------
  print("------------------------------------")
  print("Proceso de llegada al inventario M2")  
  x_1, y_1 = package2.getCurrentPoint()
  star3 = Star(table)
  star3.setPointToStart(x_0,y_0)
  star3.setPointToFinish(x_1,y_1)
  x_0, y_0 = star3.start()
  star3.showCloseList()
  print("Recoger a inventario M2 en (", str(x_0), ",", str(y_0), ")")

  print("------------------------------------")
  print("Proceso de entrega del inventario M2")  
  x_1, y_1 = 3,2
  star4 = Star(table)
  star4.setPointToStart(x_0,y_0)
  star4.setPointToFinish(x_1,y_1)
  x_0, y_0 = star4.start()
  star4.showCloseList()
  print("Dejar inventario M2 en (", str(x_0), ",", str(y_0), ")")
 
  #-----------------------------------------------------------------------------------------------------------
  print("------------------------------------")
  print("Proceso de llegada al inventario M3")  
  x_1, y_1 = package3.getCurrentPoint()
  star5 = Star(table)
  star5.setPointToStart(x_0,y_0)
  star5.setPointToFinish(x_1,y_1)
  x_0, y_0 = star5.start()
  star5.showCloseList()
  print("Recoger a inventario M3 en (", str(x_0), ",", str(y_0), ")")

  print("------------------------------------")
  print("Proceso de entrega del inventario M3")  
  x_1, y_1 = 3,1
  star6 = Star(table)
  star6.setPointToStart(x_0,y_0)
  star6.setPointToFinish(x_1,y_1)
  x_0, y_0 = star6.start() 
  star6.showCloseList()
  print("Dejar inventario M3 en (", str(x_0), ",", str(y_0), ")")
  
  star.showOpenList()
