class Passenger():
    import glob
    import sys
    def __init__(self,startpoint,destination,date,luggages,pets,people):
        self.startpoint=startpoint #Σημείο έναρξης.
        self.destination=destination #Σημείο άφιξης.
        self.date=date #Ημερομηνία έναρξης ταξιδιού.
        self.luggages=luggages #Αποσκευές που θα έχει ο χρήστης.
        self.pets=pets #Κατοικίδια
        self.people=people #Άτομα που θα εκτελέσουν το ταξίδι.
    #Αυτή η μέθοδος θα δίνει τιμές στα πεδία της φόρμας.
    def FormFill(self):   
        import datetime
        
        print("Παρακαλώ συμπληρώστε τα στοιχεία της φόρμας")
        
        while True:
            self.startpoint = input("Διάλεξε το σημείο εκκίνησης:")
            if len(self.startpoint)!=0:
                False
                break
            else:
                print("Παρακαλώ πληκτρολογήστε κάτι")
        while True:
            self.destination = input("Διάλεξε το σημείο προορισμού:")
            if len(self.destination)!=0 and self.destination!=self.startpoint:
                False
                break
            else:
                print("Παρακαλώ πληκτρολογήστε κάτι. Προσοχή ο προορισμός δεν μπορεί να ίδιος με την αφετηρία.") 
        while True: #Έλεγχος ορθότητας ημερομηνιών. Δέχεται μόνο μεταγενέστερες ημερομηνίες απο την στιγμή που θα εκτελεστεί.
                            try:
                                self.date=input("Πληκτρολογείστε την ημερομηνία έναρξης στην μορφή dd/mm/yyyy: ") 
                                day, month, year = list(map(int,self.date.split("/"))) 
                                date = datetime.datetime(year, month, day) #ελεγχουμε αν εχει δωσει σωστες τιμες
                                x = datetime.datetime.now()
                                if  date >= x: 
                                    False
                                    break
                                else:
                                    print("Η χρονία δεν μπορεί να είναι μεγαλύτερη του 2020. Προσπαθήστε ξανά.")
                                    True
                            except ValueError:
                                print("Η μορφή ημερομινίας που δώσατε δεν είναι αποδεκτή, παρακαλώ ακολουθήστε τις οδηγιές και προσπαθήστε ξανά.")
        
        while True :  #Έλεγχος ορθότητας εισόδου ύπαρξης κατοικιδίων.
            self.pets = input("Δηλώστε την ύπαρξη κατοικηδίου με Ναι ή Οχι: " )
            if self.pets == "Ναι" or self.pets == "Οχι":
               False
               break
            else:
                print("Παρακαλώ πληκτρολογήστε ορθά την απάντηση σας!")           
        
        while True : #Έλέγχος ορθότητας εισόδου αποσκευών.
            
            self.luggages = input("Επιλέξτε το μέγεθος των αποσκευών: \n Σακίδιο πλάτης , Μικρή βαλίτσα , Μεσαία βαλίτσα , Μεγάλη βαλίτσα:")
            self.temp = self.luggages
            if self.luggages == "Σακίδιο πλάτης" or self.luggages == "Μικρή βαλίτσα" or self.luggages == "Μεσαία βαλίτσα" or self.luggages == "Μεγάλη βαλίτσα":
                False
                break
            else :
              print("Παρακαλώ επιλέξτε ορθά το μέγεθος των αποσκευών! \n") 
              
        
        
        while True: #Έλεγχος ορθότητας εισόδου αριθμού ατόμων.
         self.people = input("Παρακαλώ πληκτρολογήστε τον αριθμό τον ατόμων που επιθυμείτε \n1 2 3 4:")
         if self.people >= "1" and self.people <= "4" :
            False
            break               
         else:
            print("Παρακαλώ πληκτρολογήστε έναν αριθμό απο το 1 μέχρι και το 4")
            
            
        # Μέθοδος που εκτυπώνει τα αποτελέσματα των εισόδων.
    def PrintInfo(self):
        
        print("Σημείο εκκίνησης:" , self.startpoint ,"\n", "Προορισμός:", self.destination ,"\n", "Ημερομηνία:" , self.date ,"\n" , "Αποσκευές:" , self.luggages, "\n" , "Κατοικίδια:", self.pets ,"\n", "Άτομα:" , self.people ,"\n")
     
       # Μέθοδος  που θα εκτελεί αναζήτηση στην βάση με τις αναρτήσεις.
    def TravelSearch():
        
        print("tarvel")
       
             
    
   
# f=Passenger("αθηνα" , "πατρα" , "12/5/20" , "Βαλιτσα" , "Ναι" , "4" )    
# f.FormFill()
# f.PrintInfo()       
   
            
        
       
       
