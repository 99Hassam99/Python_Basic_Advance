# poem.txt contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in your python program and find out words with maximum occurance.

word_status={}

with open('poem.txt','r') as f:
    for line in f:
        words=line.split(' ')
        for word in words:
            if word in word_status:
                word_status[word]+=1
            else:
                word_status[word] = 1
print(word_status)

word_occurance = list(word_status.values())
max_count = max(word_occurance)
print(f"max occurance of any word is: {max_count}")

print('Words with maximum occurance are: ')
for word, count in word_status.items():
    if count==max_count:
        print(word)