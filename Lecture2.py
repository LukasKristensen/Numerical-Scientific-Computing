import time

import numba
import numpy


def no_roll(N, a, b):
    i = 0
    sum1 = 0
    while i < N:
        sum1 += a[i]**b[i]
        i += 1


def two_roll(N, a, b):
    i = 0
    sum1, sum2 = 0, 0
    while i < (N/2-1):
        sum1 += a[2*i]**b[2*i]
        sum2 += a[2*i+1]**b[2*i+1]
        i += 1
    sum = sum1 + sum2


def four_roll(N, a, b):
    i = 0
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    while i < (N/4-1):
        sum1 += a[4*i]**b[4*i]
        sum2 += a[4*i+1]**b[4*i+1]
        sum3 += a[4*i+2]**b[4*i+2]
        sum4 += a[4*i+3]**b[4*i+3]
        i += 1
    sum = sum1 + sum2 + sum3 + sum4


def eight_roll(N, a, b):
    i = 0
    sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8 = 0, 0, 0, 0, 0, 0, 0, 0
    while i < (N/8-1):
        sum1 += a[8*i]**b[8*i]
        sum2 += a[8*i+1]**b[8*i+1]
        sum3 += a[8*i+2]**b[8*i+2]
        sum4 += a[8*i+3]**b[8*i+3]
        sum5 += a[8*i+4]**b[8*i+4]
        sum6 += a[8*i+5]**b[8*i+5]
        sum7 += a[8*i+6]**b[8*i+6]
        sum8 += a[8*i+7]**b[8*i+7]
        i += 1
    sum = sum1 + sum2 + sum3 + sum4 + sum5 + sum6 + sum7 + sum8


def exercise_two_one():
    """
    Exercise 2.1: "Loop unrolling"
    Implement the example of loop-unrolling in section 1.7.2 (p. 53-54) in Python. Ignore the use of pointers and use a
    while loop instead of for loop. The reason is that Python for loops are automatically optimized in the background.
    You should try to unroll at least 2 and 4 steps. See my results for 16 steps below.
    Measure the execution time.
    """
    N = 1e06

    a = numpy.linspace(1, 10, num=int(N))
    b = numpy.linspace(10, 1, num=int(N))

    start_time = time.time()
    no_roll(N, a, b)
    print("(2.1) [No Roll] Computation time:", time.time()-start_time)

    start_time = time.time()
    two_roll(N, a, b)
    print("(2.1) [Two Roll] Computation time:", time.time()-start_time)

    start_time = time.time()
    four_roll(N, a, b)
    print("(2.1) [Four Roll] Computation time:", time.time()-start_time)

    start_time = time.time()
    eight_roll(N, a, b)
    print("(2.1) [Eight Roll] Computation time:", time.time()-start_time)

    """
    Results without numba:
        (2.1) [No Roll] Computation time: 0.37106776237487793
        (2.1) [Two Roll] Computation time: 0.4389922618865967
        (2.1) [Four Roll] Computation time: 0.38599610328674316
        (2.1) [Eight Roll] Computation time: 0.38300108909606934
    """


def exercise_two_two():
    """
    Exercise 2.2: "Cache blocking"
    Implement the example in the 4th-6th line of section 1.7.3 (p. 55) in Python. Use while loop instead of for loop.
    Also, use Numba to compile your Python function for highest performance. Interpreted Python is too slow to reveal
    the difference in cache latency.
    Increase the size parameter, measure the execution time and calculate the time per operation. At some point, when
    exceeding the L1 cache size (often 32 KB), the time per operation should increase.
    Extend the code to use the cache blocking principle and verify that the time per operation goes down.
    """
    pass


if __name__ == '__main__':
    exercise_two_one()
