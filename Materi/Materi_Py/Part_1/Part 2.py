#Deklarasi list
angka = [1, 2, 3, 4, 5]
nama_buah = ["apel", "pisang", "mangga"]
#Diatas adalah variabel untuk angka dan nama buah

print(angka, nama_buah)#Ini adalah kode untuk memanggil variabel ang dan nama buah
print(angka [0])#Ini adalah kode untuk memanggil isi variabel angka yaitu '1'
print(angka [1])#Ini adalah kode untuk memanggil isi variabel angka yaitu '2'

angka.append(6)  # Menambahkan elemen ke akhir list
angka.remove(3)  # Menghapus elemen dengan nilai 3
angka.sort()  # Mengurutkan list
print(angka) #Maka hasil pada output nanti adalah [1, 2, 4, 5, 6]