# Importing Libraries
import numpy as np
import random, math
import matplotlib.pyplot as plt

def random_generator(dim , num):
    points= np.random.randint(low=0,high=100,size=(num,dim))
    return points

def mean(x):
    mean = np.mean(x)
    return mean


def distance(a, b):
    dist = np.linalg.norm(a-b)
    return dist


def knn(points, num_samples, K):
    mean_avg = []
    for num in num_samples:
        distance_list = []

        for p in points:
            dis = distance(p,num)
            distance_list.append(dis)

        distance_list.sort()
        tmp_res = mean(distance_list[:K])
        mean_avg.append(tmp_res)

    return mean_avg

def plot(dims , avg_dist):
    plt.figure(figsize=(20,10))

    for d,avr in zip(dims,avg_dist):
        plt.plot(avr,label=str(d))
        
    plt.legend()
    plt.show()

def plot2(dims , avg_dist):
    avg_dist = list(map(lambda x: mean(x),avg_dist))

    plt.figure(figsize=(20,10))

    plt.plot(dims,avg_dist)
    plt.scatter(dims,avg_dist)

    label = list(map(lambda x:str(x),dims))
    plt.show()



if __name__ == "__main__":
    dims = [1, 2, 3, 10, 100]
    avg_dist = []
    plt.style.use("seaborn")
    for d in dims:
        points = random_generator(dim=d,num=100)
        num_samples = random_generator(dim=d,num=10)
        res = knn(points=points, num_samples=num_samples, K=6)
        avg_dist.append(res)
        
    plot(dims,avg_dist)
    plot2(dims,avg_dist)
    

    
