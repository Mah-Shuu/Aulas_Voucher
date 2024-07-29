def media(*args: float):
    total = 0
    for num in args:
        total+=num
    total = total/len(args)
    return total

x = media(4,34,76,55,9)

print(x)