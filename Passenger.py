from Traveler import Traveler
class Passenger(Traveler):
    import glob
    import sys
    
    
    #validinfo = False
    #petscounter = 0
    
    #startpoint = "Κορίνθου 17"
    
    #destination = ""
    
    #date = '12/12/20'
    
    #luggages = ["Σακίδιο πλάτης" , "Μικ΄ρη βαλίτσα" , "Μεσαία βαλίτσα" , "Μεγάλη βαλίτσα"]
    
    #pets = ["Ναι" , "Οχι"]
    
    #people = ["1" , "2" , "3" ,"4"]
    
    
    
    def __init__(self,startpoint,destination,date,luggages,pets,people):
       
        self.startpoint=startpoint
        self.destination=destination
        self.date=date
        self.luggages=luggages
        self.pets=pets
        self.people=people
       
    
    
    #Αυτή η μέθοδος θα δίνει τιμές στα πεδία της φόρμας.
    def FormFill(self):   
        import datetime
        
        print("Παρακαλώ συμπληρώστε τα στοιχεία της φόρμας")
        
        self.startpoint = input("Διάλεξε το σημείο εκκίνησης:")
        self.destination = input("Επέλεξε προοριμσό:")
        self.date=input("Πληκτρολογείστε την ημερομηνία έναρξης στην μορφή dd/mm/yyyy format: ")
        day, month, year = list(map(int,self.date.split("/")))
        self.date = datetime.date(year, month, day)
        
        while True :  
            self.pets = input("Δηλώστε την ύπαρξη κατοικηδίου με Ναι η Οχι: " )
            if self.pets == "Ναι" or self.pets == "Οχι":
               False
               break
            else:
                print("Παρακαλώ πληκτρολογήστε ορθά την απάντηση σας!")           
        
        while True :
            
            self.luggages = input("Επιλέξτε το μέγεθος των αποσκευών: \n Σακίδιο πλάτης , Μικρή βαλίτσα , Μεσαία βαλίτσα , Μεγάλη βαλίτσα:")
            if self.luggages == "Σακίδιο πλάτης" or self.luggages == "Μικρή βαλίτσα" or self.luggages == "Μεσαία βαλίτσα" or self.luggages == "Μεγάλη βαλίτσα":
                #if self.luggages == "Σακίδιο πλάτης":
                    #print("Παρακαλώ δηλώστε την ύπαρξη βαλίτσας εάν αυτή υπάρχει.")
                    #self.luggages=input("Παρακαλώ δηλώστε την ύπαρξη βαλίτσας εάν αυτή υπάρχει.\n Μικρή βαλίτσα , Μεσαία βαλίτσα , Μεγάλη βαλίτσα:")
                #else:
                    #self.luggages=input("Θα θέλατε θα έχετε μαζί σας και ένα Σακίδιο πλάτης:\n Ναι η Οχι")
                False
                break
            else :
              print("Παρακαλώ επιλέξτε ορθά το μέγεθος των αποσκευών! \n") 
              
        
        
        while True:
         self.people = input("Παρακαλώ πληκτρολογήστε τον αριθμό τον ατόμων που επιθυμείτε \n1 2 3 4:")
         if self.people >= "1" and self.people <= "4" :
            False
            break               
         else:
            print("Παρακαλώ πληκτρολογήστε έναν αριθμό απο το 1 μέχρι και το 4")
        # Μέθοδος που θα ελέγχει αν οι τύποι δεδομένων που συμπλήρωσε ο χρήστης είναι σωστοί.
    def PrintInfo(self):
        
        print("Σημείο εκκίνησης:\n" , self.startpoint ,"\n", "Προορισμός:\n", self.destination ,"\n", "Ημερομηνία:\n" , self.date ,"\n" , "Αποσκευές:\n" , self.luggages, "\n" , "Κατοικίδια:\n", self.pets ,"\n", "Άτομα:\n" , self.people ,"\n")
     
       # Μέθοδος  που θα εκτελεί αναζήτηση στην βάση με τις αναρτήσεις.
    def TravelSearch():
        
        print("tarvel")
       
             
    
   
f=Passenger("αθηνα" , "πατρα" , "12/5/20" , "Βαλιτσα" , "Ναι" , "4")    
f.FormFill()
f.PrintInfo()       
   
            
        
       
       
