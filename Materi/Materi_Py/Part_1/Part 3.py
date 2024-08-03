#Loop
for i in range(1, 6):
    print(i)    #Pada bagian ini nantinya akan menampilkan angka 1-5, karena pada jarak kita hanya memberikan 1-6, dan yang tampil hanya 1-5

#While Loop
i = 1
while i <= 6:
    print(i)
    i += 1  #Pada bagian ini nantinya akan menampilkan angka 1-6, karena kita telah mendeklarasikan i=1 dan ketika i kecil sama
            #-> dengan 6, maka nantinya pada outputnya akan menampilkan angka 1-6

#Fungsi sapa menggunakan variabel nama
nama = "ZAKI"
def sapa(nama): #def adalah keyword yang digunakan untuk mendefinisikan sebuah fungsi. Sapa adalah nama fungsi yang didefinisikan. Nama adalah parameter yang diterima oleh fungsi tersebut.
    print(f"Halo, {nama}!")

sapa(nama)  # Memanggil fungsi sapa

#Juga bisa seperti ini
def sapa(nama):
    print(f"Halo, {nama}!")

sapa("ZAKI")  # Memanggil fungsi sapa