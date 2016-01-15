try:
    import cPickle as pickle
except:
    import pickle
import pprint
import sys

import pickle, urllib.request

handle = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()

for elt in data:
    print("".join([e[1] * e[0] for e in elt]))

# pkl_file = open('banner.p', 'rb')
#f = open('banner.p', 'rb')
#data1 = pickle.load(f)

#data1_string = pickle.load(f)
    #data1_string = f.readlines()
#data2 = pickle.loads(data1_string)
#f.close()
#pprint.pprint(data1_string)

#pprint.pprint(data1)

# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)

#pkl_file.close()
