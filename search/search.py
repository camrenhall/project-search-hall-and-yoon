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

import util
from game import Directions


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

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    # Initialize stack used for DFS
    _Stack = util.Stack()
    # Initialize set used to track what nodes we have already visited
    _Visited = []
    # Get starting state and push it onto stack
    startingState = problem.getStartState()
    if problem.isGoalState(startingState):
        return []

    _Stack.push((startingState, []))
    # Set of directions to convert from string to game.Direction type
    _setDirections = {'North': Directions.NORTH, 'South': Directions.SOUTH,
                      'East': Directions.EAST, 'West': Directions.WEST}
    while not _Stack.isEmpty():
        # Pop top item, see if not visited
        top = _Stack.pop()
        space = top[0]
        dir = top[1]
        if problem.isGoalState(space):
            return dir
        if space not in _Visited:
            _Visited.append(space)
            for it in problem.getSuccessors(space):
                if it[0] not in _Visited:
                    _Stack.push((it[0], dir + [_setDirections[it[1]]]))

def breadthFirstSearch(problem):
    # Initialize stack used for BFS
    _Queue = util.Queue()
    # Initialize set used to track what nodes we have already visited
    _Visited = []
    # Get starting state and push it onto stack
    startingState = problem.getStartState()
    if problem.isGoalState(startingState):
        return []

    _Queue.push((startingState, []))
    # Set of directions to convert from string to game.Direction type
    _setDirections = {'North': Directions.NORTH, 'South': Directions.SOUTH,
                      'East': Directions.EAST, 'West': Directions.WEST}
    while not _Queue.isEmpty():
        # Pop top item, see if not visited
        top = _Queue.pop()
        space = top[0]
        dir = top[1]
        if problem.isGoalState(space):
            return dir
        if space not in _Visited:
            _Visited.append(space)
            for it in problem.getSuccessors(space):
                if it[0] not in _Visited:
                    _Queue.push((it[0], dir + [_setDirections[it[1]]]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # initialize priority queue for UCS and set for visited nodes
    _PriorityQueue = util.PriorityQueue()
    _Visited = []
    startingState = problem.getStartState()

    # check if starting state is goal state
    if problem.isGoalState(startingState):
        return []

    _PriorityQueue.push((startingState, [], 0), 0)
    # Set of directions to convert from string to game.Direction type
    _setDirections = {'North': Directions.NORTH, 'South': Directions.SOUTH,
                      'East': Directions.EAST, 'West': Directions.WEST}

    while not _PriorityQueue.isEmpty():
        # Pop top item, see if not visited
        top = _PriorityQueue.pop()
        space = top[0]
        dir = top[1]
        cost = top[2]
        if problem.isGoalState(space):
            return dir
        if space not in _Visited:
            _Visited.append(space)
            for it in problem.getSuccessors(space):
                if it[0] not in _Visited:
                    _PriorityQueue.push((it[0], dir + [_setDirections[it[1]]], cost+it[2]), it[2])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # initialize priority queue for UCS and set for visited nodes
    _PriorityQueue = util.PriorityQueue()
    _Visited = []
    startingState = problem.getStartState()

    # check if starting state is goal state
    if problem.isGoalState(startingState):
        return []

    _PriorityQueue.push((startingState, [], 0), 0)
    # Set of directions to convert from string to game.Direction type
    _setDirections = {'North': Directions.NORTH, 'South': Directions.SOUTH,
                      'East': Directions.EAST, 'West': Directions.WEST}

    while not _PriorityQueue.isEmpty():
        # Pop top item, see if not visited
        top = _PriorityQueue.pop()
        space = top[0]
        dir = top[1]
        cost = top[2]
        if problem.isGoalState(space):
            return dir
        if space not in _Visited:
            _Visited.append(space)
            for it in problem.getSuccessors(space):
                if it[0] not in _Visited:
                    h_cost = cost + it[2] + heuristic(it[0], problem)
                    _PriorityQueue.push((it[0], dir + [_setDirections[it[1]]], cost + it[2]), h_cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
