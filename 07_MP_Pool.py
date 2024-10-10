from multiprocessing import Pool
import time
def f(n):
    return n*n

if __name__ == "__main__":
    array = [1,2,3,4,5]
    p = Pool()  # with pool
    result = p.map(f,array)
    # result = []  # without pool
    # for n in array:
    #     result.append(f(n))
    print(result) # same result


# example 2
def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":
    t1 =time.time()
    p = Pool()
    results = p.map(f,range(10000))
    p.close()
    p.join()
    print(f'pool took time of: {time.time()-t1} seconds')

    t2=time.time()
    result = []
    for x in range(10000):
        result.append(f(x))

    print(f'seriel processing took time of: {time.time()-t2} seconds')



# pool argument called processes



def s(m):
    return m*m
if __name__ == "__main__":
    p = Pool(Processes=3)
    reslt =p.map(f,[1,2,3,4,5])
    for n in reslt:
        print(n)