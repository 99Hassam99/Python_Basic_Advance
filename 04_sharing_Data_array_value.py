import multiprocessing

def cal_square(number,result,v):
    v.value = 5.673
    for idx, n in enumerate(number):
        result[idx] = n*n


if __name__ == "__main__":
    number = [3,5,6]  # should give 3 numbers digits
    result = multiprocessing.Array("i",3) # because of this 3 we can only pass 3 numbers in a list
    v = multiprocessing.Value('d',0.0)
    p =multiprocessing.Process(target=cal_square, args=(number,result,v))

    p.start()
    p.join()

    print(result[:])
    print(v.value)