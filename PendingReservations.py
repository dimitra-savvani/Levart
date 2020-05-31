class PendingReservations:
    travelList = []
    review = str
    starReview =  int
    def __init__(self,afethria,proorismos,hmerominia,wra,atoma,aposkeyes,katoikidia):
        self.afethria=afethria
        self.proorismos=proorismos
        self.hmerominia=hmerominia
        self.wra= wra
        self.atoma= atoma
        self.aposkeyes=aposekyes
        self.katoikidia=katoikia
    def DisplayForm(*args): # μέθοδος που δέχεται αόριστο αριθμό από arguments τα αριθμοί και τα κάνει Print
        i=1
        for a in args[1:]:
            print(i,a)
            i+=1
        return args  
        
    def Form():
        c=Traveler(self.afethria,self.proorismos,self.hmerominia,self.wra,self.atoma,self.aposkeyes,self.katoikidia)
        from Driver import *
        from Passenger import *
        self.afethria=d.startpoint
        self.proorismos=d.destination
        self.hmerominia=d.date
        self.wra= d.time
        self.aposkeyes=d.luggages
        self.atoma= d.people
        self.katoikidia=d.pets 
        c.DisplayForm()
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
    def ReviewTraveler():
        //
    def WriteReview():
        //
    def StarReview():
        //
    def DeleteReservation():
        //
    def InformTraveler():
        //

    def CompleteReservation():
        //

    