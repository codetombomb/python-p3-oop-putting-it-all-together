#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        self._size = 0

    def get_size(self):
        return self._size

    def set_size(self, size):
        if not type(size) == int:
            print("size must be an integer.")
        else:
            self._size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(get_size, set_size,)