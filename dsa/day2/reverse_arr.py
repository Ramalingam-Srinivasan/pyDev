import numpy


def arrays_func(arr):
    # complete this function
    # use numpy.array
    arr_val = numpy.array(arr,float)
    reversed_arr = arr_val[::-1]
    return reversed_arr

if __name__ == "__main__":
    print(arrays_func([1,2,3,4,5]))

