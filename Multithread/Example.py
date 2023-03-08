import threading

def Yaz():
    for i in "alibabanın bir çiftliği var çiftliğinde inekleri var":
        print(i)

def Say():
    for i in range(1,100):
        print(i)

print(" Yaz fonksiyonu adresi : ",Yaz)
print(" Say fonksiyonu adresi : ",Say)
# Yaz ve Say fonksiyonları sıralı çalıştırılıyor.
# Bu kullanımın thread ile bir ilgisi yok.
# Ardışık çalışan fonksiyonlar bir birlerini kesmiyorlar.
Yaz()
Say()

print(" Thread işletimi başlıyor  ")
t1 = threading.Thread(target=Yaz)
t2 = threading.Thread(target=Say)
t1.start()
t2.start()
t1.join()
t2.join()

print("************")


