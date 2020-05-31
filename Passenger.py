from AggelosGit import Traveler
class Passenger(Traveler):
    import glob
    import sys
    
    
    #validinfo = False
    
    startpoint = "Κορίνθου 17"
    
    destination = ""
    
    date = '12/12/20'
    
    luggages = ["Σακίδιο πλάτης" , "Μικ΄ρη βαλίτσα" , "Μεσαία βαλίτσα" , "Μεγάλη βαλίτσα"]
    
    pets = ["Ναι" , "Οχι"]
    
    people = ["1" , "2"]
    
    def __init__(self,startpoint,destination,date,luggages,pets):
       
        self.startpoint=startpoint
        self.destination=destination
        self.date=date
        self.luggages=luggages
        self.pets=pets
       
    
    
    #Αυτή η μέθοδος θα δίνει τιμές στα πεδία της φόρμας.
    def FormFill(self):   
        import datetime
        self.startpoint = "Κορίνθου 17"
        print("Παρακαλώ συμπληρώστε τα στοιχεία της φόρμας")
        
        self.startpoint = input("Διάλεξε το σημείο εκκίνησης:")
        self.destination = input("Επέλεξε προοριμσό:")
        self.date=input("Πληκτρολογείστε την ημερομηνία έναρξης στην μορφή dd/mm/yyyy format: ")
        day, month, year = list(map(int,self.date.split("/")))
        self.date = datetime.date(year, month, day)
        
        self.pets = input("Δηλώσε την ύπαρξη κατοικηδίου:" )
        
        if self.pets == "Ναι" or self.pets == "Οχι":
                pass
        else:
                self.pets = input("Δηλώσε την ύπαρξη κατοικηδίου με Ναι η Οχι:")
        
       
            
        self.luggages = input("Επέλεξε το μέγεθος των αποσκευών: \n Σακίδιο πλάτης , Μικρή βαλίτσα , Μεσαία βαλίτσα , Μεγάλη βαλίτσα:")
        
         
       # Μέθοδος που θα ελέγχει αν οι τύποι δεδομένων που συμπλήρωσε ο χρήστης είναι σωστοί.
    def DataCheck():
       
       print("DataCheck")
     
       # Μέθοδος  που θα εκτελεί αναζήτηση στην βάση με τις αναρτήσεις.
    def TravelSearch():
       
       print("tarvel")
    
   
f=Passenger("αθηνα" , "πατρα" , "12/5/20" , "Βαλιτσα" , "Ναι")    
f.FormFill()
       
   
            
        
       
       
       
   
            
        
       
       
       
