def main(num):
    x = 1
    fingers = ["thumb", "index", "middle", "ring", "pinkie"]
    # while(x <= num):
    #     print(x)
    #     x = x+1
        
    # for j in range(5, num + 2):
    #     print(j)
        
    for f in fingers:
        if len(f) >5: continue
        # if (x %2 ==1): break
        print (str(x) + f + " is a good boy")
        x = x+1
    
    for i, d in enumerate(fingers):
        print(d.upper() +" is at index " + str(i)) 
        
if __name__ == "__main__":
    main(8)
    