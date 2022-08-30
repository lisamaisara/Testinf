import random
#tekaan nombor proton
rahsia = random.randint(19,25)
teka = True
while teka:
    nombor = int(input("masukkan nombor proton tekaan anda(19,25):"))
    #ini input kita meneka nombor
    if nombor == rahsia:
        print ("tahniah tekaan anda tepat")
        teka = False
    elif nombor > rahsia:
        print ("nombor tekaan lebih daripada nombor sebenar")
    else:
        print ("nombor tekaan anda kurang daripada nombor sebenar")
        
def namaelemen():
    print("teka nama elemen")
    
    elemen= [
        "kalium",
        "kalsium",
        "skandium",
        "titanium",
        "vanadium",
        "kromium",
        "mangan"
        ]
        

    
    guess = None
    
    while elemen != guess:
        guess = str(input("masukkan nama elemen" ))
        if elemen == guess:
            print ("tahniah!!")
            guess = False
        else:
            print ("maaf anda salah")
    else:
        print ("jumpa lagi!!")
        
namaelemen()

