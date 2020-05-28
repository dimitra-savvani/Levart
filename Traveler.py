class Traveler:
    import glob
    import sys
    # import cv2
    name = "Mickey"
    surname = "Mouse"
    username = "mickeymouse"
    password = "1"
    birthdate = "18/11/1928"
    telephone = "6969696969"
    email = "mickeymouse@upatras.com"
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
        from sys import exit
        import datetime
        T=Traveler()
        T.DisplayInfo(self.name,self.surname,self.username,self.password,self.birthdate,self.telephone,self.email)
        n=self.name
        s=self.surname
        u=self.username
        p=self.password
        b=self.birthdate
        t=self.telephone
        e=self.email
        j=True
        while j:
            print("Διαλέξτε το στοιχείο που επιθυμείτε να επεξεργαστείτε διαλέγοντας τον αντίστοιχο αριθμό. Για έξοδο από την επεξεργασία δεδομένων πατήστε 0.")
            a=input()
            if a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7" or a=="0":
                if a=="1":
                    k=True
                    while k:
                        n=input("Πληκτρολογείστε το νέο σας όνομa:")
                        for i in n:
                            if not n.isalpha():
                                print("Επιτρέπονται μόνο γράμματα στο όνομα σας." )
                                break
                            else:
                                print("Τα νέα σας στοιχεία είναι:")
                                T.DisplayInfo(n,s,u,p,b,t,e)
                                k=False
                                break
                elif a=="2":
                    k=True
                    while k:
                        s=input("Πληκτρολογείστε το νέο σας επίθετο:")
                        for i in s:
                            if not s.isalpha():
                                print("Επιτρέπονται μόνο γράμματα στο όνομα σας.")
                                break
                            else:
                                print("Τα νέα σας στοιχεία είναι:")
                                T.DisplayInfo(n,s,u,p,b,t,e)
                                k=False
                                break
                elif a=="3":
                    k=True
                    while k:
                        u=input("Πληκτρολογείστε το νέο σας όνομa χρήστη:")
                        for i in u:
                            if not u.isalpha():
                                print("Επιτρέπονται μόνο γράμματα στο όνομα χρήστη σας.")
                                break
                            else:
                                print("Τα νέα σας στοιχεία είναι:")
                                T.DisplayInfo(n,s,u,p,b,t,e)
                                k=False
                                break  
                elif a=="4":
                    k=True
                    while k:
                        p=input("Πληκτρολογείστε το νέο σας κωδικό:")
                        for i in p:
                            if i == ("")or i==(" "):
                                print("Δεν επιτρέποτνται κένα στον κωδικό σας.")
                                break
                            else:
                                print("Τα νέα σας στοιχεία είναι:")
                                T.DisplayInfo(n,s,u,p,b,t,e)
                                k=False
                                break
                elif a=="5":
                    k=True
                    while k:
                        try:
                            b=input("Πληκτρολογείστε τα νέa σας γενέθλια στην μορφή dd/mm/yyyy format: ")
                            day, month, year = list(map(int,b.split("/")))
                            birthdate = datetime.date(year, month, day)
                            if year>1900 and year<2020:
                                print("Τα νέα σας στοιχεία είναι:")
                                T.DisplayInfo(n,s,u,p,b,t,e)
                                k=False
                            else:
                                print("Η χρονία δεν μπορεί να είναι μικρότερη του 1900 και μεγαλύτερη του 2020. Προσπαθήστε ξανά.")
                                k=True
                        except ValueError:
                            print("Η μορφή ημερομινίας που δώσατε δεν είναι αποδεκτή, παρακαλώ ακολουθήστε τις οδηγιές και προσπαθήστε ξανά.")
                elif a=="6":
                    k=True
                    while k:
                        t=input("Πληκτρολογείστε το νέο σας τηλέφωνο:")
                        for i in t:
                            try:
                                int(t)
                                if len(t)!=10:
                                    print("Ο αριθμός τηλεφώνου σας δεν μπορεί να είναι μικρότερος ή μεγαλύτερος από δέκα ψηφία. Παρακαλώ προσπαθήστε ξανά.")
                                    break
                                else:
                                    print("Τα νέα σας στοιχεία είναι:")
                                    T.DisplayInfo(n,s,u,p,b,t,e)
                                    k=False
                            except ValueError:
                                print("Επιτρέπονται μόνο αριθμοί στο τηλέφωνο σας.")
                                break    
                elif a=="7":
                    k=True
                    while k:
                        e=input("Πληκτρολογείστε το νέο σας email:")
                        for i in e:
                            if i == ("")or i==(" "):
                                print("Το στοιχείο",i,"δεν είναι επιτρεπτό. Δεν επιτρέποτνται κένα στο όνομα χρήστη σας.")
                                break
                            else:
                                print("Τα νέα σας στοιχεία είναι:")
                                T.DisplayInfo(n,s,u,p,b,t,e)
                                k=False
                                break
                    print(e)
                elif a=="0":
                    print("Τα νέα σας στοιχεία είναι:")
                    T.DisplayInfo(n,s,u,p,b,t,e)
                    exit()
            else:
                print("Παρακαλώ πληκτολογήστε έναν αριθμό σύμφωνα με τις οδηγίες.")
                j=True
xrhsths1=Traveler()             
xrhsths1.EnterPassword()
    #DisplayInfo(name,surname,username,password,birthdate,telephone,email)
xrhsths1.EditInfo()
    
    # def SelectPendingTravels():
    # def PasswordVerification():
    
    

    # def Delete Account():

    # def DeactivateAccount():

    # def ReasonSelection():

    # def PostReview():