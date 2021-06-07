
import random as rn
import statistics as st
import matplotlib.pyplot as plt


def fitness_function(board):
    fitness=[]
    for i in board:
        if i in fitness:
            while True:
                 r =rn.randint(1, len(board))
                 if(r not in fitness):
                     fitness.append(r)
                     break
        else: 
            fitness.append(i) 
    return fitness



def switch(n,goal):
    for i in range(n):
        j = rn.randint(0, len(goal)-1)
        k = rn.randint(0, len(goal)-1)
        goal[j] = goal[k]  
        goal[k] = goal[j]
    return goal


def reproduce(x):
    return switch(3,x)


def mutation(board):
    return switch(1,board)


def create_population(population_size, total_queens):
    population =[]
    for i in range(population_size):
        random=[]
        for i in range(total_queens):
            r  =rn.randint(1, total_queens)
            random.append(r)
        population.append(random)
    return population    




def compute_goal_fit(n):
    goal_fit = 0
    for i in range(n):
        goal_fit =goal_fit + i
    return goal_fit



def fitness(board,goal_fit):
    check =[]
    count=0
    for i in board:
        if i in check:
            count =count+1
        for j in range(i+1,len(board)):
            if abs(i-board[j])==(j-i):
                count = count + 1

        check.append(i)
                
    return goal_fit - count    



def random_selection(population, fitness, goal_fit):
    j = rn.randint(0, len(population)-1)
    j =population[j]
    k = rn.randint(0, len(population)-1)
    k =population[k]
    i =rn.randint(0, len(population)-1)
    for p in range(i):
         j[p]=k[p]
    
    return  fitness(j)



def gen_alg(population):
    nmax = 100000
    n = nmax
    goal_fit = compute_goal_fit(len(rn.choice(population)))
    print("\ngoal fit for current population ",goal_fit)
    print("problem dimension: ",len(rn.choice(population)),"x",len(rn.choice(population)))
    print("population size: ",len(population))
    print("max generation: ",n)
    print("\nrunning")
    
    while n>0:
        new_population =[]
        for i in range(len(population)):
            x = random_selection(population,fitness_function, goal_fit)
            board = reproduce(x)
            if rn.uniform(0,1)<1.0:
                board = mutation(board)
            if fitness(board,goal_fit) == goal_fit:
                print("...done.")
                print("optimal solution = ",board, " \nfound after ", nmax-n, "generations.")
                population.append(board)
                return population
            new_population.append(board)
        population = new_population
        n -=1
    print("no solution found in ",nmax, " generation try again.")
    return None

dimension= int(input("Enter the number of queens : "))  # input your dimension here for N-queen problem 
                                                        #such as 4 by 4,5 by 5 ,8 by 8 and so on 

population=create_population(dimension,dimension)   
iteration=gen_alg(population)

x=[]
y=[]
for i in range(len(iteration)): 
    x.append(i)
    y.append(st.variance(iteration[i]) )


plt.plot(x, y) 
plt.xlabel('Fitness') 
plt.ylabel('Variance of fitness')

plt.title('Evolution of fitness') 
  
plt.show()


