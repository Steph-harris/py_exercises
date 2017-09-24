def main():
    print 2 + 2

if __name__ == "__main__":
    main()
    
f = "F you, Debbie!"
#print(f)

def smFun():
    #global f
    f = 45
    print(f)
    
smFun()
print(f)

#del f
#print(f)