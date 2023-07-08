import numpy as np
import random

def RandPara1(start,end):
    '''This function returns
    a random parameter between low and upper
    interval, total is the total number of samples in the interval'''
    return random.uniform(start,end)

def RandPara2(start,end):
    '''This function returns
    a random parameter between low and upper
    interval, total is the total number of samples in the interval'''
    return random.randint(start,end)

def RandPara(low,upper,total):
    '''This function returns
    a random parameter between low and upper
    interval, total is the total number of samples in the interval'''
    a =+ upper
    b =+ low
    return a + (b - a) * (np.random.random_integers(total) - 1) / (total - 1.)


def main():
    print(RandPara(0,1,60))
    

if __name__== '__main__':
    print()
