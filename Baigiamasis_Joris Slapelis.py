#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sveiki atvykę į žaidimą "Klasikinės kartuvės"!

vardas = input("Įveskite savo vardą: ")
print("Labas, " + vardas, ".Pažaiskime klasikines kartuves!")

print("Taigi, koks yra tavo pirmas spėjimas?")

žodis = "vasara"
spėjimai = ''
bandymai = 10
while bandymai > 0:         
    klaida = 0             
    for x in žodis:      
        if x in spėjimai:    
          print(x)
        else:
            print("_")
        #Gavus klaidingą spėjimą, padidinti nepavykusių bandymų skaičių +1
            klaida += 1    
    #Jeigu teisingai, atspausdinti laimėjimą
    if klaida == 0:        
        print("Bravo! Tu laimėjai!")
        break              
    print()
    #Prašyti žaidėjo spėti raidę
    spėjimas = input("Atspėk raidę: ") 
    spėjimai += spėjimas                    

    if spėjimas not in žodis:  
     #Tada bandymų skaičius mažėja po -1
        bandymai -= 1        
        print("Klaidingas spėjimas")    
        print("Tu turi likusius", + bandymai, 'spėjimus')  
    #Jeigu liko nulis bandymų, žaidėjas išnaudojo visus 10 ėjimų
        if bandymai == 0:           
    
        #Atspausdinti pralaimėjimą
            print ("Tu pralaimėjai")


# In[ ]:




