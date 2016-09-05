# CMPS 101
# HW7
# Andres Segundo
# Tarum Fraz

import copy
import collections
import heapq
import time
import os


class Graph(object):
    # Initializing empty graph
    def __init__(self):
        self.adj_list = dict()    # Initial adjacency list is empty dictionary
        self.vertices = set()    # Vertices are stored in a set
        self.degrees = dict()    # Degrees stored as dictionary

    # Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
    def isEdge(self,node1,node2):
        if node1 in self.vertices:        # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1            # Edge is present!

        if node2 in self.vertices:        # Check if node2 is vertex
            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2
                return 1            # Edge is present!

        return 0                # Edge not present!

    # Add undirected, simple edge (node1, node2)
    def addEdge(self,node1,node2):

        # print('Called')
        if node1 == node2:            # Self loop, so do nothing
            # print('self loop')
            return
        if node1 in self.vertices:        # Check if node1 is vertex
            nbrs = self.adj_list[node1]        # nbrs is neighbor list of node1
            if node2 not in nbrs:         # Check if node2 already neighbor of node1
                nbrs.add(node2)            # Add node2 to this list
                self.degrees[node1] = self.degrees[node1]+1    # Increment degree of node1

        else:                    # So node1 is not vertex
            self.vertices.add(node1)        # Add node1 to vertices
            self.adj_list[node1] = {node2}    # Initialize node1's list to have node2
            self.degrees[node1] = 1         # Set degree of node1 to be 1

        if node2 in self.vertices:        # Check if node2 is vertex
            nbrs = self.adj_list[node2]        # nbrs is neighbor list of node2
            if node1 not in nbrs:         # Check if node1 already neighbor of node2
                nbrs.add(node1)            # Add node1 to this list
                self.degrees[node2] = self.degrees[node2]+1    # Increment degree of node2

        else:                    # So node2 is not vertex
            self.vertices.add(node2)        # Add node2 to vertices
            self.adj_list[node2] = {node1}    # Initialize node2's list to have node1
            self.degrees[node2] = 1         # Set degree of node2 to be 1

    # Give the size of the graph. Outputs [vertices edges wedges]
    #
    def size(self):
        n = len(self.vertices)            # Number of vertices

        m = 0                    # Initialize edges/wedges = 0
        wedge = 0
        for node in self.vertices:        # Loop over nodes
            deg = self.degrees[node]      # Get degree of node
            m = m + deg             # Add degree to current edge count
            wedge = wedge+deg*(deg-1)/2        # Add wedges centered at node to wedge count
        return [n, m, wedge]            # Return size info

    # Print the graph
    def output(self,fname,dirname):
        os.chdir(dirname)
        f_output = open(fname,'w')

        for node1 in list(self.adj_list.keys()):
            f_output.write(str(node1)+': ')
            for node2 in (self.adj_list)[node1]:
                f_output.write(str(node2)+' ')
            f_output.write('\n')
        f_output.write('------------------\n')
        f_output.close()

        
    def path(self, start, end):

        visit = collections.deque() # A queue to collect the nodes in graph we have visited
        queue = collections.deque() # originial queue to place all of the nodes
        queue.append([start]) # Add the source to the queue
    
        while queue:         
            path = queue.popleft() # First path in the txt file
            node = path[-1] # We want to extract the last node in the path
            if node == end: # If we have reached the end of it
                return list(path) # Add it to the list
            elif node not in visit: # if the node is not in the queue of visited nodes
                for currNode in self.adj_list.get(node, []):
                    path2 = collections.deque(path) # Create  NEW  path
                    path2.append(currNode) # Add the current node to it
                    queue.append(list(path2)) # Append it with the lsit
                visit.append(node) # Put the node in the visited list
            
            
    def levels(self, start):
        visit, q = collections.deque(), set([start]) # Make 2 queues, one for initial and one for visited
        lev = [0, 0, 0, 0, 0, 0, 0] # Initial array of all of the levels we have visited
        count = 0 # We will use a counter to count the nodes at each level
       
        while q: # While the queue is not empty
            nextLev=set()  # Create a new empty set for the next level
            for node in q - set(visit): # for all of the nodes that are in the set
                lev[count] = lev[count] + 1 # keep adding at each level
                visit.append(node) # Add to the visited node so we know we have been there
                nextLev = nextLev | set(self.adj_list.get(node, [])) - set(visit) # Go to the next level
            q = nextLev # We need the queue for the bext level
            count = count + 1 # Iterate the counter

        return lev # Return all of the levels 
        