class Kume(list):
     elemanlar = []
     def __init__(self, liste):
         for eleman in liste:
             if eleman not in self.elemanlar:
                 self.elemanlar.append(eleman)

a_kumesi = Kume([10,10,20,30])
print(a_kumesi.elemanlar)
