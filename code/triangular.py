##--------------------------------------------------------------------------------------------- 
##This work by Carlos Alvarez is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
##---------------------------------------------------------------------------------------------


##Upper trianguar matrix storage

class Triangular:
    def __init__(self, size):
        try:
            assert (size > 0) and (type(size) == int)
        except AssertionError:
            print("size must be a possitive integer.")
            return
        self.size = size
        self.M = []
        for i in xrange(size-1):
            v = [0 for j in xrange(size-1-i)]
            self.M.append(v)

    def __call__(self, y, x):
        try:
            assert (x > y) and (x <= len(self.M))
        except AssertionError:
            print("Index in triangular matrix out of range.")
            return
        return self.M[y][x-y-1]

    def set_element(self, y, x, val):
	try:
            assert (x > y) and (x <= len(self.M))
        except AssertionError:
            print("Index in triangular matrix out of range.")
            return
        self.M[y][x-y-1] = val
        
    def set_zero(self):
	for i in xrange(self.size-1):
	  for j in xrange(self.size-1-i):
	    self.M[i][j] = 0
