"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, path):
        
        file = open(path)

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)