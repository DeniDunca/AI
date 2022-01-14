# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import math

import util
import random


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST

    return [s, s, w, s, w, w, s, w]


def randomSearch(problem):
    pointer = problem.getStartState()
    list = []
    while (not (problem.isGoalState(pointer))):
        successor = problem.expand(pointer)
        random_succ = int(random.random() * len(successor))
        random.choice(successor)
        next = successor[random_succ]
        pointer = random.choice(successor)[0]
        pointer = next[0]
        list.append(next[1])
    print(list)
    return list

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of path that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """

    """
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.expand(problem.getStartState()))
    "*** YOUR CODE HERE ***"
    for i in problem.expand(problem.getStartState()):
        print(i)

    mylist1 = {"Marcel": 14, "Maria": 13}
    mylist2 = {"Marcel2": 14, "Maria2": 13}

    stack = util.Stack()
    for (i, j) in mylist1.items():
        stack.push((i, j))
    for (i, j) in mylist2.items():
        stack.push((i, j))
    print(stack.pop())

    from game import Directions
    w = Directions . WEST
    e = Directions . EAST
    s = Directions .SOUTH

    return randomSearch(problem)
    
    """

    # calea pe care va merge pacman
    path = {}
    # in stiva tinem nodurile neexplorate
    frontier = util.Stack()
    # se pune in stiva state-ul de start
    frontier.push(problem.getStartState())
    # o lista de noduri explorate pentru a ne asigyra ca nu le parcurgem de mai multe ori
    explored = []
    path[problem.getStartState()] = []
    # daca stiva e goala si nu am gasit finish ul inseamna ca nu exista goal
    while not (frontier.isEmpty()):
        # scoatem primul nod din stiva si il punem il lista de noduri explorate
        current = frontier.pop()
        explored.append(current)
        # verificam daca am ajuns la goal
        if problem.isGoalState(current):
            return path[current]
        # adaugam celelalte noduri neexplorate in stiva (succesorii)
        for (state, action, cost) in problem.expand(current):
            if state not in explored:
                frontier.push(state)
                path[state] = path[current] + [action]
    return path[current]
    #util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # calea pe care va merge pacman
    path = {}
    # in coada tinem nodurile neexplorate
    frontier = util.Queue()
    # se pune in coada state-ul de start
    frontier.push(problem.getStartState())
    # o lista de noduri explorate pentru a ne asigura ca nu le parcurgem de mai multe ori
    explored = []
    path[problem.getStartState()] = []
    explored.append(problem.getStartState())
    while not (frontier.isEmpty()):
        # scoatem primul nod din coada
        current = frontier.pop()
        # verificam daca este goal-ul
        if problem.isGoalState(current):
            return path[current]
        # adaugam toti succesorii neexplorati in coada
        for (state, action, cost) in problem.expand(current):
            if state not in explored and state not in frontier.list:
                frontier.push(state)
                path[state] = path[current] + [action]
                explored.append(state)
    return path[current]
    #util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # folosim PriorityQueue pentru ca este importanta ordinea elementelor in queue in functie de h
    frontier = util.PriorityQueue()
    # o lista de noduri explorate pentru a ne asigura ca nu le parcurgem de mai multe ori
    explored = []
    # tine o tupla de state uri si path ul ca sa ajungem int-un state
    startingTuple = (problem.getStartState(), [], 0)
    frontier.push(startingTuple, 0)
    while not frontier.isEmpty():
        # dau pop la nodul cu euristica cea mai mica ( primul din PriorityQueue)
        current = frontier.pop()
        state = current[0]
        path = current[1]
        cost = current[2]
        # nu exploram stari deja explorate
        if state in explored:
            continue
        explored.append(state)
        # vedem daca starea este goal
        if problem.isGoalState(state):
            return path
        #adaugam toti succesorii neexplorati in coada
        for child in problem.expand(state):
            childState = child[0]
            newAction = child[1]
            newCost = child[2]
            if childState not in explored:
                # schimbam itemul din coada cu unul care are o prioritate mai mica
                frontier.update((childState, path + [newAction], cost + newCost), cost + newCost + heuristic(childState, problem))
    return []
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
