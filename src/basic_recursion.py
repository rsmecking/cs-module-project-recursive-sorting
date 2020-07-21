def countdown(n):
    if n == 0:
        return
    countdown(n-1)
    countdown(n-1)
    print(n)

countdown(3)


a = range(1,6)
def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])

print(sum_list(a))

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1) # recursive call

print(recursive_factorial(998))

def count_st(word):
    pass
    if len(word) > 2:
        return 0
    else:
        if word[0:2] == "st":
            return 1 + count_st(word[2:])
        