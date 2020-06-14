# string berada diantara kutip satu '' atau kutip dua ""
a = 'Python'
b = "Python"
print('Nilai variabel a adalah', a)
print('Nilai variabel b adalah', b)

# string memiliki index yang berawal dari 0, 1, 2, ... bernilai integer
"""
di variabel a diatas
index 0 = P = index -6
index 1 = y = index -5
index 2 = t = index -4
index 3 = h = index -3
index 4 = o = index -2
index 5 = n = index -1
untuk mengaksesnya dengan sintaks berikut,
a[index]
"""
print('index 0 =', a[0], 'index -6 =', a[-6])
print('index 1 =', a[1], 'index -5 =', a[-5])
print('index 2 =', a[2], 'index -4 =', a[-4])
print('index 3 =', a[3], 'index -3 =', a[-3])
print('index 4 =', a[4], 'index -2 =', a[-2])
print('index 5 =', a[5], 'index -1 =', a[-1])

# untuk mengakses karakter string dengan batas tertentu menggunakan sintaks berikut
# namavariabel[indexbatasawal:indexbatasakhir]
# penjelasan yang diakses dari batasawal sampai sebelum batasakhir
print(b[0:2])  # artinya yang diakses index 0 dan 1
print(b[:4])  # artinya yang diakses karakter pertama sampai index 3
print(b[3:])  # artinya yang diakses index 3 sampai index terakhir
# jika index batas akhir tidak ada, maka artinya yang diakses hanya sampai index terakhir yang ada
print(b[2:22])  # hasilnya thon

# untuk membedakan isi string atau karakter kutip bisa menggunakan tanda \' atau \"
# ' atau " dianggap karakter, bukan penanda string
print('hallo world! i\'am learning python')
print("Andrew berkata,\"Aku ingin belajar python!\"")

# bisa juga untuk mendapatkan karakter ' maka penanda string dengan kutip dua "" atau sebaliknya
print("hallo world! i'am learning python")
print('Andrew berkata,"Aku ingin belajar python!"')

# string literals, menggunakan triple quote """...""
# namun ketika di enter akan menghasilkan baris baru secara otomatis tanpa perlu \n
# tanpa baris baru
print("""hello world! how are you ?""")
# terdapat baris baru, yaitu dari kata how ketika di run berada di baris baru
print("""hello world!
how are you ?""")
# agar ketika di enter tidak dianggap sebagai baris baru, maka menggunakan tanda \
print("""hello world!\
how are you ?""")

# operator yang berfungsi dalam string yaitu + dan *
# operator jumlah dalam string menghasilkan string pertama dengan string kedua jadi bersanding
a = "hello"
b = "world"
c = a + b
print(c)  # menghasilkan helloworld

# concate
a = 'Py''thon'
print(a)  # menghasilkan Python

# operator perkalian hanya bisa mengalikan string dengan integer
# hasilnya menjadi pengulangan string sesuai nilai integernya
a = "Python"
b = 3 * a  # boleh juga a * 3
print(b)  # menghasilkan PythonPythonPython

# salah satu built-in function untuk string adalah len()
# untuk menentukan panjang karakter string termasuk spasi
var = "hello, saya belajar python tentang string"
karakter = len(var)
print('Banyaknya karakter var adalah', karakter)
