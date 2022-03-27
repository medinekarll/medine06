import os
try:
    os.mkdir("elma")
except FileExistsError:
    print("aynı isimle dosyan var"!)

  