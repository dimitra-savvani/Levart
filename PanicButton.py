from Traveler import Traveler
class PanicButton: 
    #def __init__(self,certainpanictrigger):
        #self.certainpanictrigger=certainpanictrigger
    enablePanicButton: bool
    allowePictureCapture: bool
    allowLocationCapture: bool
    allowSendingMessage: bool
    emergencyContacts = [6996699669]
    activasionSignal = True
    
    def __init__(self,lat,lon,fwto):
        self.lat=lat
        self.lon=lon
        self.fwto=fwto
    def RequestPicture(self):
        self.fwto="Φωτογραφία"
    def RequestLocationCapture(self):
        #import requests
        #import json
        #send_url = 'http://freegeoip.net/json'
        #r = requests.get(send_url)
        #j = json.loads(r.text)
        #lat = j['latitude']
        #lon = j['longitude']
        self.lat="48.067906"
        self.lon="12.860655"
        return self.lat
    def RequestRightMessage(self,x,la,lo,fw):
        l=PanicButton
        l.ComposeSMS(x,la,lo,fw)       
    #Αυτή η μέθοδος δείχνει την λίστα με τους πιθανούς κινδύνους στον χρήστη.            
    def RequestDangerList(self):
        p=PanicButton("","","")
        print('\n Λίστα με πιθανούς κινδύνου')
        dangerlist = ["Δέχομαι σεξουαλική παρενόχληση" , "Έχω πέσει θύμα κλοπής" , "Ο συνταξιδιώτης μου με εγκατέληψε" , "Ο συνταξιδιώτης μου με πήγε σε διαφορετικό προορισμό απο τον κανονισμένο"]
        for i, j in enumerate(dangerlist):
            print(i+1, j)
        while True:
            try:
                pan = int(input ("Διαλέξτε τον κίνδυνο στον οποίο βρίσκεστε: Για έξοδο πληκτρολογήστε 0. "))
                if pan == 0:
                    print('Έπιλέξατε έξοδο απο την λίστα κινδύνου',"\n")
                    False
                    break
                elif pan==1 or pan==2 or pan==3 or pan==4 :
                    print('Ο κίνδυνος που επιλέξατε ειναι ο:',dangerlist[pan-1],"\n")
                    p.RequestPicture()
                    p.RequestLocationCapture()
                    p.RequestRightMessage(pan-1,self.lat,self.lon,self.fwto)
                    False
                    break
                else:
                    print("Παρακαλώ επιλέξτε σωστά.")
            except ValueError:
                print("Αυτό το πεδίο δέχετε μόνο αριθμούς.")
    def ComposeSMS(i,lat,lon,fwto):
        t=Traveler
        if i == 0:
            print( '\n Το όνομα μου είνα', t.name ,' και δέχομαι σεξουαλική παρενόχληση στο ταξίδι που εκτελώ! Παρακάτω παραθέτονται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !',lat,lon,fwto,"\n")
        elif i == 1:   
            print( '\n Το όνομα μου είναι',t.name,'  και έπεσα θύμα κλοπής στο ταξίδι που εκτελώ! Παρακάτω παρατίθενται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !',lat,lon,fwto,"\n")
        elif i == 2:   
           print( '\n Το όνομα μου είναι', t.name,' και ο συνταξηδιώτης μου με εγκατέληψε στο ταξίδι που εκτελώ! Παρακάτω παραθέτονται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !',lat,lon,fwto,"\n")
            
        elif i == 3: 
            print( '\n Το όνομα μου είναι', t.name,' και ο συνταξηδιώτης μου με παραπλάνησε και πάει σε διαφορετικό προορισμό απο τον προσκαθορισμένο στο ταξίδι που εκτελώ! Παρακάτω παραθέτονται πληροφορίες οι οποίες θα είναι χρήσιμες για την βοήθεια μου !',lat,lon,fwto,"\n")
        #dangerlist = ["1) Δέχομαι σεξουαλική παρενόχληση" , "2) Έχω πέσει θύμω κλοπής" , "3) Ο συνταξιδιώτης μου με εγκατέληψε" , "4) Ο συνταξιδιώτης μου με πήγε σε διαφορετικό προορισμό απο τον κανονισμένο"]
        
        #print (*dangerlist , sep = "\n")
            
# p=PanicButton("48.067906","12.860655","Φωτογραφία")
# p.RequestDangerList()
#p.RequestPicture()

          
                
            
