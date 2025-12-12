
class BBox:
    def __init__(self, x1=100, y1=100, x2=100, y2=100):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    def get_size(self):
        return {"width": self.width, "height": self.height}

    def merge(self, other):
        self.x1 = min(self.x1, other.x1)
        self.y1 = min(self.y1, other.y1)
        self.x2 = max(self.x2, other.x2)
        self.y2 = max(self.y2, other.y2)
        return self


class ColorMode:
    def __init__(self, civilian, friend, hostile, neutral, unknown):
        self.Civilian = civilian
        self.Friend = friend
        self.Hostile = hostile
        self.Neutral = neutral
        self.Unknown = unknown
