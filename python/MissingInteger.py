def solution(A):
    # write your code in Python 3.6
    # sorting? o no sorting?
    miss = 1
    for x in sorted(A):
        if x == miss:
            miss +=1
        if x > miss:
            return miss
    return miss