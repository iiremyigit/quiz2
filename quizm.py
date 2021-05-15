dosya = open("odev.txt","r")
for veri in dosya:
   veri = veri.replace("2","")
   veri = veri.replace("+","")
   veri = veri.replace("1","")
   veri = veri.replace("3","")
   veri = veri.replace("4","")
   veri = veri.replace("5","")
   veri = veri.replace("6","")
   veri = veri.replace("7","")
   veri = veri.replace("8","")
   veri = veri.replace("9","")
   veri = veri.replace("(","")
   veri = veri.replace(")","")
   veri = veri.replace("-","")
   veri = veri.replace("=","")
   veri = veri.replace("/","")
   veri = veri.replace("-","")
   veri = veri.replace("?","")
   print(veri)



