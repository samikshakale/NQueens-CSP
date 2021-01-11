#!/usr/bin/python3
import sys
import collections
import time
counter = 0
def main():
    num = input("WHAT SIZE?            ")
    N = int(num)
    state = createState(N)
    # var1 = get_next_unassigned_var(state)
    # print("Var1: " + str(var1))
    #assign(state, 1, 1)
    # print(state)
    # var2 = get_next_unassigned_var(state)
    # print("Var2: " + str(var2))
    #assign(state, 2, 5)
    # print(state)
    # print(goal_test(state))
    #assign(state, 3, 8)
    # assign(state, 4, 6)
    # assign(state, 5, 3)
    #assign(state, 6, 7)
    #print(state)
    #print(get_next_unassigned_var(state, N))

    # assign(state, 7, 2)
    # assign(state, 8, 4)
    # print(goal_test(state))
    #print state
    start = time.time()
    result = CSP_solve(state, N)
     
    end = time.time()  
    elapsed = end - start
    print("N: " + str(N))
    print("Time: " + str(elapsed))
    print("# recursions: " + str(counter))
    print("Result: " + str(result)) 
    
def CSP_solve(state, N):
    global counter
    counter+=1
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state, N)
    #print("Var" + str(var))
    if var != None:
        for val in get_Sorted_Values(state, var, N):
            #print("Entered for")
            new_state = copy(state)
            new_tup = assign(new_state, var, val)
            #if check(new_state, var) == False:
            if new_tup[1] == False:
                continue
            result = CSP_solve(new_state, N)
            if result == False:
                continue
            if goal_test(result) == True:
                return result
    return False
    
def goal_test(state):
    for x in state:
        if state[x][0] == None:
            return False
    for x in state:
        for y in state:
            if x == y:
                continue
            if abs(state[x][0] - state[y][0]) == abs(x - y):
                return False
            if state[x][0] == state[y][0]:
                return False
    return True
def copy(D):
    D2 = {x:(D[x][0], set(D[x][1])) for x in D}
    return D2

def check(state, lastRow):
    if lastRow == 1:
        return True
    for x in range(1, lastRow + 1):
        for y in range(1, lastRow + 1):
            if x == y:
                continue
            if state[x][0] or state[y][0] == None:
                continue
            if abs(state[x][0] - state[y][0]) == abs(x - y):
                return False
            if state[x][0] == state[y][0]:
                return False
    return True
    
    # for x in state:
    #     if state[x][0] == None:
    #         continue
    #     for y in state:
    #         if state[y][0] == None:
    #             continue
    #         if abs(state[x][0] - state[y][0]) == abs(x - y):
    #             return False
    #         if state[x][0] == state[y][0]:
    #             return False
    # return True 
                
def get_next_unassigned_var(state, N):
    min_length = N +1
    next_var = 0
    for x in state:
        if state[x][0] != None:
            continue
        cur_length = len(state[x][1])
        if cur_length < min_length:
            min_length = cur_length
            next_var = x
        #state[x][0] == None:
            #return x
    #return None
    return next_var
    
def createState(finNum):
    state = dict()
    possibleLoc = set()
    for x in range(1,finNum+1):
        possibleLoc.add(x)
    for x in range(1,finNum+1):
        state[x] = (None, possibleLoc)
    return state

def checkDiagonals(state, row1, col1):
    return None

def get_Sorted_Values(state, row, N): #should return a list ordered by edges then middle positions
    #my_list.sort(key=lambda x: x[1]) --> sorts based on second value in tuple
    center = (float(N + 1))/2
    #reg_lst = list(state[row][1])
    sorted_lst = []
    for x in state[row][1]:
        if x < center:
            sorted_lst.append((x, x-0))
        else:
            sorted_lst.append((x, N-x))
    sorted_lst.sort(key=lambda x: x[1])
    to_ret = [i[0] for i in sorted_lst]        
    return to_ret
    #return state[row][1]
    
#def updatePossibleLoc(state, placedRow, placedCol):


def assign(state, var, val):
    state[var][1].remove(val)
    copy = state[var][1]
    state[var] = (val, copy)
    diag1 = 0
    diag2 = 0
    for x in state:
        if x == var:
            continue    
        diag1 = val-(x-var)
        diag2 = val+(x-var)
        new_set = state[x][1].copy()
        if diag1 in new_set:
            new_set.remove(diag1)
        if diag2 in new_set:
            new_set.remove(diag2)
        if val in new_set:
            new_set.remove(val)
        state[x] = (state[x][0], new_set)
    counter = True
    for x in state:
        for y in state:
            if x == y:
                continue
            if state[x][0] == None:
                continue
            if state[y][0] == None:
                continue
            if abs(state[x][0] - state[y][0]) == abs(x - y):
                 counter = False
            if state[x][0] == state[y][0]:
                 counter = False
    return (state, counter)    #return a tuple with (state,True/False)   

main()
      
#write a method for checking the diagonals
#write a method for checking whether a state is completely finished and works
#write a method for checking whether a state works, up until its most recent queen (might not have to do this)
#write the shell recursion method
#write a method to update the state dictionary's set of possible places
#write a get_sorted_values method to return all the possible places for a given queen (given row)
#write an assign method to place a queen
#write a method to get the next queen to place
