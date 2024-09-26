"""
we will create two programs ,
1. to create address book and write some records into it
2. Read this address book
"""

book={}
book['tom']={
    'name':"tom",
    'address':'flat 4 block p',
    'phone no.': 3130422253
}

book['shaq']={
    'name':"shaq",
    'address':'flat 5 block p',
    'phone no.': 3189603270
}

import json
s=json.dumps(book)
with open("D:\Python\PyCharm Coding.txt","w") as f:
    f.write(s)

"""
you can now read  this JSON  data using  any language that supports JSOn such as Javascript,c++etc
Hence it is called data exchange format(i-e. exchanging data from python to javascript program)
"""

"""
go to idle and write the following code to read this dictionary
f=open("D:\Python\PyCharm Coding.txt","r")
s=f.read()
s
'{"tom": {"name": "tom", "address": "flat 4 block p", "phone no.": 3130422253}, "shaq": {"name": "shaq", "address": "flat 5 block p", "phone no.": 3189603270}}'

import json
book=json.loads(s)
book
{'tom': {'name': 'tom', 'address': 'flat 4 block p', 'phone no.': 3130422253}, 'shaq': {'name': 'shaq', 'address': 'flat 5 block p', 'phone no.': 3189603270}}
type(book)
<class 'dict'>
book["tom"]
{'name': 'tom', 'address': 'flat 4 block p', 'phone no.': 3130422253}
book["tom"]["phone no."]
3130422253
for person in book:
    print(book[person])

    
{'name': 'tom', 'address': 'flat 4 block p', 'phone no.': 3130422253}
{'name': 'shaq', 'address': 'flat 5 block p', 'phone no.': 3189603270}


"""