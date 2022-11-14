import numpy as np
import threading
import collections
import functools
import operator
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

dict_list = [{}, {}]

def count_elements(seq, mydict: dict, thread_id: int) -> dict:
    for i in seq:
        mydict[i] = mydict.get(i, 0) + 1
    return mydict


def main():
    data = np.random.randint(10, size=1000000)
    #t1 = threading.Thread(target=count_elements, args=(list(data[:len(data)//2]), dict1, 1)).start() #first half
    #t2 = threading.Thread(target=count_elements, args=(list(data[len(data)//2:]), dict2, 2)).start() #second half

    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(count_elements, list(data[:len(data)//2]), dict_list[0], 1)
        f2 = executor.submit(count_elements, list(data[len(data)//2:]), dict_list[1], 2)
        print(f1.result())
        print(f2.result())

    #t1.join()
    #t2.join()

    print(threading.active_count())

    res = dict(functools.reduce(operator.add, map(collections.Counter, [dict_list[0], dict_list[1]])))

    print(res)
    plt.bar(list(res.keys()), res.values(), color='g')
    plt.show()


if __name__ == '__main__':
    main()