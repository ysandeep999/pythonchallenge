import urllib.request

add = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

num = '12345'

for iter in range(399):
    address = add + num

    f = urllib.request.urlopen(address)
    a = f.read().decode('utf-8')
    #print(a)
    num = a.split(" ")[-1]
    print(iter)
    
print(add)
#print(f.open())