sList = [2, 5, 12, 22, 31, 38, 44, 54, 59, 72, 85, 90, 99, 102]

def liSrch(guess, arList):
    guesses = 0
    
    while(guesses < len(arList)):
        if(guess == arList[guesses]):
            print("item was at index %d" % guesses)
            return
        elif(guess < arList[guesses]):
            break
        else:
            guesses +=1
       
    print("item not in list. Guesses: %d" % guesses)
    
def biSrch(guess, arList):
    guesses = 0
    lo = 0
    mid = round(len(arList) / 2)
    high = len(arList) -1
    
    while(guess >= arList[lo] and guess <= arList[high]):
        guesses += 1
        
        if(guess == arList[mid]):
            print("Found %s in %d guesses" % (guess, guesses))
            return
        elif(guess < arList[mid]):
            high = mid - 1
            mid = round(high / 2)
        else:
            low = mid + 1
            mid = round((high + low) /2)
    
    print("%d not found in list. Guesses: %d" % (guess, guesses))
    
liSrch(100, sList)
biSrch(100, sList)
