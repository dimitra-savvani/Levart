from myLevartSettings import LevartSettings
from Traveler import Traveler
import datetime
class Levart:
    L = LevartSettings()
    language = L.LanguageSettings()
    
    companyInfo = ['261094735', '261094756', 'levart@info.gr']
    
    def __init__(self, language): 
        self.language = language
       

    
    def Register():
        reg = int(input ('Κάνε εγγραφή στη Levart \n 0-->ΝΑΙ \n 1-->ΟΧΙ \n Επίλεξε:'))
        if reg == 1:
            typedΝame = input("Πλήκτρολογήστε το όνομα σας: ")
            typedSurname = input("Πλήκτρολογήστε το επίθετο σας: ")
            typedUsername = input("Πλήκτρολογήστε το όνομα χρήστη σας: ")
            #it is acceptable only if not taken from another user
            typedPassword1 = input("Πλήκτρολογήστε των κωδικό σας: ")
            typedPassword2 = input("Πλήκτρολογήστε των κωδικό σας ξανά: ")
            while typedPassword1 != typedPassword2:
                print("Τα πεδία του κωδικού σας δεν ταιριάζουν, προσπαθηστε ξανα.")
                typedPassword1 = input("Πλήκτρολογήστε των κωδικό σας: ")
                typedPassword2 = input("Πλήκτρολογήστε των κωδικό σας ξανά: ")
            k=True
            while k:
                try:
                    typedBirhtdate=input("Πληκτρολογείστε τα νέa σας γενέθλια στην μορφή dd/mm/yyyy format: ")
                    day, month, year = list(map(int, typedBirhtdate.split("/")))
                    typedBirhtdate = datetime.date(year, month, day)
                    if year>1900 and year<2020:
                        k=False
                    else:
                        print("Η χρονία δεν μπορεί να είναι μικρότερη του 1900 και μεγαλύτερη του 2020. Προσπαθήστε ξανά.")
                        k=True
                except ValueError:
                    print("Η μορφή ημερομινίας που δώσατε δεν είναι αποδεκτή, παρακαλώ ακολουθήστε τις οδηγιές και προσπαθήστε ξανά.")
            k=True
            while k:
                typedTelephone=input("Πληκτρολογείστε το τηλέφωνο σας:")
                for i in typedTelephone:
                    try:
                        int(typedTelephone)
                        if len(typedTelephone)!=10:
                            print("Ο αριθμός τηλεφώνου σας δεν μπορεί να είναι μικρότερος ή μεγαλύτερος από δέκα ψηφία. Παρακαλώ προσπαθήστε ξανά.")
                            break
                        else:
                            k=False
                    except ValueError:
                        print("Επιτρέπονται μόνο αριθμοί στο τηλέφωνο σας.")
                        break  
            k=True
            while k:
                typedEmail=input("Πληκτρολογείστε το νέο σας email:")
                for i in typedEmail:
                    if i == ("")or i==(" "):
                        print("Το στοιχείο",i,"δεν είναι επιτρεπτό. Δεν επιτρέποτνται κένα στο όνομα χρήστη σας.")
                        break
                    else:
                        k=False
                        break
        
        Registered = True
        return Registered 
        
    def Login():
        #Traveler(self.name, self.surname, self.username, self.password, self.birthdate, self.telephone, self.email)
        T = Traveler("Mickey","Mouse","m","1","18/11/1928","6969696969","mickeymouse@upatras.com")
        typedUsername = input("Πλήκτρολογήστε το όνομα χρήστη σας: ")
        typedPassword = input("Πλήκτρολογήστε των κωδικό σας: ")
        while not typedUsername == T.username or not typedPassword == T.password:
            print("Τα στοιχεία που δώσατε δεν αντιστοιχούν σε κάποιο λογαριασμό.")
            cancelLogin = input("Θέλετε να  αποχωρίσετε απο τη σελίδα του Loginq; y/n: ")
            if cancelLogin == 'y':
                return
            typedUsername = input("Πλήκτρολογήστε το όνομα χρήστη σας: ")
            typedPassword = input("Πλήκτρολογήστε των κωδικό σας: ")
        print("Επιτυχής σύνδεση λογαριασμού.")
        
    
    def ComposeSMS(): 
        text = 'some text'
        return text
    
    #def SendMessage(): 
        
    
    
    
    
        
        
        
    
    
    
    
    
   
    

        
