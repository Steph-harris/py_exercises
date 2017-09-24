class myClass():
    def method1(self):
        print "myclass method 1"
        
    def method2(self, newStr):
        print "second method gets " + newStr
        
class secClass(myClass):
    def secMeth2(self):
        print("second class meth")
        
    def secMeth1(self):
        myClass.method1(self)
        print("another class method 1")
        
def main():
    aInst = myClass()
    aInst.method1()
    aInst.method2("some other arg")
    bInst = secClass()
    bInst.secMeth1()

if __name__ == "__main__":
    main()