import shapefile
"""
NPM1194027
mod 8=3
 persegi panjang ada n buah
 n = 2
"""
w = shapefile.Writer('soal10')
w.shapeType
#kolom
w.field("Nama","C")
w.field("Objek ke","C")
#baris
w.record("Bangun Ruang1","1")
w.record("Bangun Ruang2","2")
#pembuatan bangun ruang pertama
w.poly([[
    [1,5],
    [2,5],
    [2,9],
    [1,9],
    [1,5]
]])
#pembuatan bangun ruang kedua
w.poly([[
	[4,5],
    [5,5],
    [5,9],
    [4,9],
    [4,5]
]])
w.close()