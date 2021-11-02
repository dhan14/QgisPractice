import shapefile
w = shapefile.Writer('soal8', shapeType=shapefile.POLYGON)
w.shapeType
w.field("Nama","C")
w.field("garis","C")
w.record("polygon","(1.3)(5.3)(1.2)(5.2)(1.3)")
#Membuat Polygon 
w.poly([[
    [1,3],
    [5,3],
    [1,2],
    [5,2],
    [1,3]
]])
w.close()