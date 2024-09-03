class Patient():

    def __init__(self):
        self.id = 0
        self.name = ''
        self.age = 0
        self.weight = 0
        self.height = 0
        self.gender = ''
    
    def printData(self):
        print('Name: ', self.name, ', Age: ', self.age, ', Weight: ', self.weight, ', Gender: ', self.gender)