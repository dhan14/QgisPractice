import shapefile

#inisiasi w sebagai shapefile bertipe polygon
w = shapefile.Writer("soal6", shapeType=shapefile.POLYGON)
w.shapeType

#inisiasi kolom
w.field("kolom1", "C")
w.field("kolom2", "C")

#inisiasi baris input
w.record('garis','1,3')

#Inisiasi polygon
w.poly([[[1, 3], [5, 3]]])

w.close()