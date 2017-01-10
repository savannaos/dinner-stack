#Savanna Smith 
#Dinner Stack
#Created: 1/6/2017
#Modified: 1/6/2017
import json

class DinnerStack:

  def __init__(self,fname):
    with open(fname,'r') as f: 
      self.items = json.load(f)
    if len(self.items) == 0: #file not initialized
      self.numItems = 0
      items[0] = 0
    else:
      self.numItems = len(self.items) -1 #first line has index we're on
    self.currIndex = self.items[0]

  def pushItem(self,newString):
  #adds item to front of list and arranges the overall order to accomodate
    newIndex = self.numItems+1
    self.items.append([newString,self.currIndex])
    if self.numItems != 0: 
      for i in range(1,self.numItems): 
        if self.items[i][1] == self.currIndex:
          self.items[i][1] = newIndex
          break
    self.currIndex = newIndex
    self.numItems+=1
    print(self.items[1:])

  def popItem(self):
  #pop the current index and set the current index to the next in the order
    if self.numItems == 0 or self.numItems == 1: return
    dinner = self.items[self.currIndex][0] 
    self.currIndex = self.items[self.currIndex][1]
    return dinner
  
  def peakItem(self):
  #look at current item but do not change current index yet
    if self.numItems == 0 or self.numItems == 1: return
    return self.items[self.currIndex][0] 
    
  def save(self,fname):
  #save updates in json file 
    self.items[0] = self.currIndex
    with open(fname,'w') as f:
      json.dump(self.items,f)

  def trialRun(self):
  #testing calls
    self.pushItem("rice")
    self.pushItem("burger")
    print(self.popItem())
    print(self.popItem())
    print(self.popItem())
    print(self.popItem())
    print(self.popItem())
    print(self.popItem())
    self.save('Jfile.txt')

#DinnerStack('Jfile.txt').trialRun()
print(DinnerStack('Jfile.txt').peakItem())
