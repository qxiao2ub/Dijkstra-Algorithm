#1st chunk : vertex

import sys; #following use max function

#define vertex
class Vertex(object):
  
  def __init__(self, name):#build with vertex name
    self.name = name;
    self.visited = False;
    self.predecessor = None;
    self.adjacentciesList = [];#vertex adjacent edges
    self.minDistance = sys.maxsize; #above import sys, to use max function, this first initialize shortest distance to infinity
    
  #def __cmp__(self, otherVertex): #define comparator
   # return self.cmp(self.minDistance, otherVertex.minDistance);
    
  def __lt__(self, other): #less than operation
    selfPriority = self.minDistance;
    otherPriority = other.minDistance;
    return selfPriority < otherPriority;
  
#2nd chunk: edge
  
class Edge(object):
  
  def __init__(self, weight, startVertex, targetVertex):
    self.weight = weight;
    self.startVertex = startVertex;
    self.targetVertex = targetVertex;

#3rd chunk: algorithm

import heapq; #find priority in queue

class Algorithm(object):

  def calculateShortestPath(self, vertexList, startVertex):
    
    queue = [];
    startVertex.minDistance = 0;#starting point distance is 0
    heapq.heappush(queue, startVertex);#pushing startVertex to heap
    
    while len(queue)>0:
      
      actualVertex = heapq.heappop(queue);
      
      for edge in actualVertex.adjacentciesList:
        u = edge.startVertex;
        v = edge.targetVertex;
        newDistance = u.minDistance + edge.weight;
        
        if newDistance < v.minDistance:
          v.predecessor = u;
          v.minDistance = newDistance;
          heapq.heappush(queue, v);
          
  def getShortestPathTo(self, targetVertex):
    
    print("Shortest path to target is: ", targetVertex.minDistance);
    
    node = targetVertex;
    
    while node is not None:
      print("%s -> " % node.name);
      node = node.predecessor;
    
#4th chunk: application
  
node1 = Vertex("r");
node2 = Vertex("a");
node3 = Vertex("p");
node4 = Vertex("q");
node5 = Vertex("b");
  
edge1 = Edge(2, node1, node2);          
edge2 = Edge(1, node2, node3);          
edge3 = Edge(6, node3, node4);
edge4 = Edge(2, node5, node4);          
edge5 = Edge(4, node1, node5);          
edge6 = Edge(3, node2, node5);          
edge7 = Edge(-3, node4, node2);          
edge8 = Edge(2, node3, node5);

node1.adjacentciesList.append(edge1);
node1.adjacentciesList.append(edge5);
node2.adjacentciesList.append(edge2);
node2.adjacentciesList.append(edge6);
node3.adjacentciesList.append(edge3);
node3.adjacentciesList.append(edge8);
node4.adjacentciesList.append(edge7);
node5.adjacentciesList.append(edge4);

vertexList = [node1, node2, node3, node4, node5];
edgeList = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8];

algorithm = Algorithm();
algorithm.calculateShortestPath(vertexList, node1); #r is starting vertex
algorithm.getShortestPathTo(node4);#here we give example to end q