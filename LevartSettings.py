import Levart
#import PanicButton

class LevartSettings:
    
    
     
    ''' Needed procedure to verify user'''
    def Identification(T):# with T being an object of class Traveler
        changePic = int(input ('Πρόσθεσε νέα φωτογραφία προφίλ \n 1-->ΝΑΙ \n 0-->ΟΧΙ \n Επίλεξε:'))    
        #upload eggrafo
        #elegxos
        #upload fwtografia
        #elgxos
        #sugrisi
        print('Επιτυχής ταυτοποίηση στοιχείων, μπορείτε πλέον να Ταξιδέψετε μέσω της Levart')
        T.enableTraveling = True #if true, users are allowed to arrange travels through Levart
         
    
    
    def PanicButtonSettings(P):# with P being an object of class PanicButton
         P.emergencyContacts = [6983775649, 6947789379]
         P.enablePanicButton = True
         P.allowePictureCapture = True
         P.allowLocationCapture = True
         P.allowSendingMessage = True
         
    def LanguageSettings(self):# with L being an object of class Levart
        print('Διαλέξτε τη γλώσσα της επιλογής σας:')
        Languages = ['Greek', 'English', 'German', 'French', 'Russian','Έξοδος απο ρυθμίσεις γλώσσας']
        for i, j in enumerate(Languages):
            print(i, j)
        while True:
            try:
                langIndex = int(input ("Διάλεξε Γλώσσα: "))
                while langIndex > i :
                    langIndex = int(input ("Το νούμερο που διάλεξες δεν αντιστοιχεί σε διαθέσιμη γλώσσα, διάλεξε ξανά: "))
                if langIndex == i:
                    print('Έπιλέξατε έξοδο απο τις ρυθμίσεις γλώσσας')
                else:
                    print('Η γλώσσα τέθηκε σε',Languages[langIndex])
                break
            except ValueError:
                print("Αυτό το πεδίο δέχετε μόνο αριθμούς.")
        language = Languages[langIndex]
        
    

    def GeneralSettings(T):# with T being an object of class Traveler
        allowNotification = True
        
    def SecuritySettings(T):# with T being an object of class Traveler
        privateProfile = True
        
        
        
    

