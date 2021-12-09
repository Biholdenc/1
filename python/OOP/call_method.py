class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __call__(self):
        volume = self.width*self.height*self.depth
        print('volume is equal to', volume)

obj = Box(10, 20, 30)

obj()