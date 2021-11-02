import shapefile
#membuat 2 poligon
w = shapefile.Writer('soal9')
w.shapeType
#kolom
w.field("Nama","C")
w.field("Objek ke","C")
#baris
w.record("Bangun Ruang1","1")
w.record("Bangun Ruang2","2")
#pembuatan bangun ruang pertama
w.poly([[
    [1,3],
    [5,3],
    [5,2],
    [1,2],
    [1,3]
]])
#pembuatan bangun ruang kedua
w.poly([[
    [1,6],
    [5,6],
    [5,9],
    [1,9],
    [1,6]
]])
w.close()