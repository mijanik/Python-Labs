import random
import numpy as np
import threading
import time
import collections
import functools
import operator
import matplotlib.pyplot as plt

dict1 = {}
dict2 = {}


def count_elements(seq, mydict: dict, thread_id: int) -> dict:
    for i in seq:
        mydict[i] = mydict.get(i, 0) + 1
    return mydict


def main():
    data = np.random.randint(10, size=1000000)
    threading.Thread(target=count_elements, args=(list(data[:len(data)//2]), dict1, 1)).start() #first half
    threading.Thread(target=count_elements, args=(list(data[len(data)//2:]), dict2, 2)).start() #second half

    while threading.active_count() != 1:
        pass

    print(threading.active_count())
    print(dict1)
    print(dict2)

    res = dict(functools.reduce(operator.add, map(collections.Counter, [dict1, dict2])))

    print(res)
    plt.bar(list(res.keys()), res.values(), color='g')
    plt.show()


if __name__ == '__main__':
    main()
