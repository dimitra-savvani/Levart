import Levart
import PanicButton

class LevartSettings:
    
     
    
    def Identification(T):# with T being an object of class Traveler
        changePic = int(input ('Πρόσθεσε νέα φωτογραφία προφίλ \n 0-->ΝΑΙ \n 1-->ΟΧΙ \n Επίλεξε:'))    
        #upload eggrafo
        #elegxos
        #upload fwtografia
        #elgxos
        #suugrisi
        print('Επιτυχής ταυτοποίηση στοιχείων, μπορείτε πλέον να Ταξιδέψετε μέσω της Levart')
        T.enableTraveling = True
        return T.enableTraveling
    
    
    def PanicButtonSettings(P):# with P being an object of class PanicButton
         contactsList = [6983775649, 6947789379]
         enablePanicButton = True
         allowePictureCapture = True
         allowLocationCapture = True
         allowSendingMessage = True
         
    def LangugeSettings(L):# with L being an object of class Levart
        Languages = ['Greek', 'English', 'German', 'French', 'Russian']
        for i, j in enumerate(Languages):
            print(i, j)
        langIndex = int(input ("Διάλεξε Γλώσσα: "))
        while langIndex > i :
            langIndex = int(input ("Το νούμερο που διάλεξες δεν αντιστοιχεί σε διαθέσιμη γλώσσα, διάλεξε ξανά: "))
        print('Η γλώσσα τέθηκε σε',Languages[langIndex])
        L.languge = Languages[langIndex]
        return L.language
    

    def GeneralSettings(T):# with T being an object of class Traveler
        allowNotification = True
        
    def SecuritySettings(T):# with T being an object of class Traveler
        privateProfile = True
