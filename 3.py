import string


start = 0
numdict = []

def pychal(num, line):
        

    #lngstr1 = input("enter long string : ")

    #lngstr1 = "2)ocr\n3)"
    
    lngstr = line.replace("\n","")

    

    lnlen = len(lngstr)
    global start
    #start = 0

    for a in lngstr:
        #print(ord(a))
        aci = ord(a)

        if aci in range(num,num + 1): #and aci in range(90,127):
            #print(a)
            start += 1

        #if(start != 0):
            #print(start)
            

    #return start
    #print("\n\n total len : ",lnlen,"\n output len :",start)


def files(nnn):

    global start, numdict
    f = open('3text.txt', 'r')
    #num = {}

    for number in range(nnn,nnn + 1):
        start = 0
        for line in f:
            pychal(number, line)
        numdict.append([chr(number),start])
        #numdict[chr(number)] = start
        #start = 0
    #print("end")
    #print(type(num))
    #print(numdict)

def st():
    for nn in range(0,127):
        files(nn)

    for item in numdict:
        if item[1] != 0:
            print(item)
    #print(numdict)
    #for keys,values in numdict.items():
        #if(values > 0 and values < 1000):
        #    print(keys,":",values)
    #print(numdict)
#st()

def linefinder(line):
    for chactr in line:
        assi = ord(chactr)
        if assi not in range(0,65) and assi not in range(91,97) and assi not in range(123,128):
            print(chr(assi))                  

def beginhere():
    f = open('3text.txt', 'r')
    #num = {}
    for line in f:
        linefinder(line)
        
beginhere()
    
#files()
