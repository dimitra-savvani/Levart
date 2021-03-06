class PendingReservations():
    t = []
    review = str
    starReview = int
    count = 0 
    def __init__(self,afethria,proorismos,hmeromhnia,katoikidia,aposkeyes,atoma):
        self.afethria=afethria
        self.proorismos=proorismos
        self.hmeromhnia=hmeromhnia
        self.katoikidia=katoikidia
        self.aposkeyes=aposkeyes
        self.atoma=atoma
    def DisplayForm(*args): # μέθοδος που δέχεται αόριστο αριθμό από arguments τα αριθμοί και τα κάνει Print
        i=["Αφετηρία: ","Προορισμός: ","Ημερομηνία: ","Κατοικίδια: ","Αποσκευές: ","Άτομα: "]
        x=0
        for a in args[1:]:
            print(i[x],a)
            x+=1
        return args
    def Form(self):
        c=PendingReservations("Πάτρα","Αθήνα","12/12/2020","Ναι","Μεγάλη Βαλίτσα","3") 
        print("Τα ταξίδι σας είναι: \n")
        c.DisplayForm(self.afethria,self.proorismos,self.hmeromhnia,self.katoikidia,self.aposkeyes,self.atoma)
        k=True 
        while k:
            a=input("Εάν θέλετε να κάνετε ολοκλήρωση ταξιδιού πληκτρολογήστε το 1, για ακύρωση ταξιδιού πληκτρολογήστε το 2, για έξοδο πληκτρολογήστε 0 :\n")
            if a=="1":
                c.ReviewTraveler()
                c.CompleteReservation()
                k=False
            elif a=="2":
                c.DeleteReservation()
                c.InformTraveler()
                k=False
            elif a=="0":
                break
            else: 
                print("Διαλέξτε κάτι σύμφωνα με τις οδηγίες.")
    def ReviewTraveler(self):
        r=PendingReservations("Πάτρα","Αθήνα","12/12/2020","Ναι","Μεγάλη Βαλίτσα","3") 
        k=True
        while k:
            a=input("Εάν θέλετε να αξιογήσετε τον χρήστη που πραγματοποιήσατε το ταξίδι πατήστε 1, για ολοκλήρωση χωρίς αξιλόγηση πατήστε 0.")
            if a=="1":
                r.WriteReview()
                r.StarReview()
                k=False
            elif a=="0":
                k=False 
            else:
                print("Παρακαλώ επιλέξτε σύμφωνα με τις οδηγίες.")
                True
                
    def WriteReview(self):
        writtenReviews = []
        review=input("Παρακαλώ πληκτρολογήστε την αξιολόγηση σας για τον χρήστη που επιθυμείτε.")
        writtenReviews.append(review)
    def StarReview(self):
        starReviews=[]
        k=True
        while k:
            sreview=input("Παρακαλώ πληκτρολογήστε τα αστέρια σας για τον χρήστη που επιθυμείτε σε κλίμακα 1-10.")    
            try:
                int(sreview)
                if len(sreview)!=1 :
                    print("Η αξιολόγηση σας δεν μπορεί να είναι μικρότερη του 1 ή μεγαλύτερη του 10. Παρακαλώ προσπαθήστε ξανά.")
                    
                else:
                    starReviews.append(sreview)
                    print(sreview)
                    k=False
                        
            except ValueError:
                print("Επιτρέπονται μόνο αριθμοί στην αξιολόγηση σας.")
   
    def CompleteReservation(self): 
        c=PendingReservations
        c.t.append(self.afethria)
        c.t.append(self.proorismos)
        c.t.append(self.hmeromhnia)
        c.t.append(self.katoikidia)
        c.t.append(self.aposkeyes)
        self.afethria=None
        self.proorismos=None
        self.hmeromhnia=None
        self.katoikidia=None
        self.aposkeyes=None
        c.count+=1
        print("Το ταξίδι σας έχει ολοκληρωθεί και προστέθηκε στο πεδίο Ολοκληρωμένα ταξίδια.\n")
    def DeleteReservation(self):
        c=PendingReservations
        self.afethria=None
        self.proorismos=None
        self.hmeromhnia=None
        self.katoikidia=None
        self.aposkeyes=None
        c.count=0
    def InformTraveler(self):
        print("Ένα ταξίδι το οποίο συμμετείχατε έχει διαγραφεί. Για να δείτε τις λεπτομέριες πατήστε εδώ.\n")