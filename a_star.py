import math
import dists as cities

auxStart = ''

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
   if start not in cities.dists.keys():
       print('Essa cidade não existe')
       return
   nodes = cities.dists[start]
   global auxStart
   if auxStart.__eq__(''):
      auxStart = start
   nodeList = {}
   for n in nodes:
       cityName = n[0]
       if cityName.__eq__(auxStart):
           continue
       cityDist = n[1]
       distance = cities.straight_line_dists_from_bucharest[cityName]
       total = cityDist + distance
       nodeList[cityName] = total
   minNodecityName = min(nodeList.keys(), key=lambda k: nodeList[k]) 
   print(minNodecityName)
   if minNodecityName.__eq__(goal) or auxStart.__eq__(goal):
       return
   a_star(minNodecityName)

cityName = input('Digite o nome da cidade para chegar em Bucharest: ')
   
a_star(cityName)
