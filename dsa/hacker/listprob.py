#'s learn about list comprehensions! '
#   'You are given three integers  and  representing the dimensions of a cuboid along with an integer . '
#  'Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . '
# ' use list comprehensions rather than multiple loops, as a learning exercise.)

#https://www.hackerrank.com/challenges/list-comprehensions/problem



if __name__ == '__main__':

    def input_values(x,y,z,n):

        result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
        return result

    print(input_values(1,1,1,2))
