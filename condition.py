#kondisi if adalah kondisi yang akan di eksekusi oleh program jika bernilai benar atau True
nilai = 9

if(nilai > 7):
    print("Selamat anda lulus")

if(nilai > 10):
    print("Selamat anda lulus")
else:
    print("nilai salah")

#sample penggunaan Elif Python
today = "Sabtu"

if(today == "Senin"):
    print("Saya akan kerja")
elif(today == "Selasa"):
    print("Saya akan kerja")
elif(today == "Rabu"):
    print("Saya akan kerja")
elif(today == "Kamis"):
    print("Saya akan kerja")
elif(today == "Jumat"):
    print("Saya akan kerja")
elif(today == "Sabtu"):
    print("Hari ini Sabtu")
elif(today == "Minggu"):
    print("Hari ini Libur")
