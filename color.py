class color:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def to_rgb(self) -> list:
        return list([self.red, self.green, self.blue])

    def to_bgr(self) -> list:
        return list([self.blue, self.green, self.red])


yellow = color(255, 255, 0)
blue = color(0, 0, 255)
cyan = color(0, 255, 255)
red = color(255, 0, 0)
white = color(255, 255, 255)
