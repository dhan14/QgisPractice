import shapefile
w = shapefile.Writer('soal2', shapeType=1)
"""
shapeType=1 artinya mewakili tipe bentuk
"""
w.shapeType

#inisiasi kolom
#Field tipe bisa 
"""
Karakter(C), 
Nomor(N), 
Desimal(F), 
Boolean(L), 
Tanggal(D) 
Memo(M)
"""
w.field('kolom1','C')
w.field('kolom2','C')
#inisiasi baris input
w.record('titik1','1,1')
w.record('titik2','2,2')
#titik koordinat (x,y)
w.point(1,1)
w.point(2,2)

w.close()#menyimpan hasil dengan nama soal1