# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

if __name__ == "__main__":
    num_item = int(input())
    items = list(map(int, input().split()))
    num_customers = int(input())
    stock = Counter(items)
    total_income = 0

    for _ in range(num_customers):
        size, price = map(int, input().split())
        if stock[size] > 0:
            total_income += price
            stock[size] -= 1

    print(total_income)
