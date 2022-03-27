try:
    sayi1=int(input("bir sayı giriniz"))
    sayi2=int(input("bir sayı giriniz"))
    print("sayılarınızın bölümü:",sayi1/sayi2)
except ValueError:
    print("girdiğiniz değer int olmalı!")
except ZeroDivisionError:
    print("bir sayı 0'a bölünemez!")
