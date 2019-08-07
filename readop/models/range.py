class Range:
    def __init__(self, min_value: float, max_value: float):
        if min_value > max_value:
            raise ValueError('min_value ({0}) must be larger than max_value ({1})'.format(min_value, max_value))

        self._min_value = min_value
        self._max_value = max_value

    def __repr__(self):
        return '[{0}, {1}]'.format(self.min_value, self.max_value)

    def includes(self, value):
        return self.min_value <= value <= self.max_value

    def scale(self, scale: float, upper: bool) -> None:
        if upper:
            self._min_value += (scale * (self.max_value - self.min_value))
        else:
            self._max_value -= (scale * (self.max_value - self.min_value))

    @property
    def min_value(self) -> int:
        return int(self._min_value)

    @property
    def max_value(self) -> int:
        return int(self._max_value)

    @classmethod
    def from_normalized_value(cls, normalized_value: float, scale: float):
        if normalized_value < 0:
            return cls(normalized_value * scale + scale, scale)
        else:
            return cls(0, normalized_value * scale)
