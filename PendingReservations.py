from Passenger import Passenger
class PendingReservations(Passenger):
    
    travelList = []
    review = str
    starReview =  int
    
    def __init__(self,afethria,proorismos,hmerominia,wra,atoma,aposkeyes,katoikidia):
        self.afethria=Passenger.startpoint
        self.proorismos=Passenger.destination
        self.hmerominia=Passenger.date
        self.wra= wra
        self.atoma= atoma
        self.aposkeyes=Passenger.luggages
        self.katoikidia=Passenger.pets
    def DisplayForm(*args): # μέθοδος που δέχεται αόριστο αριθμό από arguments τα αριθμοί και τα κάνει Print
        i=1
        for a in args[1:]:
            print(i,a)
            i+=1
        return args  
        
    def Form(self):
        c=PendingReservations("patra","athina","5555","4","atoma","4","nai")
        p=Passenger()
        c.DisplayForm(self.afethria)
        Passenger.FormFill()
        k=True 
        while k:
            a=input("Εάν θέλετε να κάνετε ολοκλήρωση ταξιδιού πληκτρολογήστε το 1, για ακύρωση ταξιδιού πληκτρολογήστε το 2, για έξοδο πληκτρολογήστε 0 :")
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
        r=PendingReservations(self.afethria,self.proorismos,self.hmerominia,self.wra,self.atoma,self.aposkeyes,self.katoikidia)
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
   
    def CompleteReservation():  
                   
   #def DeleteReservation():
        
   # def InformTraveler():
   

        
print(Passenger.startpoint)
p=PendingReservations("afethria", "proorismos", "hmerominia", "wra", "atoma", "aposkeyes", "katoikidia")
p.Form()
#p.ReviewTraveler()
  
        

    