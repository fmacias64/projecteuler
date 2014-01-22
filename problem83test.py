# euler 82
# grid is a dictionary with key as tuple (i,j) and value as value of node
# i is row, j is column of grid

import time
t0 = time.time()

f = open('matrix.txt', 'r')
grid = {}
counter = 1
for line in f:
   temp = line.replace('\n','')
   temp = temp.split(',')
   for a in range(len(temp)):
       grid[(counter,a+1)] = int(temp[a])
   counter += 1
rows = 80
cols = 80

def findNeighbors(vertex):
   i, j = vertex[0], vertex[1]
   output = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]  # all neighbors
   remove = []
   for v in output:
      if v[0] < 1 or v[0] > rows or v[1] < 1 or v[1] > cols:  
         remove.append(v)
   final = [x for x in output if not x in remove]
   return final
      
# Let's implement Dijkstra's algo from Wikipedia
def dka(graph, source):    # graph will be our grid, source will be (1,1)
   dist = {}
   for v in graph:
      dist[v] = float("inf")#assign infinite value to each
   dist[source] = graph[source]
   Q = dist.copy()   #make a copy of graph, as a hash
   length = len(Q)
   while length > 0:
      u = min(Q, key=Q.get) #get the min value of Q
      if dist[u] == float("inf"):
         break
      if u == (rows, cols):
         break
      del Q[u]
      length -= 1
      n = findNeighbors((u))
      neighbors = [x for x in n if x in Q]
      for v in neighbors:
         alt = dist[u] + grid[v]
         if alt < dist[v]:
            dist[v] = alt
            Q[v] = alt
   return dist

vertex=(1,1)
dist = {}
for v in grid:
   dist[v] = float("inf")
dist[vertex] = grid[vertex]
Q = dist.copy()
u = min(Q, key=Q.get)
print u
print Q.get(u)