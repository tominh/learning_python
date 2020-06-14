# lists juga dikatakan sebagai array, sifatnya mirip dengan string dan memang defaultnya string
# lists atau array memiliki index, dan isinya bisa bertipe integer, float atau string
a = [1, 2, 3, '4', 5, 6.2]
print(a)  # melihat isi lists atau array a

"""
index lists atau array diawali dari 0 dan integer
untuk mengakses indexnya menggunakan sintax => namavariabel[indexnya], indexnya tidak bisa melebihi isi lists atau arraynya
dari variabel a
index 0 = 1 = index -6
index 1 = 2 = index -5
index 2 = 3 = index -4
index 3 = 4 = index -3
index 4 = 5 = index -2
index 5 = 6 = index -1
"""
print("index 0 =", a[0], "index -6 =", a[-6])
print("index 1 =", a[1], "index -5 =", a[-5])
print("index 2 =", a[2], "index -4 =", a[-4])
print("index 3 =", a[3], "index -3 =", a[-3])
print("index 4 =", a[4], "index -2 =", a[-2])
print("index 5 =", a[5], "index -1 =", a[-1])
"""
contoh pengaksesan yang akan terjadi Traceback karena isi lists atau arraynya hanya sampai index 5
print("index 10 =", a[10])
"""

# untuk mengakses karakter lists atau array dengan batas tertentu menggunakan sintaks berikut
# namavariabel[indexbatasawal:indexbatasakhir]
# penjelasan yang diakses dari batasawal sampai sebelum batasakhir
print(a[0:2])  # artinya yang diakses index 0 dan 1
print(a[:4])  # artinya yang diakses karakter pertama sampai index 3
print(a[3:])  # artinya yang diakses index 3 sampai index terakhir
# jika index batas akhir tidak ada, maka artinya yang diakses hanya sampai index terakhir yang ada
print(a[2:22])  # hasilnya [3,4,5,6]

"""
dua buah lists atau array bila dijumlahkan akan menghasilkan suatu lists atau array baru
dengan isi berupa gabungan lists atau array yang dijumlahkan, urutannya tergantung posisi
penjumlahannya
"""
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = a + b
print(c)  # hasilnya berupa array [1,2,3,4,5,6,7,8,9,10]

d = b + a
print(d)  # hasilnya berupa array [6,7,8,9,10,1,2,3,4,5]

"""
operator perkalian array menghasilkan kelipatan isi array sesuai dengan angka yang dikalikan
namun hanya bisa dengan integer
"""
e = a * 2
print(e)  # hasilnya berupa array [1,2,3,4,5,1,2,3,4,5]

# mengubah item pada array
a = ['a', 'b', 'c', 'd', 'e']
b = 8
a[3] = b  # item pada index 3 diubah dengan isi variabel b
print(a)  # hasilnya berupa array ['a', 'b', 'c', 8, 'e']

# menambahkan item pada array dengan sintaks namavariabelarray.append(itemnya)
a = ['a', 'b', 'c', 'd']
a.append(8)
print(a)  # hasilnya berupa array ['a', 'b', 'c', 'd', 8]

"""
mengubah item array dengan batas tertentu menggunakan sintaks berikut
namavariabel[indexbatasawal:indexbatasakhir] = [itemnya],
itemnya harus sesuai jika banyakknya item yang akan di ubah
"""
var = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
var[2:5] = ['C', 'D', 'E']
print(var)  # hasilnya berupa array ['a', 'b', 'C', 'D', 'E', 'f', 'g']

"""
menghapus item array pada batas tertentu menggunakan sintaks berikut
namavariabel[indexbatasawal:indexbatasakhir] = []
"""
var[2:5] = []
print(var)  # hasilnya berupa array ['a', 'b', 'f', 'g']

# salah satu built-in function untuk array adalah len()
var = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
b = len(var)
print("Banyaknya item pada array var adalah", b)

"""
array dua dimensi atau sering disebut sebagai array dalam array,
index luar berupa array, index dalam berupa index yang menunjuk itemnya, indexnya berupa integer dari 0
sintaks mengaksesnya seperti berikut
namavariabel[indexluar][indexdalam]
"""
a = [['a', 'b', 'c'],
     ['d', 'e', 'f']
     ]  # index luar ke 0 berupa array ['a','b','c'], index luar ke 1 berupa array ['d','e','f']

item = a[0][1]  # index luar ke 0 ['a','b','c'] index dalamnya 1 menunjuk ke item b
print("Item index luar ke 0 dan index dalam ke 1 adalah", item)
