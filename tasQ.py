import os
import yaml

class TasQ():  
    
    def __init__(self, file_name):
        self.file_name = file_name
        
        if os.path.exists(self.file_name):
            self.importdata()

        else:
            self.short = [] # short term tasks
            self.long = []  # long term tasks
            self.complete = []
        
    def importdata(self):
        with open(self.file_name, 'r') as f:
            data_dict = yaml.safe_load(f)

            self.short = data_dict['short']
            self.long = data_dict['long']
            self.complete = data_dict['complete']

    def exportdata(self):
        data_dict = {
                    'short':self.short,
                    'long':self.long,
                    'complete':self.complete
                   }
        
        with open(self.file_name, 'w') as f:
            yaml.dump(data_dict, f)

    def insert(self, position, item, lterm='short'):
        if lterm == 'short':
            self.short.insert(position, item)

        elif lterm == 'long':
            self.long.insert(position, item)

        else:
            raise ValueError("2nd arg must either go to 'short' or 'long' list")

        self.exportdata()
    
    def append(self, item, lterm='short'):
        if lterm == 'short':
            self.short.append(item)

        elif lterm == 'long':
            self.long.append(item)

        else:
            raise ValueError("2nd arg must either go to 'short' or 'long' list")
        self.exportdata()

    def topdone(self, position=0, lterm='short'):
        if lterm == 'short':
            self.complete.append(self.short.pop(position))

        elif lterm == 'long':
            self.complete.append(self.long.pop(position))

        else:
            raise ValueError("2nd arg must either go to 'short' or 'long' list")
        self.exportdata()

    def topkick(self, position=1, lterm='short'):
        if lterm == 'short':
            task = self.short.pop(0)
            self.short.insert(position, task) 

        elif lterm == 'long':
            task = self.long.pop(0)
            self.short.insert(position, task) 

        else:
            raise ValueError("2nd arg must either go to 'short' or 'long' list")
        self.exportdata()

    def nextshort(self, count=5):
        print(self.short[:count])

    def nextlong(self, count=5):
        print(self.long[:count])

