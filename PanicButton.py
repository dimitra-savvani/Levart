from Levart import Levart
class PanicButton:
    
    
    
    #def __init__(self,certainpanictrigger):
        #self.certainpanictrigger=certainpanictrigger
    
    enablePanicButton: bool

    allowePictureCapture: bool

    allowLocationCapture: bool

    allowSendingMessage: bool

    emergencyContacts = [6996699669]
    
    activasionSignal = True
    
    def RequestPicture():
        print("Τραβήχτηκε φωτογραφία")
        
    def RequestLocationCapture():
        #import requests
        #import json
    
        #send_url = 'http://freegeoip.net/json'
        #r = requests.get(send_url)
        #j = json.loads(r.text)
        #lat = j['latitude']
        #lon = j['longitude']
        pass
        
            
    def RequestRightMessage(x):
        l=Levart
        txt = l.ComposeSMS(x)
        
        
        
        
        
    #Αυτή η μέθοδος δείχνει την λίστα με τους πιθανούς κινδύνους στον χρήστη.            
    def RequestDangerList(self):
        p=PanicButton
        print('\n Λίστα με πιθανούς κινδύνου')
        dangerlist = ["Δέχομαι σεξουαλική παρενόχληση" , "Έχω πέσει θύμα κλοπής" , "Ο συνταξιδιώτης μου με εγκατέληψε" , "Ο συνταξιδιώτης μου με πήγε σε διαφορετικό προορισμό απο τον κανονισμένο"]
        for i, j in enumerate(dangerlist):
            print(i, j)
        while True:
            try:
                langIndex = int(input ("Διαλέξτε τον κίνδυνο στον οποίο βρίσκεστε: "))
                while langIndex > i :
                    langIndex = int(input ("Το νούμερο που διάλεξες δεν αντιστοιχεί σε είδος κινδύνου, διάλεξε ξανά: "))
                if langIndex == i:
                    print('Έπιλέξατε έξοδο απο την λίστα κινδύνου')
                else:
                    print('Ο κίνδυνος που επιλέξατε ειναι ο:',dangerlist[langIndex])
                    p.RequestRightMessage(langIndex)
                break
            except ValueError:
                print("Αυτό το πεδίο δέχετε μόνο αριθμούς.")
        dangerlist = dangerlist[langIndex]
        return dangerlist
        
        #dangerlist = ["1) Δέχομαι σεξουαλική παρενόχληση" , "2) Έχω πέσει θύμω κλοπής" , "3) Ο συνταξιδιώτης μου με εγκατέληψε" , "4) Ο συνταξιδιώτης μου με πήγε σε διαφορετικό προορισμό απο τον κανονισμένο"]
        
        #print (*dangerlist , sep = "\n")
            
p=PanicButton() 
p.RequestDangerList() 
p.RequestRightMessage()
#p.RequestPicture()

          
                
            
