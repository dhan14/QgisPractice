import shapefile
w = shapefile.Writer('soal7')
w.shapeType
w.field('Nama Bidang', 'C')
w.field('Koordinat', 'C')
#nama Record
w.record('polygon', '(1.3)(5.3)(1.2)(5.2)')
#Array sebuah polygon
w.poly([[
    [1,3],
    [5,3],
    [1,2],
    [5,2]
]])
w.close()