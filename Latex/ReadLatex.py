import os

fileList=["Bolum_0_Dogrusal_Cebir","Bolum_1_Dogrusal_Programlamada_Modelleme",
          "Bolum_2_Simplex",
"Bolum_4_Diger_Cozum_Yontemleri",
"Bolum_3_Duality_ve_Duyarlilik_Analizleri",
"Bolum_5_Amac_Programlama",
"Bolum_FractalProgramlama",
"Bolum_6_Tamsayili_Programlama",
"Bolum_7_Tasima_ve_atama_Problemleri"
"Bolum_8_Ag_ve_Akis_Problemleri",
"Bolum_TSP"]

for i in fileList:
    f=open("D://Kitap//YA//"+i+".tex", "r")
    print(i)
    while True:
        try:
            xx=f.readline()
        except:
            break
        if (xx.lstrip().rstrip()=="\end {exmp}"):
            print(xx)
