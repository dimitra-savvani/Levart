class Vehicle:
    vehicleType= ['Sedan', 'SUV', 'VAN', 'Pickup', 'HatchBack', 'Coupe', 'Cabriolet']
    vehicleBrand= ['Mercedes', 'BMW', 'Audi', 'Subaru', 'Suzuki', 'Toyota', 'Opel']
    transmissionType= ['Manual', 'Automatic']
    fuelType= ['Gas', 'Petroleum', 'Diesel', 'Electric']
    driveTrain= ['FWD', 'RWD', '4WD']

    for i, j in enumerate(vehicleType):
        print(i, j)
        
    a = int(input ("Τύπος αυτοκινήτου: "))
    print(vehicleType[a])
    print()
    
    for i, j in enumerate(vehicleBrand):
        print(i, j)
        
    b = int(input ("Μάρκα αυτοκινήτου: "))
    print(vehicleBrand[b])
    print()
        
    for i, j in enumerate(transmissionType):
        print(i, j)
        
    c = int(input ("Σασμάν: "))
    print(transmissionType[c])
    print()
        
    for i, j in enumerate(fuelType):
        print(i, j)
        
    d = int(input ("Καύσιμο: "))
    print(fuelType[d])
    print()
        
    for i, j in enumerate(driveTrain):
        print(i, j)
    
    e = int(input ("Κίνηση: "))
    print(driveTrain[e])
    print()
        
   ##def FormFill():
      
   ##def DataCheck():
   ##return
