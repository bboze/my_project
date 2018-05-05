'''
Created on 30 Apr 2018

@author: branko
'''

import sys
from root.nested.prim import PrimNum

if __name__ == '__main__':
    print('Hello World')

print(sys.path)

print((lambda isOdd: isOdd(4))(lambda x: x % 2 != 0))

def function():
 print('It is a function.')
 
foo = function
function()

import pickle

website = {'title' : 'Techbeamers', 'site_link' : '/','site_type': 'technology blog','owner':'Python Serialization tutorial','established_date':'Sep2015'}

with open ('website.pickle','wb') as f:
    pickle.dump(website,f)

with open ('website.pickle', 'rb') as f:
    data = pickle.load(f)
    print (data)

pn = PrimNum('tst', 10); 
pn.print_successive_primes(5, 10)

pn.is_prime(2)
        
#prim.print_successive_primes(5)                 

