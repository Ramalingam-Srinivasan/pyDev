if __name__ == '__main__':
    # Read the integer n
    num = int(input("enter the input values :"))

    # Read the space-separated integers and convert them to a list
    integer_list = list(map(int, num.split()))

    # Convert the list to a tuple
    t = tuple(integer_list)

    # Print the hash value of the tuple
    print(hash(t))
