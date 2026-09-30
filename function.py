def sapa():
    print("Halo, selamat datang di program ini!")
sapa()

def sapa(nama,kelas,umur):
    print("Halo, " + nama + "! Selamat datang di program ini!")
sapa("Budi")

nama = input("Masukkan nama Anda: ")
kelas = input("Masukkan kelas Anda: ")
umur = input("Masukkan umur Anda: ")
sapa(nama,kelas,umur)

#fungi untuk menghitung luas 
#persegi panjang dengan 2 parameter
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang adalah:", luas)
hitung_luas(5, 10)


def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas
hasil = hitung_luas(5, 10)
print("Luas persegi panjang adalah:", hasil)

def kali(a, b):
    return a * b
x =kali(4,5)
y=kali(x,2)
print(y)