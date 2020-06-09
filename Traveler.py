from Signing import Signing
class Traveler:
    import sys
    L = Signing
    name, surname, username, password, birthdate, telephone, email = L.Register() 
    def __init__(self,name,surname,username,password,birthdate,telephone,email): # αντικαθήστα την βάση δεδομένων και μας βοήθα στο να δημιουργήσουμε default χρήστη και να επεξεργαζόμαστε τις μεταβλητές του
        self.name=name
        self.surname=surname
        self.username=username
        self.password=password
        self.birthdate=birthdate
        self.telephone=telephone
        self.email=email
        # profilePicture = cv2.imread('mickeyspicture.png')
        #enableTraveling = False
        
    def TravelerSettings(self):#μεθοδος που θα καλείτε απο την LevartSettings για την επεξεργασια του λογαριασμου
        l=Traveler#δημιουργουμε αντικείμενο με deault τιμες
        l.VerifyPassword(l)
        s=Signing
        #l.VerifyPassword() #κανουμε ελεγχο κωδικου προσβασης πριν μπορέσει να επεξεργαστη τα δεδομένα του
        k=True
        while k:   # δημιουργουμε while για να μπορει να επιλέξει οσες φορες θελει την EditInfo
                a=input("Για να επεξεργαστήτε το προφίλ σας πληκτολογήστε το 1, για να απενεργοποιήσετε τον λογαριασμό σας πληκτολογήστε το 2, για να διαγράψετε οριστικά τον λογαριασμό σας πληκτολογήστε το 3. Για έξοδο πληκτολογήστε το 0.")
                if a=="1":
                    l.EditInfo(l)
                elif a=="2":
                    l.DeactivateAccount(l) #Εφοσον κανει απενεργοποιησει μεταφέρεται στην Login για να κανει επαναφορα
                    s.Login(self.username,self.password)
                    k=False
                    break
                elif a=="3":
                    while True: #δημιουργουμε while σε περιπτωση που μετανιωσει την επιλογη διαγραφης
                        yn=input("Είστε σίγουρος ότι θέλετε να διαγράψετε όριστικά των λογαριασμό σας; Πλήκτρολογήστε y/n:")
                        if yn=="y":
                            l.DeleteAccount(l)#Εφοσον κανει διαγραφη μεταφέρεται στην Login (αρχικη οθονη)
                            s.Login(self.username,self.password)
                            False
                        elif yn=="n":
                          break  
                        else:
                            False
                            break
                elif a=="0":
                    k=False
                else:
                    print("Δεν επιλέξατε κάτι")
                    k=True
    def DisplayInfo(*args): # μέθοδος που δέχεται αόριστο αριθμό από arguments τα αριθμοί και τα κάνει Print
        i=1
        for a in args[1:]:
            print(i,a)
            i+=1
        return args  
    
    def VerifyPassword(self):#μέθοδος που επαλυθέυει τον κωδικό πρόσβασης και θα καλείτε πρίν την επεξεργασία του λογαριασμού
        from sys import exit #χρειαζόμαστε την exit ώστε να υπάρχει περιορισμένος αριθμός προσπαθείων
        i = 1
        while i <= 3:            # while για να έχει 3 προσπάθεις ο χρήστης
            enteredPassword = input("Παρακαλώ πληκτρολογήστε τον κωδικό χρήστη σας:") #κωδικός '1'
            if enteredPassword == (""): #διασφαλίζουμε ότι ο χρήστης έχει πληκτρολογήσει κάτι και δεν το προσμετράμε σαν προσπάθεια
                print("Δεν πληκτρολογίσατε κάτι. Παρακαλώ προσπαθήστε ξανά:")
            else:
                if (self.password == enteredPassword): #επαληθεύομυε αν ο κωδικος που προσέθεσε είναι αυτός που είναι αποθηκευμένος για τον χρήστη και επιτρέπει την πρόσβαση στις ρυθμίσεις
                    print("Καλωσήλθατε")
                    break  
                else:
                    if i<=2: # δινουμε στον χρήστη αλλες 2 προσπάθειες να πληκτρολογήσει τον κωδικό του
                        print("Λάθος κωδικός πρόσβασης. Έχετε", 3 - i, "προσπάθειες ακόμα.")
                    elif i==3: #εαν δώσει 3 φορες λανθασμένο κωδικο θα παρέχεται link ανάκτησης
                        print ("Πληκτρολόγησατε λάθος κωδικό 3 φορές. Έαν έχετε ξεχάσει τον κωδικό σας κάντε ανάκτηση πατώντας εδώ.")
                        exit(0)
                i += 1

    def EditInfo(self):
            import datetime #χρειαζομαστε την datetime για την ημερομηνια γέννησης
            T=Traveler("Mickey","Mouse","mickeymouse","1","18/11/1928","2109989500","mickeymouse@upatras.com") #δημιουργουμε αντικείμενο με deault τιμες
            T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email) # εμφανιζουμε στον χρήστη τα δεδομενα ως εχουν
            j=True 
            while j: #δημιουργουμε while για να επεξεργαζετε τα δεδομένα του όσες φορες επιθυμει ο χρήστης
                print("Διαλέξτε το στοιχείο που επιθυμείτε να επεξεργαστείτε διαλέγοντας τον αντίστοιχο αριθμό. Για έξοδο από την επεξεργασία δεδομένων πατήστε 0.")
                a=input() #επιλεγει τι θελει να επεξεργαστη
                if a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7" or a=="0": 
                    if a=="1":
                        k=True
                        while k: # δημιουργουμε while μεχρι να δωσει αποδεκτο ονομα
                            self.name=input("Πληκτρολογείστε το νέο σας όνομa:") #ζηταμε το νεο ονομα
                            for i in self.name:
                                if not self.name.isalpha(): #αν δεν δωσει αποδεκτο ονομα πρεπει να ξαναδωσει ονομα
                                    print("Επιτρέπονται μόνο γράμματα στο όνομα σας." )
                                    break
                                else: #αν δωσει σωστο ονομα προχωραμε
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email) # εμφανιζουμε στον χρήστη τα νεα δεδομενα 
                                    k=False
                                    break
                    elif a=="2":
                        k=True
                        while k: # δημιουργουμε while μεχρι να δωσει αποδεκτο επιθετο
                            self.surname=input("Πληκτρολογείστε το νέο σας επίθετο:")#ζηταμε το νεο επιθετο
                            for i in self.surname:
                                if not self.surname.isalpha(): #αν δεν δωσει αποδεκτο επιθετο πρεπει να ξαναδωσει επιθετο
                                    print("Επιτρέπονται μόνο γράμματα στο όνομα σας.")
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")#αν δωσει σωστο επιθετο προχωραμε
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email) # εμφανιζουμε στον χρήστη τα νεα δεδομενα 
                                    k=False
                                    break
                    elif a=="3":
                        k=True
                        while k:
                            self.username=input("Πληκτρολογείστε το νέο σας όνομa χρήστη:")
                            for i in self.username:
                                if not self.username.isalpha():
                                    print("Επιτρέπονται μόνο γράμματα στο όνομα χρήστη σας.")
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                                    k=False
                                    break  
                    elif a=="4":
                        k=True
                        while k:
                            self.password=input("Πληκτρολογείστε το νέο σας κωδικό:")
                            for i in self.password:
                                if i == ("")or i==(" "):
                                    print("Δεν επιτρέποτνται κένα στον κωδικό σας.")
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                                    k=False
                                    break
                    elif a=="5":
                        k=True
                        while k:
                            try:
                                self.birthdate=input("Πληκτρολογείστε τα νέa σας γενέθλια στην μορφή dd/mm/yyyy format: ") 
                                day, month, year = list(map(int,self.birthdate.split("/"))) #ελεγχουμε αν ο χρηστης εχει δωσει τα γενεθλια του σε σωστη μορφη
                                birthdate = datetime.date(year, month, day) #ελεγχουμε αν εχει δωσει σωστες τιμες
                                if year>1900 and year<2020: #βαζουμε περιορισμο στις χρονιες γεννησης
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                                    k=False
                                else:
                                    print("Η χρονία δεν μπορεί να είναι μικρότερη του 1900 και μεγαλύτερη του 2020. Προσπαθήστε ξανά.")
                                    k=True
                            except ValueError:
                                print("Η μορφή ημερομινίας που δώσατε δεν είναι αποδεκτή, παρακαλώ ακολουθήστε τις οδηγιές και προσπαθήστε ξανά.")
                    elif a=="6":
                        k=True
                        while k:
                            self.telephone=input("Πληκτρολογείστε το νέο σας τηλέφωνο:")
                            for i in self.telephone:
                                try:
                                    int(self.telephone)
                                    if len(self.telephone)!=10: #ελεγχουμε αν ο αριθμος τηλεφωνο είναι 10 ψηφιων
                                        print("Ο αριθμός τηλεφώνου σας δεν μπορεί να είναι μικρότερος ή μεγαλύτερος από δέκα ψηφία. Παρακαλώ προσπαθήστε ξανά.")
                                        break
                                    else:
                                        print("Τα νέα σας στοιχεία είναι:")
                                        T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                                        k=False
                                except ValueError:
                                    print("Επιτρέπονται μόνο αριθμοί στο τηλέφωνο σας.")
                                    break    
                    elif a=="7":
                        k=True
                        while k:
                            self.email=input("Πληκτρολογείστε το νέο σας email:")
                            for i in self.email:
                                if i == ("")or i==(" "):
                                    print("Δεν επιτρέποτνται κένα στο email σας.")
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                                    k=False
                                    
                        
                    elif a=="0":
                        print("Τα νέα σας στοιχεία είναι:")
                        T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                        break
                else:
                    print("Παρακαλώ πληκτολογήστε έναν αριθμό σύμφωνα με τις οδηγίες.")
                    j=True    
    
    def DeactivateAccount(self):
         d=Traveler("Mickey","Mouse","mickeymouse","1","18/11/1928","2109989500","mickeymouse@upatras.com")
         d.ReasonSelection()
         print("Ο λογαριασμός σας έχει απενεργοποιήθει προσωρινά. Για να ανακτήσετε τον λογαριασμό σας κάντε σύνδεση με τους όνομα χρήση σας και των κωδικό πρόσβασης σας.")        
    def DeleteAccount(self): #δημιουργουμε μεθοδο που διαγραφει τα στοιχεια του χρήστη
         self.name = None
         self.surname = None 
         self.username = None 
         self.password = None 
         self.birthdate = None 
         self.telephone = None 
         self.email = None 
         print("Ο λογαριασμός διεγράφή οριστικά.")
    def ReasonSelection(self): #μεθοδος που ζηταει τους λογους απενεργοποιησεις απο τον χρήστη
           k=True
           j=0
           k=1
           a=["Χρειάζομαι ένα διάλειμμα.","Δεν ξέρω από που να αρχίσω.","Δεν ενδιαφέρομαι για ταξίδια πλέον.", "Ανησυχώ για το απόρρητό μου.","Δεν μπορώ να βρω Travel Buddies.","Δημιούργησα άλλο λογαριασμό.","Άλλο."]
           
           for i in a[0:7]:
               print(k, a[j] )
               j+=1
               k+=1
           logos=input("Γιατί θέλετε να απενεργοποιήσετε τον λογαριασμό σας; Επιλέξτε τον αντίστοιχο αριθμό: ")   
           while k:
               if logos == "1" or logos == "2" or logos == "3" or logos == "4" or logos == "5" or logos == "6" :
                   print("Ελπίζουμε να σας ξαναδούμε σύντομα.")
                   k=False
               elif logos=="7":
                   allo=input("Παρακαλώ δώστε μια μικρή περιγραφ΄η του λόγου σας: ")
                   print(allo)
                   k=False
               else:
                   print("Παρακαλώ διαλέξτε σωστά σύμφωνα με τις οδηγιές")       
                   break
    def TravelDeletation(self):
        print("Ένα ταξίδι το οποίο συμμετείχατε έχει διαγραφεί. Για να δείτε τις λεπτομέριες πατήστε εδώ.")