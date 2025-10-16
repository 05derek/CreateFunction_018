luas = lambda jarijari : 3.14159 * jarijari**2

try :
    jari = float(input("Isikan nilai jari - jari : "))
    result = luas(jari)
    print = (f"Luas dari lingkarang dengan jari jari{jari} adalah {result}")
    
except ValueError :
    print ("Nilai jari-jari harus angka jawa")