#from Signing import Signing
from LevartSettings import LevartSettings
from Traveler import Traveler
from PanicButton import PanicButton
from Driver import Driver
from Passenger import Passenger
from PendingReservations import PendingReservations
class Levart:
    from sys import exit
    
    companyInfo = ['261094735', '261094756', 'levart@info.gr']
    L = LevartSettings
    T = Traveler
    Pa=PanicButton("48.067906","12.860655","Φωτογραφία")
    D=Driver("Aθήνα" , "Πάτρα" , "12/5/20" , "Μεγάλη Βαλίτσα" , "Ναι" , "4" )    
    P=Passenger("Aθήνα" , "Πάτρα" , "12/5/20" , "Μεγάλη Βαλίτσα" , "Ναι" , "4" )    
    Pe=PendingReservations("Πάτρα","Αθήνα","12/12/2020","Ναι","Μεγάλη Βαλίτσα","3") 
    k=True
    while k:
        print("Για να μπείτε στις ρυθμίσεις της εφαρμογής πληκτρολογήστε το 1, \n")
        print("Για να μπείτε στις ρυθμίσεις λογαριασμού πληκτρολογήστε το 2, \n")
        print("Για να κάνετε ανάρτηση ταξιδιού πληκτρολογήστε το 3, \n")
        print("Για να κάνετε αναζήτηση ταξιδιού πληκτρολογήστε το 4, \n")
        print("Για να κάνετε επεξεργασία των ταξιδιών που εκκρεμούν πληκτρολογήστε το 5, \n")
        print("Για να ενεργοποιήσετε το Panic Button πληκτρολογήστε το 6, \n")
        print("Για να κάνετε έξοδο από την Levart πληκτρολογήστε το 0.")
        
        e=input("Παρακαλώ επιλέξτε τι θέλετε να κάνετε:\n")
        if e=="1":
            L.LanguageSettings()
            False
        elif e=="2":
            T.TravelerSettings(T)
            False
        elif e=="3":
            D.FormFill()
            False
        elif e=="4":
            P.FormFill()
            False
        elif e=="5":
            Pe.Form()
            False
        elif e=="6":
            Pa.RequestDangerList()
            False
        elif e=="0":
            exit(0)
        else:
            print("Παρακαλώ επιλέξτε σύμφωνα με τις οδηγίες\n")        
            
     
l=Levart

    
    
    
    