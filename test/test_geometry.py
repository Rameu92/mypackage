import mypackage as mp

def test_geometry():
    point1 = mp.Point(0,0)
    point2 = mp.Point(3,4)
    line = mp.Line(point1, point2)

    assert line.length() == 5.0