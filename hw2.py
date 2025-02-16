#! /usr/bin/env python3

#from hw2.search import *
from search import *

# ********************************************************
# CS 370 HW #2  DUE Thursday, 2/13/2025 at 11:59 pm
#                via gradescope

# ********************************************************
# Name: Rafia Mobashira
# Email address: rafia.mobashira@yale.edu
# ********************************************************

# This file may be opened in python 3

# ********************************************************
# ** problem 0 ** (1 easy point) 
# Replace the number 0 in the definition below to indicate
# the number of hours you spent doing this assignment
# Decimal numbers (eg, 6.237) are fine.  Exclude time
# spent reading.

def hours():
    return 4

# ********************************************************
# here we create the burning building
# ********************************************************

room_map = UndirectedGraph(dict(
    H10=dict(H11=5,S10=5),
    H11=dict(H10=5,R11=5,H12=5),
    H12=dict(H11=5,R12=5,H13=5),
    H13=dict(H12=5,R13=5,H14=5),
    H14=dict(H13=5,R14=5,H15=5),
    H15=dict(H14=5,H16=5),
    H16=dict(H15=5,R16=5,H17=5),
    H17=dict(H16=5,R17=5,H18=5),
    H18=dict(H17=5,R18=5,H19=5),
    H19=dict(H18=5,S19=5),
    S19=dict(H19=5,S29=10,EXIT=10),

    EXIT=dict(S19=10),
    S10=dict(H10=5,S20=10),
    R11=dict(H11=5),
    R12=dict(H12=5,R13=5),
    R13=dict(H13=5,R12=5),
    R14=dict(H14=5,R15=5),
    R15=dict(H15=5,R14=5,R16=5),
    R16=dict(H16=5,R15=5),
    R17=dict(H17=5),
    R18=dict(H18=5),
    R19=dict(H19=5),

    H20=dict(H21=5,S20=5),
    H21=dict(H20=5,R21=5,H22=5),
    H22=dict(H21=5,R22=5,H23=5),
    H23=dict(H22=5,R23=5,H24=5),
    H24=dict(H23=5,R24=5,H25=5),
    H25=dict(H24=5,H26=5),
    H26=dict(H25=5,R26=5,H27=5),
    H27=dict(H26=5,R27=5,H28=5),
    H28=dict(H27=5,R28=5,H29=5),
    H29=dict(H28=5,S29=5),
    S29=dict(H29=5,S19=10,S39=10),

    S20=dict(H20=5,S10=5,S30=10),
    R21=dict(H21=5),
    R22=dict(H22=5,R23=5),
    R23=dict(H23=5,R22=5),
    R24=dict(H24=5,R25=5),
    R25=dict(H25=5,R24=5,R26=5),
    R26=dict(H26=5,R25=5),
    R27=dict(H27=5),
    R28=dict(H28=5),
    R29=dict(H29=5),

    H30=dict(H31=5,S30=5),
    H31=dict(H30=5,R31=5,H32=5),
    H32=dict(H31=5,R32=5,H33=5),
    H33=dict(H32=5,R33=5,H34=5),
    H34=dict(H33=5,R34=5,H35=5),
    H35=dict(H34=5,H36=5),
    H36=dict(H35=5,R36=5,H37=5),
    H37=dict(H36=5,R37=5,H38=5),
    H38=dict(H37=5,R38=5,H39=5),
    H39=dict(H38=5,S39=5),
    S39=dict(H39=5,S29=10,S49=10),

    S30=dict(H30=5,S20=10),
    R31=dict(H31=5),
    R32=dict(H32=5,R33=5),
    R33=dict(H33=5,R32=5),
    R34=dict(H34=5,R35=5),
    R35=dict(H35=5,R34=5,R36=5),
    R36=dict(H36=5,R35=5),
    R37=dict(H37=5),
    R38=dict(H38=5),
    R39=dict(H39=5),

    H40=dict(H41=5,S40=5),
    H41=dict(H40=5,R41=5,H42=5),
    H42=dict(H41=5,R42=5,H43=5),
    H43=dict(H42=5,R43=5,H44=5),
    H44=dict(H43=5,R44=5,H45=5),
    H45=dict(H44=5,H46=5),
    H46=dict(H45=5,R46=5,H47=5),
    H47=dict(H46=5,R47=5,H48=5),
    H48=dict(H47=5,R48=5,H49=5),
    H49=dict(H48=5,S49=5),
    S49=dict(H49=5,S39=10),

    S40=dict(H40=5,S30=10),
    R41=dict(H41=5),
    R42=dict(H42=5,R43=5),
    R43=dict(H43=5,R42=5),
    R44=dict(H44=5,R45=5),
    R45=dict(H45=5,R44=5,R46=5),
    R46=dict(H46=5,R45=5),
    R47=dict(H47=5),
    R48=dict(H48=5),
    R49=dict(H49=5)
    ))

room_map.locations = dict(
    H10=(40,50),
    H11=(50,50),
    H12=(60,50),
    H13=(70,50),
    H14=(80,50),
    H15=(90,50),
    H16=(100,50),
    H17=(110,50),
    H18=(120,50),
    H19=(130,50),

    S10=(40,50),
    R11=(50,60),
    R12=(60,60),
    R13=(70,60),
    R14=(80,60),
    R15=(90,60),
    R16=(100,60),
    R17=(110,60),
    R18=(120,60),
    R19=(130,60),
    S19=(140,50),
    EXIT=(165,40),


    H20=(40,75),
    H21=(50,75),
    H22=(60,75),
    H23=(70,75),
    H24=(80,75),
    H25=(90,75),
    H26=(100,75),
    H27=(110,75),
    H28=(120,75),
    H29=(130,75),

    S20=(40,75),
    R21=(50,85),
    R22=(60,85),
    R23=(70,85),
    R24=(80,85),
    R25=(90,85),
    R26=(100,85),
    R27=(110,85),
    R28=(120,85),
    R29=(130,85),
    S29=(140,75),

    H30=(40,100),
    H31=(50,100),
    H32=(60,100),
    H33=(70,100),
    H34=(80,100),
    H35=(90,100),
    H36=(100,100),
    H37=(110,100),
    H38=(120,100),
    H39=(130,100),

    S30=(40,100),
    R31=(50,110),
    R32=(60,110),
    R33=(70,110),
    R34=(80,110),
    R35=(90,110),
    R36=(100,110),
    R37=(110,110),
    R38=(120,110),
    R39=(130,110),
    S39=(140,100),
    
    H40=(40,125),
    H41=(50,125),
    H42=(60,125),
    H43=(70,125),
    H44=(80,125),
    H45=(90,125),
    H46=(100,125),
    H47=(110,125),
    H48=(120,125),
    H49=(130,125),

    S40=(40,125),
    R41=(50,135),
    R42=(60,135),
    R43=(70,135),
    R44=(80,135),
    R45=(90,135),
    R46=(100,135),
    R47=(110,135),
    R48=(120,135),
    R49=(130,135),
    S49=(140,125)
    )

room_map.temps = dict(
    
    H10=70,
    H11=70,	       
    H12=70,	       
    H13=70,
    H14=70,
    H15=70,
    H16=70,
    H17=70,
    H18=70,
    H19=70,
    
    S10=70,
    R11=70,
    R12=70,	       
    R13=70,
    R14=70,
    R15=70,
    R16=70,
    R17=70,
    R18=70,
    R19=70,
    S19=70,
    H20=80,
    H21=80,
    H22=80,
    H23=80,
    H24=80,
    H25=80,
    H26=80,
    H27=80,
    H28=80,
    H29=80,
    
    S20=80,
    R21=70,
    R22=70,
    R23=70,
    R24=70,
    R25=100,
    R26=70,
    R27=70,
    R28=70,
    R29=70,
    S29=80,
    
    H30=100,
    H31=100,
    H32=100,
    H33=100,
    H34=150,
    H35=150,
    H36=150,
    H37=100,
    H38=100,
    H39=100,
    
    S30=100,
    R31=100,
    R32=100,
    R33=100,
    R34=300,
    R35=500,
    R36=300,
    R37=100,
    R38=100,
    R39=100,
    S39=100,
    
    S40=80,
    H40=80,
    H41=80,
    H42=80,
    H43=80,
    H44=80,
    H45=80,
    H46=80,
    H47=80,
    H48=80,
    H49=80,
    
    R41=70,
    R42=70,
    R43=70,
    R44=100,
    R45=200,
    R46=100,
    R47=70,
    R48=70,
    R49=80,
    S49=80,
    EXIT=60
)

## useful if you want to display building in a jupyter notebook
## not needed to solve the homework
xnode_colors = {node: 'white' for node in room_map.locations.keys()}
xnode_positions = room_map.locations
xnode_label_pos = { k:[v[0],v[1]-3]  for k,v in room_map.locations.items() }
xedge_weights = {(k, k2) : v2 for k, v in room_map.graph_dict.items() for k2, v2 in v.items()}

room_graph_data = {  'graph_dict' : room_map.graph_dict,
                     'node_colors': xnode_colors,
                     'node_positions': xnode_positions,
                     'node_label_positions': xnode_label_pos,
                     'edge_weights': xedge_weights
}

'''

Define a function temp(node) that returns the temperature of the given
node in the graph.

'''

def temp(node):
   return room_map.temps.get(node, None)

'''
Define the following search routines that operate on the room_map
structure defined above.

- depth first search

- breadth first search

- best first search, where you always prefer the coolest room
  available

- worst first search, where you always prefer the hottest room
  available (this is good for finding the fire)

- astar search, using the g function based on path cost, h function
  based on estimated distance to goal state based on location data.

They each return a tuple consisting of the list of nodes comprising
the solution path, a single number indicating the cost of that path,
and a third integer indicating the cost of the search, i.e., the
number of nodes explored.  If the debug parameter is True, the return
tuple includes a fourth value, which is a list of the nodes visited,
in order.

The goal parameter may be either a string identifying a node, e.g.,
'R15', or a function of one argument that when evaluated, returns True
if the goal has been reached.

For the first four functions, the goal parameter is optional.  The default
goal is to find a room that is on fire.  Any room with a temperature over
400 degrees is on fire.
'''

class RoomProblem(Problem):
    
    def __init__(self, initial, goal=None, room_map=None):
        super().__init__(initial, goal)
        self.room_map = room_map

    def actions(self, state):
        return list(self.room_map.get(state).keys())
    
    def result(self, state, action):
        return action
    
    def goal_test(self, state):
        if self.goal:
            return state == self.goal
        return temp(state) > 400 
    
    def path_cost(self, c, state1, action, state2):
        return c + self.room_map.get(state1, state2)

    def value(self, state):
        raise NotImplementedError


def room_depth_first(initial, goal, debug=False):
    problem = RoomProblem(initial, goal, room_map)  # Pass room_map to the problem

    solution_node = depth_first_graph_search(problem)

    if solution_node is None:
        return None 

    # Extract solution path
    path = solution_node.path()
    path_nodes = [node.state for node in path] 
    path_cost = solution_node.path_cost 
    search_cost = len(problem.explored)  

    if debug:
        visited_nodes = list(problem.explored) 
        return (path_nodes, path_cost, search_cost, visited_nodes)

    return (path_nodes, path_cost, search_cost)


def room_breadth_first(initial, goal, debug=False):
    problem = RoomProblem(initial, goal, room_map)  # Pass room_map to the problem

    solution_node = breadth_first_graph_search(problem)

    if solution_node is None:
        return None 

    # Extract solution path
    path = solution_node.path()
    path_nodes = [node.state for node in path] 
    path_cost = solution_node.path_cost 
    search_cost = len(problem.explored) 

    if debug:
        visited_nodes = list(problem.explored)  
        return (path_nodes, path_cost, search_cost, visited_nodes)

    return (path_nodes, path_cost, search_cost)


def room_best_first(initial, goal, debug=False):
    problem = RoomProblem(initial, goal, room_map)  # Pass room_map to the problem

    solution_node = best_first_graph_search(problem)

    if solution_node is None:
        return None 

    # Extract solution path
    path = solution_node.path()
    path_nodes = [node.state for node in path]
    path_cost = solution_node.path_cost 
    search_cost = len(problem.explored) 

    if debug:
        visited_nodes = list(problem.explored) 
        return (path_nodes, path_cost, search_cost, visited_nodes)

    return (path_nodes, path_cost, search_cost)


def f_worst(node):
    # Return the temperature of the node, which is a measure of cost
    return room_map.get(node.state, float('inf'))  # Use temperature as "cost"
    
def room_worst_first(initial, goal, debug=False):
    problem = RoomProblem(initial, goal, room_map)  # Pass room_map to the problem
    
    solution_node = best_first_graph_search(problem, f_worst)

    if solution_node is None:
        return None 

    # Extract the solution path
    path = solution_node.path()
    path_nodes = [node.state for node in path] 
    path_cost = solution_node.path_cost 
    search_cost = len(problem.explored) 

    if debug:
        visited_nodes = list(problem.explored) 
        return (path_nodes, path_cost, search_cost, visited_nodes)

    return (path_nodes, path_cost, search_cost)


def room_heuristic(state, goal=None):
    """A simple heuristic function that calculates the difference in temperature between the current room and a goal room."""
    # If we have an explicit goal, use the temperature difference between the two rooms
    if goal:
        return abs(temp(state) - temp(goal))
    
    # If no goal, heuristic is the difference from 400 degrees (fire threshold)
    return abs(temp(state) - 400)

def room_astar(initial, goal, debug=False):
    problem = RoomProblem(initial, goal, room_map)  # Pass room_map to the problem

    # Perform A* search using the heuristic function
    solution_node = astar_search(problem, h=room_heuristic)

    if solution_node is None:
        return None 

    # Extract solution path
    path = solution_node.path()
    path_nodes = [node.state for node in path]
    path_cost = solution_node.path_cost 
    search_cost = len(problem.explored)

    if debug:
        visited_nodes = list(problem.explored) 
        return (path_nodes, path_cost, search_cost, visited_nodes)

    return (path_nodes, path_cost, search_cost)


'''
You may write auxiliary procedures and classes in addition to the
requested one(s) -- for each of your auxiliary procedures or classes,
please include a comment explaining what it does, and giving an
example or two.  I should state explicitly, I expect you to use
functions and classes defined in search.py.

Note: you will also need to change the signature of some of the search
procedures to provide the default parameter value for goal.

Finally, we shall apply search to your life.  When Bill Clinton was a
teenager, he wanted to be president.  Similarly, Brett Kavanaugh had
early ambitions to be a supreme court justice. In spite of their
various behavioral tangents, they each achieved their respective goal.

Which of the above search strategies could be applied to your life,
assuming you have a singular ambition?  Define the function
careerpath() below that returns a string, either "depthfirst",
"breadfirst", "bestfirst", or "astar".  I guess "worstfirst" should
also be in the mix. Just don't tell your parents.
'''
def careerpath():
    return "astar"

### test function from google python course
### =======================================
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if (hasattr(expected, '__call__')):
        OK = expected(got)
    else:
        OK = (got == expected)
    if OK:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('hours')
  print('# is it greater than 0?')
  test(hours(), lambda x: x > 0)

  print ('temp(node)')
  test(temp('R11'),70)
  test(temp('R35'),500)
  test(temp('EXIT'),60)
  test(temp('ENTRANCE'),None)

  print ('room_depth_first')
  test(room_depth_first('EXIT', 'S20'), (['S19', 'S29', 'S39', 'S49', 'H49', 'H48', 'H47', 'H46', 'R46', 'R45', 'R44', 'H44', 'H43', 'H42', 'H41', 'H40', 'S40', 'S30', 'S20'], 125, 26))

  test(room_depth_first('S20', 'EXIT'), (['S30', 'S40', 'H40', 'H41', 'H42', 'H43', 'H44', 'H45', 'H46', 'H47', 'H48', 'H49', 'S49', 'S39', 'S29', 'S19', 'EXIT'], 115, 21))

  test(room_depth_first('EXIT'), (['S19', 'S29', 'S39', 'S49', 'H49', 'H48', 'H47', 'H46', 'R46', 'R45', 'R44', 'H44', 'H43', 'H42', 'H41', 'H40', 'S40', 'S30', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'R35'], 150, 68))

  test(room_depth_first('EXIT',lambda x: x == 'S20'),(['S19', 'S29', 'S39', 'S49', 'H49', 'H48', 'H47', 'H46', 'R46', 'R45', 'R44', 'H44', 'H43', 'H42', 'H41', 'H40', 'S40', 'S30', 'S20'], 125, 26))

  print ('room_breadth_first')
  test(room_breadth_first('EXIT', 'S20'), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'S10', 'S20'], 75, 77))

  test(room_breadth_first('S20', 'EXIT'), (['H20', 'H21', 'H22', 'H23', 'H24', 'H25', 'H26', 'H27', 'H28', 'H29', 'S29', 'S19', 'EXIT'], 75, 83))

  test(room_breadth_first('EXIT'), (['S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'H35', 'R35'], 60, 51))

  test(room_breadth_first('EXIT',lambda x: x == 'S20'),(['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'S10', 'S20'], 75, 77))

  print ('room_best_first')
  test(room_best_first('EXIT', 'S20'), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'S10', 'S20'], 75, 23))

  test(room_best_first('S20', 'EXIT'), (['S10', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'S19', 'EXIT'], 75, 23))

  test(room_best_first('EXIT'), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'S10', 'S20', 'S30', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'R35'], 120, 85))

  test(room_best_first('EXIT',lambda x: x == 'S20'),(['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'S10', 'S20'], 75, 23))

  print ('room_worst_first')
  test(room_worst_first('EXIT', 'S20'), (['S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'R36', 'R35', 'R34', 'H34', 'H33', 'H32', 'H31', 'H30', 'S30', 'S20'], 105, 36))

  test(room_worst_first('S20', 'EXIT'), (['S30', 'H30', 'H31', 'H32', 'H33', 'H34', 'R34', 'R35', 'R36', 'H36', 'H37', 'H38', 'H39', 'S39', 'S29', 'S19', 'EXIT'], 105, 85))

  test(room_worst_first('EXIT'), (['S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'R36', 'R35'], 60, 10))

  test(room_worst_first('EXIT',lambda x: x == 'S20'), (['S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'R36', 'R35', 'R34', 'H34', 'H33', 'H32', 'H31', 'H30', 'S30', 'S20'], 105, 36))

  print ('room_astar')
  test(room_astar('EXIT', 'S20'), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'S10', 'S20'], 75, 18))

  test(room_astar('S20', 'EXIT'), (['H20', 'H21', 'H22', 'H23', 'H24', 'H25', 'H26', 'H27', 'H28', 'H29', 'S29', 'S19', 'EXIT'], 75, 14))

  print ('\ndebug examples\n')

  test(room_depth_first('EXIT','R15', debug=True), (['S19', 'S29', 'S39', 'S49', 'H49', 'H48', 'H47', 'H46', 'R46', 'R45', 'R44', 'H44', 'H43', 'H42', 'H41', 'H40', 'S40', 'S30', 'S20', 'S10', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'R15'], 170, 34, ['EXIT', 'S19', 'S29', 'S39', 'S49', 'H49', 'R49', 'H48', 'R48', 'H47', 'R47', 'H46', 'R46', 'R45', 'R44', 'H44', 'H43', 'R43', 'R42', 'H42', 'H41', 'R41', 'H40', 'S40', 'S30', 'S20', 'S10', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'R15']))

  test(room_breadth_first('EXIT','R15', debug=True), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'R15'], 40, 31, ['EXIT', 'S19', 'H19', 'S29', 'H18', 'R19', 'H29', 'S39', 'H17', 'R18', 'H28', 'R29', 'H39', 'S49', 'H16', 'R17', 'H27', 'R28', 'H38', 'R39', 'H49', 'H15', 'R16', 'H26', 'R27', 'H37', 'R38', 'H48', 'R49', 'H14', 'R15']))

  test(room_best_first('EXIT','R15', debug=True), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'R15'], 40, 17, ['EXIT', 'S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'R11', 'R12', 'R13', 'R14', 'R15']))

  test(room_worst_first('EXIT','R15', debug=True), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'R15'], 40, 67, ['EXIT', 'S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'R36', 'R35', 'R34', 'H34', 'H35', 'H33', 'H32', 'H31', 'H30', 'R31', 'R32', 'R33', 'R37', 'R38', 'R39', 'S30', 'H29', 'H28', 'H27', 'H26', 'H25', 'R25', 'H24', 'H23', 'H22', 'H21', 'H20', 'S20', 'S40', 'H40', 'H41', 'H42', 'H43', 'H44', 'R44', 'R45', 'R46', 'H45', 'H46', 'H47', 'H48', 'H49', 'R49', 'S49', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'R11', 'R12', 'R13', 'R14', 'R15']))

  test(room_astar('EXIT','R15', debug=True), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'R15'], 40, 8, ['EXIT', 'S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'R15']))

  test(room_depth_first('EXIT', debug=True), (['S19', 'S29', 'S39', 'S49', 'H49', 'H48', 'H47', 'H46', 'R46', 'R45', 'R44', 'H44', 'H43', 'H42', 'H41', 'H40', 'S40', 'S30', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'R35'], 150, 68, ['EXIT', 'S19', 'S29', 'S39', 'S49', 'H49', 'R49', 'H48', 'R48', 'H47', 'R47', 'H46', 'R46', 'R45', 'R44', 'H44', 'H43', 'R43', 'R42', 'H42', 'H41', 'R41', 'H40', 'S40', 'S30', 'S20', 'S10', 'H10', 'H11', 'H12', 'H13', 'H14', 'H15', 'R15', 'R16', 'H16', 'H17', 'H18', 'R18', 'R17', 'R14', 'R13', 'R12', 'R11', 'H20', 'H21', 'H22', 'H23', 'H24', 'H25', 'R25', 'R26', 'H26', 'H27', 'H28', 'R28', 'R27', 'R24', 'R23', 'R22', 'R21', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'R35']))

  test(room_breadth_first('EXIT', debug=True), (['S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'H35', 'R35'], 60, 51, ['EXIT', 'S19', 'H19', 'S29', 'H18', 'R19', 'H29', 'S39', 'H17', 'R18', 'H28', 'R29', 'H39', 'S49', 'H16', 'R17', 'H27', 'R28', 'H38', 'R39', 'H49', 'H15', 'R16', 'H26', 'R27', 'H37', 'R38', 'H48', 'R49', 'H14', 'R15', 'H25', 'R26', 'H36', 'R37', 'H47', 'R48', 'H13', 'R14', 'H24', 'R25', 'H35', 'R36', 'H46', 'R47', 'H12', 'R13', 'H23', 'R24', 'H34', 'R35']))

  test(room_best_first('EXIT', debug=True), (['S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'S10', 'S20', 'S30', 'H30', 'H31', 'H32', 'H33', 'H34', 'H35', 'R35'], 120, 85, ['EXIT', 'S19', 'H19', 'H18', 'H17', 'H16', 'H15', 'H14', 'H13', 'H12', 'H11', 'H10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'S10', 'S20', 'H20', 'H21', 'R21', 'H22', 'R22', 'R23', 'H23', 'H24', 'R24', 'H25', 'H26', 'R26', 'H27', 'R27', 'H28', 'R28', 'H29', 'R29', 'S29', 'R25', 'S30', 'S40', 'H40', 'H41', 'R41', 'H42', 'R42', 'R43', 'H43', 'H44', 'H45', 'H46', 'H47', 'R47', 'H48', 'R48', 'H49', 'R49', 'S49', 'H30', 'H31', 'H32', 'H33', 'R31', 'R32', 'R33', 'R44', 'R46', 'S39', 'H39', 'H38', 'H37', 'R37', 'R38', 'R39', 'H34', 'H35', 'H36', 'R45', 'R34', 'R36', 'R35']))

  test(room_worst_first('EXIT', debug=True), (['S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'R36', 'R35'], 60, 10, ['EXIT', 'S19', 'S29', 'S39', 'H39', 'H38', 'H37', 'H36', 'R36', 'R35']))
