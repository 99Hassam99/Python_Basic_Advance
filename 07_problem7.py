# Write a python function to remove a given word from a list ad strip it at the same
# time.

# this function will just remove a word from the list at any index

def remove_word(l,words):
    for items in l:
        l.remove(words)
        return l

l = ["Ahmad","Shaheer","Hassam","Hashir","a"]
print(remove_word(l,"a"))

# but if we want to remove a word as well as an (X) character anywhere in the list, we use strip funct
# example 2


def remove_word(l,words):
    n=[]
    for items in l:
        if not (items==words):
            n.append(items.strip(words))
    return n

l = ["ahmada","Shaheeraa","Hassama","Hashira","a","asma"]
print(remove_word(l,"a"))

# the strip function remove a specific word from the start and the end

