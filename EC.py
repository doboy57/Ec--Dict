text = open("book of John text.txt","r")
r = dict()
for line in text:
    line = line.rstrip()

r = dict(Father = 0, God = 0, Christ = 0, Spirit = 0, spirit = 0,  life = 0, man = 0)
words = line.split(" ")
print(words)

for word in words:
    if word in r:
        r[word] = r[word] + 1
    
for key in list(r.keys()):
    print(key, ":", r[key])

