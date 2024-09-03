import sqlite3
import datetime
class Database():
  def createDatabase(self):
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()
    #cursor.execute('''DROP TABLE IF EXISTS Patients''')
    #cursor.execute('''DROP TABLE IF EXISTS Tests''')

    patient_table = '''CREATE TABLE IF NOT EXISTS Patients
      (
        PatientsID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, -- primary key column
        PatientNamn NVARCHAR(50) NOT NULL,
        Ålder INT NOT NULL,
        Vikt INT NOT NULL,
        Höjd INT NOT NULL,
        Kön NVARCHAR(10) NOT NULL, 
        LastOpened [Date] NOT NULL
      );'''
    test_table = '''CREATE TABLE IF NOT EXISTS Tests
      (
        Num INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,-- primary key column
        TestID INT NOT NULL, 
        PatientsID INT NOT NULL,
        TestDate [Date] NOT NULL,
        Result [REAL] NOT NULL, 
        Percent [REAL] NOT NULL
      );'''
    cursor.execute(patient_table)
    cursor.execute(test_table)
    sqliteConnection.commit()
    
    cursor.close()
    sqliteConnection.close()


  def newPatient(self,currPatient):
    from datetime import date
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()
    patient_query = '''INSERT INTO Patients (PatientNamn, Ålder, Vikt, Höjd, Kön, LastOpened)
                    VALUES ('''+"'"+currPatient.name+"'"+','+str(currPatient.age)+','+str(currPatient.weight)+','+str(currPatient.height)+','+"'"+currPatient.gender+"'"','+"'"+str(date.today())+"'"+')'
    cursor.execute(patient_query)
    sqliteConnection.commit()
    cursor.execute('SELECT PatientsID FROM Patients ORDER BY PatientsID DESC LIMIT 1; ')
    currPatient.id = cursor.fetchone()[0]

    cursor.close()
    sqliteConnection.close()

    
  # def newTest(self,currPatient,test,result,percent):
  #   from datetime import date
  #   sqliteConnection = sqlite3.connect('Database.db')
  #   cursor = sqliteConnection.cursor()
    
  #   test_query = '''INSERT INTO Tests (TestID, PatientsID, TestDate, Result, Percent)
  #               VALUES ('''+str(test.id)+','+str(currPatient.id)+','+"'"+str(date.today())+"'"+','+str(result)+','+str(percent)+')'
  #   cursor.execute(test_query)
  #   sqliteConnection.commit()

  #   cursor.close()
  #   sqliteConnection.close()

  def newTest(self, currPatient, test, result, percent):
    from datetime import date
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()

    test_query = '''INSERT INTO Tests (TestID, PatientsID, TestDate, Result, Percent)
                VALUES (?, ?, ?, ?, ?)'''
    cursor.execute(test_query, (test.id, currPatient.id, date.today(), result, percent))
    sqliteConnection.commit()

    cursor.close()
    sqliteConnection.close()



  def oldPatient(self, currPatient,id):
    from datetime import date
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()

    currPatient.id = id
    cursor.execute('SELECT PatientNamn From Patients WHERE PatientsID = '+str(id))
    currPatient.name = cursor.fetchone()[0]
    cursor.execute('SELECT Ålder From Patients WHERE PatientsID = '+str(id))
    currPatient.age = cursor.fetchone()[0]
    cursor.execute('SELECT Vikt From Patients WHERE PatientsID = '+str(id))
    currPatient.weight = cursor.fetchone()[0]
    cursor.execute('SELECT Höjd From Patients WHERE PatientsID = '+str(id))
    currPatient.height = cursor.fetchone()[0]
    cursor.execute('SELECT Kön From Patients WHERE PatientsID = '+str(id))
    currPatient.gender = cursor.fetchone()[0]

    cursor.execute("UPDATE Patients SET LastOpened = ? WHERE PatientsID = ?", (date.today(), id))
    sqliteConnection.commit()

    cursor.close()
    sqliteConnection.close()

  def editPatient(self,currPatient):
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()
    patient_query = '''UPDATE Patients SET 
                   PatientNamn = ?, 
                   Ålder = ?, 
                   Vikt = ?, 
                   Höjd = ?, 
                   Kön = ?
                   WHERE PatientsID = ?'''

  # Define the parameters to pass to the query
    params = (currPatient.name, currPatient.age, currPatient.weight, currPatient.height, currPatient.gender, currPatient.id)

  # Execute the query
    cursor.execute(patient_query, params)
    sqliteConnection.commit()

    cursor.close()  
    sqliteConnection.close()
  

  def getResults(self, currPatient, test):
    import datetime
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()

    cursor.execute('SELECT Result From Tests WHERE PatientsID = '+str(currPatient.id) +' AND TestID = '+str(test.id)+' ORDER BY TestDate')
    test.results = cursor.fetchall()
    test.float_results = [float(result[0]) for result in test.results]

    cursor.execute('SELECT TestDate From Tests WHERE PatientsID = '+str(currPatient.id) +' AND TestID = '+str(test.id)+' ORDER BY TestDate')
    test.dates = cursor.fetchall()
    test.extract_dates =[datetime.datetime.strptime(date[0], '%Y-%m-%d').date() for date in test.dates]

    cursor.close()
    sqliteConnection.close()

  def getPercent(self, currPatient, test):
    import datetime
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()



    cursor.execute('SELECT Percent From Tests WHERE PatientsID = '+str(currPatient.id) +' AND TestID = '+str(test.id)+' ORDER BY TestDate')
    test.percent = cursor.fetchall()
    test.float_percent = [float(percent[0]) for percent in test.percent]

    cursor.execute('SELECT TestDate From Tests WHERE PatientsID = '+str(currPatient.id) +' AND TestID = '+str(test.id)+' ORDER BY TestDate')
    test.dates = cursor.fetchall()
    test.extract_dates =[datetime.datetime.strptime(date[0], '%Y-%m-%d').date() for date in test.dates]

    cursor.close()
    sqliteConnection.close()

  def getAllPatients(self):
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()
    # Execute the query to check if the table exists
    cursor.execute("SELECT COUNT(*) FROM Patients")
    count = cursor.fetchone()[0]

    list = []
    if count !=0:
      cursor.execute('SELECT PatientsID FROM Patients ORDER BY PatientsID DESC LIMIT 1; ')
      last = cursor.fetchone()[0]

      for i in range(0, last):
          nameQuery = 'SELECT PatientNamn FROM Patients WHERE PatientsID = '+str(last-i)
          dateQuery = 'SELECT LastOpened FROM Patients WHERE PatientsID = '+str(last-i)+' ORDER BY LastOpened DESC LIMIT 1'

          cursor.execute(nameQuery)
          name = cursor.fetchone()[0]
          cursor.execute(dateQuery)
          date = cursor.fetchone()[0]

          # Convert the date value to a string in the format 'DD/MM-YY'
          date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%y')

          list.append(name+': '+date)
    cursor.close()
    sqliteConnection.close()
    return list



  def showDatabase(self):
    sqliteConnection = sqlite3.connect('Database.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('SELECT * FROM Patients')
    print(cursor.fetchall())
    cursor.execute('SELECT * FROM Tests')
    print(cursor.fetchall())

    cursor.close()
    sqliteConnection.close()
