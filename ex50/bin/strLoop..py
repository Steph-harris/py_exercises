strT = "carrots"
vwls = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def revSt(sTr):
    rvsd = sTr[::-1]
    arrd = []
    
    # for x in range(len(strT) - 1, -1, -1):
    #     arrd.append(strT[x])
    
    for char in sTr:
        if char in vwls:
            arrd.append("*"+char+"*")
            # print ("*"+char+"*")
        else:
            arrd.append(char)
            # print (char)
        
    print("rvsd %s" % "".join(arrd)) 
    # print(rvsd)
if __name__ == "__main__":
    revSt(strT)