import shapefile
#inisiasi w sebagai shapefile
w = shapefile.Writer('soal4', shapefile.POINTM)
w.shapeType
#inisiasi kolom
w.field('kolom1','C')
w.field('kolom2','C')
#inisiasi baris input
w.record('titik1','1,1')
w.record('titik2','2,2')
#inisiasi pointm(point meassure)
w.pointm(1,1)
w.pointm(2,2)

w.close()