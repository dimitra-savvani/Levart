class Passenger():
    import glob
    import sys
    
    
    validinfo = False
    
    startpoint = "Κορίνθου 17"
    
    destination = ""
    
    date = '12/12/20'
    
    luggages = ["Σακίδιο πλάτης" , "Μικ΄ρη βαλίτσα" , "Μεσαία βαλίτσα" , "Μεγάλη βαλίτσα" ]
    
    pets = ["Ναι" , "Οχι"]
    
    def __init__(self,validinfo,startpoint,destination,date,luggages,pets):
        self.validinfo=validinfo
        self.startpoint=startpoint
        self.destination=destination
        self.date,=date
        self.bluggages=luggages
        self.pets=pets
       
    
    
    #Αυτή η μέθοδος θα δίνει τιμές στα πεδία της φόρμας.
    def FormFill(startpoint , destination , date , luggages , pets):   
        from datetime import datetime
        self.startpoint = "Κορίνθου 17"
        print("Παρακαλώ συμπληρώστε τα στοιχεία της φόρμας")
        
        self.startpoint = input("Διάλεξε το σημείο εκκίνησης:")
        self.destination = input("Επέλεξε προοριμσό:")
        self.date_object = datetime.strptime('12/12/12', '%m/%d/%y')
        print(date_object)
        
        pets = input("Δηλώσε την ύπαρξη κατοικηδίου:" , pets)
        
        if pets == "Ναι" or pets == "Οχι":
                pass
        else:
                pets = input("Δηλώσε την ύπαρξη κατοικηδίου:" , pets)
        
        for x in luggages:
            print("Επέλεξε το μέγεθος των αποσκευών" , x)
            luggages = input()
        
      # Μέθοδος που ζητάει καινούρια δεδομένα.
    def RequestNewInfo():
        
         print("You have an error please fill the info")
         
       # Μέθοδος που θα ελέγχει αν οι τύποι δεδομένων που συμπλήρωσε ο χρήστης είναι σωστοί.
    def DataCheck():
       
       print("DataCheck")
     
       # Μέθοδος  που θα εκτελεί αναζήτηση στην βάση με τις αναρτήσεις.
    def TravelSearch():
       
       print("tarvel")
    
   
    
    FormFill("δσαδσα" , '"δσαδασ' , 22/12/1996 ,"δσαδσα" , "δσαδσασδα")
       
   
            
        
       
       
