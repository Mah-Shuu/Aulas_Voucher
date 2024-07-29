def media(*args:float):
    med = 0
    for num in args:
        med+=num
    med = med/len(args)
    return med

res = media(1,2,3,4,5,6,7,8,9)

print(res)