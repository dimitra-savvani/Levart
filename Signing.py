import datetime
from LevartSettings import LevartSettings
class Signing:
    
    def Register():
        j=True
        while j:
            reg = input ('Κάνε εγγραφή στη Levart \n 1-->ΝΑΙ \n 0-->ΟΧΙ \n Επίλεξε:')
            if reg == '1':
                k=True
                while k: # δημιουργουμε while μεχρι να δωσει αποδεκτο ονομα
                    typedΝame=input("Πληκτρολογείστε το όνομα σας:") #ζηταμε το νεο ονομα
                    for i in typedΝame:
                        if not typedΝame.isalpha(): #αν δεν δωσει αποδεκτο ονομα πρεπει να ξαναδωσει ονομα
                            print("Επιτρέπονται μόνο γράμματα στο όνομα σας." )
                            break
                        else: #αν δωσει σωστο ονομα προχωραμε
                            k=False
                            break
                k=True
                while k: # δημιουργουμε while μεχρι να δωσει αποδεκτο ονομα
                    typedSurname=input("Πληκτρολογείστε το επίθετο σας:") #ζηταμε το νεο ονομα
                    for i in typedSurname:
                        if not typedSurname.isalpha(): #αν δεν δωσει αποδεκτο ονομα πρεπει να ξαναδωσει ονομα
                            print("Επιτρέπονται μόνο γράμματα στο επίθετο σας." )
                            break
                        else: #αν δωσει σωστο ονομα προχωραμε
                            k=False
                            break
                k=True
                while k: # δημιουργουμε while μεχρι να δωσει αποδεκτο ονομα
                    typedUsername=input("Πληκτρολογείστε το όνομα χρήστη σας: ") #ζηταμε το νεο ονομα
                    for i in typedUsername:
                        if not typedUsername.isalpha(): #αν δεν δωσει αποδεκτο ονομα πρεπει να ξαναδωσει ονομα
                            print("Επιτρέπονται μόνο γράμματα στο όνομα χρήστη σας." )
                            break
                        else: #αν δωσει σωστο ονομα προχωραμε
                            k=False
                            break
                #it is acceptable only if is not taken from another user
                typedPassword1 = input("Πλήκτρολογήστε των κωδικό σας: ")
                typedPassword2 = input("Πλήκτρολογήστε των κωδικό σας ξανά: ")
                while typedPassword1 != typedPassword2:
                    print("Τα πεδία του κωδικού σας δεν ταιριάζουν, προσπαθηστε ξανα.")
                    typedPassword1 = input("Πλήκτρολογήστε των κωδικό σας: ")
                    typedPassword2 = input("Πλήκτρολογήστε των κωδικό σας ξανά: ")
                k=True
                while k:
                    try:
                        typedBirhtdate=input("Πληκτρολογείστε τα γενέθλια σας στην μορφή dd/mm/yyyy format: ")
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
                        
                print("Η εγγραφή σαν ήταν επιτυχής")
                t=LevartSettings
                t.Identification()  
                j=False 
                return [typedΝame, typedSurname, typedUsername, typedPassword2, typedBirhtdate, typedTelephone,typedEmail]
            
            elif reg=="0": 
                print("Δεν εγγραφήκατε στη Levart")
                s=Signing
                s.Login("mickeymouse",'1')
                
                j=False
                return ["Mickey","Mouse","mickeymouse","1","18/11/1928","2109989500","mickeymouse@upatras.com"]
                
                
            else:
                print("Επιλέξτε σωστά.")
        
        
    def Login(username, password):
        from sys import exit
        typedUsername = input("Πλήκτρολογήστε το όνομα χρήστη σας: ")
        typedPassword = input("Πλήκτρολογήστε των κωδικό σας: ")
        while not typedUsername == username or not typedPassword == password:
            print("Τα στοιχεία που δώσατε δεν αντιστοιχούν σε κάποιο λογαριασμό.")
            cancelLogin = input("Θέλετε να  αποχωρίσετε απο τη σελίδα του Login; y/n: ")
            if cancelLogin == 'y':
                exit(0)
            elif cancelLogin == 'n':
                typedUsername = input("Πλήκτρολογήστε το όνομα χρήστη σας: ")
                typedPassword = input("Πλήκτρολογήστε των κωδικό σας: ")
            else:
                print("Παρακαλώ επιλέξτε σωστά.")
        print("Επιτυχής σύνδεση λογαριασμού.")