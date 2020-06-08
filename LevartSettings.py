from myLevartSettings import LevartSettings



class Levart:
    L = LevartSettings()
    language = L.LanguageSettings()
    
    companyInfo = ['261094735', '261094756', 'levart@info.gr']
    
    def __init__(self, language): 
        self.language = language
        self.travelCount = 0 #plithos taksidiwn pou exei pragmatatopoiisei o xristis

    
    
    def ComposeSMS(i):
        
        if i == 0:
            text = 'I am in danger 0'
        elif i == 1:   
            text = 'I am in danger 1'
        elif i == 2:   
            text = 'I am in danger 2'
        else:   
            text = 'I am in danger 3'
        return text
    
    #def SendMessage(): 
        
  
   
    
    
    
   
    

        
