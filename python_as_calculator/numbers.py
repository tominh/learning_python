# expression
# +, -, *, /, %, //

# operator assignment =
x = 2
y = 3
print('x =', x)
print('y =', y, '\n')

# + penjumlahan biasa
a = 3 + 2
print('Nilai a =', a)

b = 3
c = 2
a = b + c
print('a =', b, '+', c, '=', a, '\n')

# - pengurangan biasa
a = 3 - 2
print('Nilai a =', a)

b = 3
c = 2
a = b - c
print('a =', b, '-', c, '=', a, '\n')

# * perkalian biasa
a = 3 * 2
print('Nilai a =', a)

b = 3
c = 2
a = b * c
print('a =', b, '*', c, '=', a, '\n')

# / pembagian biasa, tipenya otomatis menjadi float
a = 3 / 2
print('Nilai a =', a)

b = 3
c = 2
a = b / c
print('a =', b, ':', c, '=', a, '\n')

# % operator modulus atau disebut sisa bagi
b = 3
c = 2
a = b % c
print('Sisa bagi', b, ':', c, '=', a, '\n')

# // floor division atau disebut pembulatan
b = 3
c = 2
a = b // c
print('Pembagian', b, ':', c, 'dibulatkan menjadi =', a, '\n')

# ** operator pangkat
b = 3
c = 2
a = b ** c
print('Nilai', b, 'pangkat', c, '=', a, '\n')

# operator yang di dahulukan
'''
1. yang di dalam kurung
2. pangkat
3. perkalian atau pembagian tergantung posisi
4. penjumlahan atau pengurangan tergantung posisi
'''
b = 6
c = 5
d = 4
e = 3
f = 2
a = (b + c) * d / e ** f + b - c
print('Nilai (', b, '+', c, ') *', d, ':', e,
      'pangkat', f, '+', b, '-', c, '=', a, '\n')
