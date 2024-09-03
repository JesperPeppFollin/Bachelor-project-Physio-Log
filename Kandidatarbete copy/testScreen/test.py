class Test():
    #tesnames = ['Six minutes walking test', 'Hand strength test']

    def __init__(self):
        self.id = ''
        self.name = ''
        self.results = []
        self.float_results = []
        self.percent = []
        self.float_percent = []
        self.dates = []
        self.extract_dates = []

    def createResults(self, currPatient, id):
        self.id = id
        result = 0
        if id == 0:
            if currPatient.gender == 'Male':
                result = 7.57 * float(currPatient.height) - 5.02 * float(currPatient.age) - 1.76 * float(currPatient.weight) - 309
            else:
                result = 2.11 * float(currPatient.height) - 5.78 * float(currPatient.age) - 2.29 * float(currPatient.weight) + 667


        return result