class Vehicle:
    optionFill= ['Τύπος αυτοκινήτου', 'Μάρκα αυτοκινήτου', 'Σασμάν', 'Καύσιμο', 'Κίνηση']
    f=999
    
    def VehicleForm(choice):
        vehicleType= ['Sedan', 'SUV', 'VAN', 'Pickup', 'HatchBack', 'Coupe', 'Cabriolet']
        vehicleBrand= ['Mercedes', 'BMW', 'Audi', 'Subaru', 'Suzuki', 'Toyota', 'Opel']
        transmissionType= ['Manual', 'Automatic']
        fuelType= ['Gas', 'Petroleum', 'Diesel', 'Electric']
        driveTrain= ['FWD', 'RWD', '4WD']
        
        if choice==0:
            a=999
            for i, j in enumerate(vehicleType):
                print(i, j)
            while a<0 or a> len(vehicleType)-1:
                try:
                    a = int(input ("Τύπος αυτοκινήτου: "))                                  ##Select vehicle type
                except:
                    print ("Choice doesnt exist, please try again! ")
                    print()    
            print(vehicleType[a])
            print()
                
        elif choice==1:
            b=999
            for i, j in enumerate(vehicleBrand):
                print(i, j)
            while b<0 or b> len(vehicleBrand)-1:
                try:
                    b = int(input ("Μάρκα αυτοκινήτου: "))                                  ##Select vehicle brand
                except:                
                    print ("Choice doesnt exist, please try again! ")
                    print()
            print(vehicleBrand[b])
            print()
            
        elif choice==2:
            c=999
            for i, j in enumerate(transmissionType):
                print(i, j)
            while c<0 or c> len(transmissionType)-1:
                try:
                    c = int(input ("Σασμάν: "))                                             ##Select transmission type
                except: 
                    print ("Choice doesnt exist, please try again! ")
                    print()              
            print(transmissionType[c])
            print()

                                
        elif choice==3:
            d=999
            for i, j in enumerate(fuelType):
                print(i, j)
            while d<0 or d> len(fuelType)-1: 
                try:
                    d = int(input ("Καύσιμο: "))                                            ##Select fuel type
                except:
                    print ("Choice doesnt exist, please try again! ")
                    print()
            print(fuelType[d])
            print()

                
        elif choice==4:
            e=999
            for i, j in enumerate(driveTrain):
                print(i, j)
            while e<0 or e> len(driveTrain)-1:
                try:
                    e = int(input ("Κίνηση: "))                                             ##Select drivetrain
                except:
                    print ("Choice doesnt exist, please try again! ")
                    print()
            print(driveTrain[e])
            print()
                
        else:
            print ("Choice doesnt exist, please try again! ","Choose between 0 and 4.")
    
    while f != 9:
        for k,l in enumerate(optionFill):
            print(k,l)
        try:
            f = int(input("Επιλογή πεδίου από 0 εως 4 αντίστοιχα: "))       
            VehicleForm(f)
        except:
            print("Λάθος επιλογή! Διάλεξε μεταξύ 0 και 4.")
            print()
