# Importing Libraries
import matplotlib.pyplot as plt
import random
import numpy as np

def random_generator(dim , num):
    points= np.random.randint(low=0,high=100,size=(num,dim))
    return points

def oneD():
    points = random_generator(1,50)

    plt.figure(figsize=(10,5))
    plt.scatter(points, np.zeros_like(points), s=80, facecolors='b', edgecolors='b')
    plt.grid(color='gray', linestyle='-', linewidth=1,axis='x')
    plt.title("1 Dim")

    plt.show()

    unique, counts = np.unique(points//20, return_counts=True)
    plt.bar(unique, counts)

    plt.show()

def twoD():
    points = random_generator(2,50)
    x_tmp, y_tmp = list(zip(*points))
    
    plt.figure(figsize=(10,10))
    plt.scatter(x_tmp, y_tmp, s=80, facecolors='b', edgecolors='b')
    plt.grid(color='gray', linestyle='-', linewidth=1, axis='both')
    plt.title("2 Dim")

    plt.show()
    
    points= np.random.randint(low=0,high=100,size=(50,2))
    bin = list(map(lambda point: f'{point[0]//20}{point[1]//20}', points))
    unique, counts = np.unique(bin, return_counts=True)
    plt.figure(figsize=(20,10))

    plt.bar(unique, counts)

def threeD():
    points = random_generator(3,50)
    x_tmp, y_tmp, z_tmp = list(zip(*points))
    
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_tmp, y_tmp, z_tmp, c='r', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title("3 Dim")

    plt.show()

    bin = list(map(lambda point: f'{point[0]//20}{point[1]//20}{point[2]//20}', points))
    unique, counts = np.unique(bin, return_counts=True)
    plt.figure(figsize=(20,10))
    plt.bar(unique, counts)

    plt.show()

if __name__ == "__main__":
    oneD()
    twoD()
    threeD()
