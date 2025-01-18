import math
import os
import random
import re
import sys

if __name__ == "__main__":
    def find_weirdness(n):
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0:
            if 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            else:
                print("Not Weird")
        return

    find_weirdness(24)