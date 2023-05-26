"""Python serial number generator."""

class SerialGenerator:

    def __init__(self, start = 0):
        self.start = self.next = start

    def __repr__(self):
        f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self, start=100):

        start + 1
        return start

    def reset():
        num = 100
        return num

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

