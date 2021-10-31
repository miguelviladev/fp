def intersects(a1,b1,a2,b2):
    assert a1<=b1
    assert a2<=b2
    return False if b1<=a2 or b2<=a1 else True

print(intersects(2,4,1,2)) # False
print(intersects(1,2,2,4)) # False
print(intersects(1,6,2,4)) # True
