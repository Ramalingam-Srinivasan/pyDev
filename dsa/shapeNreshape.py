import numpy as np

if __name__ == "__main__":
    input_string = input("enter the list values : ")
    input_list = list(map(int, input_string.split()))
    print(input_list)
    my_arr = np.array(input_list)

    reshapped_arr = np.reshape(my_arr, (3, 3))
    print(reshapped_arr)