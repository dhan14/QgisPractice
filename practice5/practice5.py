import shapefile
#inisiasi w sebagai shapefile
w = shapefile.Writer('soal5')
w.shapeType
#inisiasi kolom
w.field('kolom1','C')
w.field('kolom2','C')
#inisiasi baris input
w.record('garis','1,5')
#Inisiasi garis agar menjadi polyline
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.close()