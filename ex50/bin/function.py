def nameMe():
    print("I am a Python Master!")
    return "here you are"
    
def argMe(arg1, arg2):
    print("this is " + arg1 + " and " + arg2)
    
def cubeMe(num):
    return num ** 3
    
def raiseMe(base, ex = 1):
    if ex > 1:
        return base ** ex
    else:
        return base
        
def multiAdd(*args):
    return sum(args)
    
nameMe()
#print nameMe()
#print nameMe
#argMe("Jerry", "Elaine")
print(cubeMe(5))
print(raiseMe(20, 3))
print(multiAdd(23, 45, 8, 12))