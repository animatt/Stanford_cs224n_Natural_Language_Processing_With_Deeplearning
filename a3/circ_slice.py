class CircSlice(list):
    def __init__(self, start, size, data):
        end = start + size
        first = slice(start, min(end, len(data)))
        second = slice(0, (end > len(data)) * (end % len(data)))
        self.extend(data[first] + data[second])

