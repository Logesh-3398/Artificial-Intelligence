import random
import numpy as np

alpha = 0.3
discount = 0.1
directions = ["up", "right", "down", "left"]
epsilon = 0.5
iterations = 100000
seed = 1
goal = []
forbidden = -1
wall = -1
start = 1

q_val = {}

for i in range(16):
    q_val[i] = {
        "up":0,
        "right":0,
        "down":0,
        "left":0
    }

random.seed(seed)

def best_action(q):
    action = "up"
    val = q["up"]
    for d in directions:
        if val < q[d]:
            val = q[d]
            action = d
    return action

def best_val(q):
    val = q["up"]
    for d in directions:
        if val < q[d]:
            val = q[d]
    return val

def get_reward(state):
    if state in goal:
        return 100
    elif state == forbidden:
        return -100
    return -0.1

def get_state(state,action):
    old_state = state
    if action == "up":
        if state + 4 < 16:
            state += 4
    elif action == "down":
        if state - 4 >= 0:
            state -= 4
    elif action == "right":
        if (state + 1) % 4 != 0:
            state += 1
    else:
        if (state) % 4 != 0:
            state -= 1
    if state == wall:
        return old_state
    return state



val = input()
val = val.split()
goal.append(int(val[0]) - 1)
goal.append(int(val[1]) - 1)
forbidden = int(val[2]) - 1
wall = int(val[3]) - 1

for _ in range(iterations):
    state = start
    while True:
        best = best_action(q_val[state])
        r = random.uniform(0,1)
        if r < epsilon:
            c = random.randint(0,3)
            best = directions[c]

        next_state = get_state(state,best)
        q_val[state][best] = (1-alpha)*q_val[state][best] + alpha*(get_reward(next_state) + discount*best_val(q_val[next_state]))
        
        state = next_state
        
        if state in goal or state == forbidden:
            break
    
if val[4] == 'p':
    for i in range(16):
        state = best_action(q_val[i])
        if i in goal:
            state = "goal"
        elif i == forbidden:
            state = "forbid"
        elif i == wall:
            state = "wall-square"
        print(f"{i+1}    {state}")
else:
    state = int(val[5]) - 1
    for d in directions:
        print(f"{d}    {round(q_val[state][d],2)}")