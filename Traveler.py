class Traveler:
    import glob
    import sys
    # import cv2
    def __init__(self,name,surname,username,password,birthdate,telephone,email):
        self.name=name
        self.surname=surname
        self.username=username
        self.password=password
        self.birthdate=birthdate
        self.telephone=telephone
        self.email=email
            # profilePicture = cv2.imread('mickeyspicture.png')
            #enableTraveling = False
            #travelBuddies = ['Donald Duck', 'Goofy']    
    def DisplayInfo(*args):
        i=1
        a=True
        for a in args[1:]:
            print(i,a)
            i+=1
        return args  
    def EnterPassword(self):
        from sys import exit
        i = 1
        while i <= 3:            
            enteredPassword = input("Παρακαλώ πληκτρολογήστε τον κωδικό χρήστη σας:")
            if enteredPassword == ("")or enteredPassword==(" ") or enteredPassword==("  ")or enteredPassword==("   ")or enteredPassword==("   ")or enteredPassword==("    "):
                print("Δεν πληκτρολογίσατε κάτι. Παρακαλώ προσπαθήστε ξανά:")
            else:
                if (self.password == enteredPassword):
                    print("Καλωσήλθατε")
                    break  
                else:
                    if i<=2:
                        print("Λάθος κωδικός πρόσβασης. Έχετε", 3 - i, "προσπάθειες ακόμα.")
                    elif i==3:
                        print ("Πληκτρολόγησατε λάθος κωδικό 3 φορές. Έαν έχετε ξεχάσει τον κωδικό σας κάντε ανάκτηση πατώντας εδώ.")
                        exit(0)
                i += 1

    def EditInfo(self):
            import datetime
            T=Traveler("Mickey","Mouse","mickeymouse","1","18/11/1928","6969696969","mickeymouse@upatras.com")
            T.DisplayInfo()
            j=True
            while j:
                print("Διαλέξτε το στοιχείο που επιθυμείτε να επεξεργαστείτε διαλέγοντας τον αντίστοιχο αριθμό. Για έξοδο από την επεξεργασία δεδομένων πατήστε 0.")
                a=input()
                if a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7" or a=="0":
                    if a=="1":
                        k=True
                        while k:
                            self.name=input("Πληκτρολογείστε το νέο σας όνομa:")
                            for i in self.name:
                                if not self.name.isalpha():
                                    print("Επιτρέπονται μόνο γράμματα στο όνομα σας." )
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                                    k=False
                                    break
                    elif a=="2":
                        k=True
                        while k:
                            self.surname=input("Πληκτρολογείστε το νέο σας επίθετο:")
                            for i in self.surname:
                                if not self.surname.isalpha():
                                    print("Επιτρέπονται μόνο γράμματα στο όνομα σας.")
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
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
                                self.birhtdate=input("Πληκτρολογείστε τα νέa σας γενέθλια στην μορφή dd/mm/yyyy format: ")
                                day, month, year = list(map(int,self.birhtdate.split("/")))
                                birthdate = datetime.date(year, month, day)
                                if year>1900 and year<2020:
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
                                    if len(self.telephone)!=10:
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
                                    print("Το στοιχείο",i,"δεν είναι επιτρεπτό. Δεν επιτρέποτνται κένα στο όνομα χρήστη σας.")
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                                    k=False
                                    break
                        
                    elif a=="0":
                        print("Τα νέα σας στοιχεία είναι:")
                        T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
                        break
                else:
                    print("Παρακαλώ πληκτολογήστε έναν αριθμό σύμφωνα με τις οδηγίες.")
                    j=True   
xrhsths1=Traveler("Mickey","Mouse","mickeymouse","1","18/11/1928","6969696969","mickeymouse@upatras.com")                
xrhsths1.EnterPassword()
    #DisplayInfo(name,surname,username,password,birthdate,telephone,email)
xrhsths1.EditInfo()
    
    # def SelectPendingTravels():
    # def PasswordVerification():
    
    

    # def Delete Account():

    # def DeactivateAccount():

    # def ReasonSelection():

    # def PostReview():