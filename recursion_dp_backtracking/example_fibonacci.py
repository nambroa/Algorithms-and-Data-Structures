from timeit import default_timer as timer


def recursive_fibonacci(number):
    if number == 0 or number == 1: return number
    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)


# Bottom up starts from the small solution and ascends into the bigger ones.
def bottom_up_dynamic_programming_fibonacci(number):
    if number == 0 or number == 1: return number
    fib_n_minus_two = 0
    fib_n_minus_one = 1
    for i in range(2, number):
        fib_n = fib_n_minus_two + fib_n_minus_one
        fib_n_minus_two = fib_n_minus_one
        fib_n_minus_one = fib_n
    return fib_n_minus_two + fib_n_minus_one


# Top down starts from the big solution and descends into the smaller ones
def top_down_dynamic_programming_fibonacci(number):
    memo = [0] * (number+1)  # We initialize first to avoid future resizes.
    return memoized_fibonacci(number, memo)


def memoized_fibonacci(number, memo):
    if number == 0 or number == 1: return number
    if memo[number] == 0:
        memo[number] = memoized_fibonacci(number-1, memo) + memoized_fibonacci(number-2, memo)
    return memo[number]

# Time comparison
start = timer()
recursive_fibonacci(30)
end = timer()
print("Recursive Fibonacci function took %s seconds" % (end - start))
start = timer()
top_down_dynamic_programming_fibonacci(35)
end = timer()
print("Top-Down DP Fibonacci function took %s seconds" % (end - start))
start = timer()
bottom_up_dynamic_programming_fibonacci(35)
end = timer()
print("Bottom-Up DP Fibonacci function took %s seconds" % (end - start))
