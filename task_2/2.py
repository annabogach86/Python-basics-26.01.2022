class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def get_wight(self, spec_grav, thick):
        return self._length * self._width * spec_grav * thick / 1000
r = Road(5000, 20)
print(r.get_wight(25, 5))

