#read from file
with open("mylist.txt") as f: 
  index = f.readline()
  rd = f.readlines()
print(rd)

#make list from file
items = []
for line in rd:
  items.append(line[:-1].split())
 
print(items)
print(items[1])
print(items[int(items[1][1])])

#save any updates into file
with open("mylist2.txt","w") as f: 
  f.write(format(items))


