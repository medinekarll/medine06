#kullanıcıdan verileri alarak dikdörtgen çevresini fonksiyon
# yaparak hesaplayınız

def çevre(a,b):
    return (a+b)*2
def alan(a,b):
    return(a*b)
a_kenar=int(input("a kenar:"))
b_kenar=int(input("b kenar:"))
print("dikdörtgen çevresi:",çevre(a_kenar,b_kenar))
print("dikdörtgen alanı:",alan(a_kenar,b_kenar))