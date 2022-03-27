import random
seviye=input("bir seviye seçiniz (kolay/orta/zor):").upper()

if seviye=="kolay":
    uret=random.randint(1, 10)
elif seviye=="orta":
    uret=random.randint(1, 50)
elif seviye=="zor":
    uret=random.randint(1, 100)
else:
    print("Lütfen doğru giriş yapınız")
while True:
  tahmin=int(input("tahminiz:"))
  if tahmin==uret:
     print("tebrikler, sayıyı buldunuz")
     break
  elif tahmin<uret:
    print("üzgünüm, sayınızı büyütün!")
  else:
    print("üzgünüm,sayınızı küçültün")
