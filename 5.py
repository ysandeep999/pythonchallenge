import urllib.request

add = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

num = '12345'

for iter in range(300):
    address = add + num

    f = urllib.request.urlopen(address)
    a = f.read().decode('utf-8')
    #print("test")
    num = a.split(" ")[-1]
    print(iter," : ",num)
    
print("ans found in 276: peak.html")
#print(add)
#print(f.open())