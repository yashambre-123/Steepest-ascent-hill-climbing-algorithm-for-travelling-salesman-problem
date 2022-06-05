import random
from typing import List, Any


def random_solution(adjacency_matrix):
    cities = list(range(len(adjacency_matrix)))
    solution=[]
    for i in range(len(adjacency_matrix)):
        random_city = cities[random.randint(0, len(cities) - 1)]
        solution.append(random_city)
        cities.remove(random_city)
    return solution

def route_length(adjacency_matrix,solution):
    current_solution=solution
    routelength=0
    for i in range(1,len(current_solution)):
        routelength=routelength+adjacency_matrix[current_solution[i-1]][current_solution[i]]
    i=4
    routelength=routelength+adjacency_matrix[current_solution[i-1]][current_solution[0]]
    return routelength

def neighbours(solution):
    neighbourss=[]
    for i in range(0,len(solution)):
        for j in range(i+1,len(solution)):
            solution_copy = solution.copy()
            swap=solution_copy[i]
            solution_copy[i]=solution_copy[j]
            solution_copy[j]=swap
            neighbourss.append(solution_copy)
    return neighbourss

def best_neighbour(performance_metric,adjacency_matrix,neighbours_of_current_solution):
    performance_metric_of_neighbours=[]
    for i in range(0,len(neighbours_of_current_solution)):
        current_neighbour_performance_metric=route_length(adjacency_matrix,neighbours_of_current_solution[i])
        performance_metric_of_neighbours.append(current_neighbour_performance_metric)
    i=0
    minimum_performance_metric=10000
    for i in range(0,len(performance_metric_of_neighbours)):
        if (performance_metric_of_neighbours[i]<minimum_performance_metric):
            minimum_performance_metric=performance_metric_of_neighbours[i]
            index=i
    return neighbours_of_current_solution[index],minimum_performance_metric

def steepest_ascent_hill_climbing(adjacency_matrix):
    current_solution=random_solution(adjacency_matrix)
    performance_metric=route_length(adjacency_matrix,current_solution)
    neighbours_of_current_solution=neighbours(current_solution)
    best_performance_metric_neighbour,best_performance_metric=best_neighbour(performance_metric,adjacency_matrix,neighbours_of_current_solution)
    print("The first node:",current_solution)
    print("The performance metric of the starting node:",performance_metric)
    print("Neighbours of the starting node")
    print(neighbours_of_current_solution)
    print("The best performance metric neighbour of the starting node:",best_performance_metric_neighbour)
    print("The performance metric of the above node",best_performance_metric)
    while (best_performance_metric<performance_metric):
        performance_metric=best_performance_metric
        current_solution=best_performance_metric_neighbour
        neighbours_of_current_solution=neighbours(current_solution)
        best_performance_metric_neighbour, best_performance_metric=best_neighbour(performance_metric,adjacency_matrix,neighbours_of_current_solution)
    print("\n")
    print("This is the optimal path:",best_performance_metric_neighbour)
    print("This is the performance metric of optimal path:",best_performance_metric)

def main():
    adjacency_matrix = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]
    steepest_ascent_hill_climbing(adjacency_matrix)

if __name__ == "__main__":
     main()

