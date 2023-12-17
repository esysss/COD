import numpy as np
import random, math
import matplotlib.pyplot as plt
from random import randrange


def random_generator(dim, num):
    points = np.random.rand(num,dim)
    return points


def mean(x):
    mean = np.mean(x)
    return mean


def distance(a, b):
    dist = np.linalg.norm(a-b)
    return dist


def ratio(points, random_index):
    distance_list = []
    for p in points:
        dis = distance(p,random_index)
        distance_list.append(dis)

    dist_max = np.max(distance_list)
    dist_min = np.min(distance_list)

    ratio_x =(dist_max - dist_min)/dist_min

    return ratio_x


def plot(dims , ratio):
    ratio = list(map(lambda x: mean(x),ratio))

    plt.figure(figsize=(20,10))

    plt.plot(dims,ratio)
    plt.scatter(dims,ratio)

    label = list(map(lambda x:str(x),dims))
    plt.show()


if __name__ == "__main__":
    dims = [2,3,5,10,20,30,50,100]
    ratio_list=[]
    for i in dims:
        points = random_generator(dim=i,num=50)
        random_index = random_generator(dim=i,num=10)

        x = ratio(points,random_index)
        ratio_list.append(x)
        print(x)
    plot(dims , ratio_list)
