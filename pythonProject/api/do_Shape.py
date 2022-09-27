import Shape

a = Shape.Point()
print(repr(a))

b = Shape.Point(3, 4)
print(str(b))
b.distance_from_origin()