import json

items = [1, ['grapes',3],['apples',1],['fish',2]]

with open("Jfile.txt", 'w') as f: 
  json.dump(items,f)

with open('Jfile.txt','r') as f:
  newList = json.load(f)

print(newList)
print(newList[2])
print(newList[2][0])
print(newList[newList[1][1]])
