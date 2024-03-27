def add(*args):
    return sum(args)

print("addition:",add(1,2,3))
print("addition:", add(1,5,7,3))

def sub(*args):
    result = args[0] - sum(args[1:])
    return result
