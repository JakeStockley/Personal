import numpy as np
import matplotlib.pyplot as mp

# time steps used (start value, stop value, total steps)
max_iter = 10000 # TOTAL NUMBER OF ITERATIONS
final_time = 100 # FINAL VALUE OF TIME
x = np.linspace(0, final_time, num=max_iter)
timestep = np.divide(final_time, max_iter)

# Function of force over time
def F(t):
    return 0 if t > 1 else 1
    
# the function we are evaluating, the inputs are: state=current state of system time = time
def f(state,time):
    # a = [p1, p2, v1, v2]
    p1 = state[0]
    p2 = state[1]
    v1 = state[2]
    v2 = state[3]
    # Define the only constant we have: The mass of mass 1
    m1 = 5
    # State space:
    state_space = [
        v1, # The rate of change of p1
        v2, # The rate of change of p2
        ( -2*p1 - 2*v1 + p2 + v2 ) / m1, # The rate of change of v1
        p1 + v1 - p2 - v2 + F(time) # The rate of change of v2
        ]
    return state_space

# Initial system conditions
y0= [
     1, #p1
     1, #dp1/dt
     1, #p2
     1  #dp2/dt
     ]

def euler(f, y0, timeset):
    iteration = 0
    state = y0
    y = []
    while iteration != max_iter:
        print("----------------------| ITERATION "+str(iteration)+" |----------------------------")
        print("CURRENT STATESPACE", state)
        print("CURRENT TIME", x[iteration])
        state = np.add(state, np.multiply(timestep, f(state, x[iteration])))
        y = y + [state[1]]
        iteration = iteration + 1

    print("OPERATION COMPLETE")
    mp.plot(x, y)
    return y

def heun(f, y0, x):
    iteration = 0
    state = y0
    y = []
    while iteration != max_iter:
        print("----------------------| ITERATION "+str(iteration)+" |----------------------------")
        print("CURRENT STATESPACE", state)
        print("CURRENT TIME", x[iteration])
        euler =  np.add(state, np.multiply(timestep, f(state, x[iteration])))
        state = np.add(state, np.multiply(np.divide(timestep, 2),np.add(f(state,x[iteration]), f(euler, np.add(x[iteration], timestep)))))
        y = y + [state[1]]
        iteration = iteration + 1

    print("OPERATION COMPLETE")
    mp.plot(x, y)
    return y

# Running the functions
euler(f, y0, x)
heun(f, y0, x)
