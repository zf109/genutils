"""
    collection of file operations
"""
from .listoperation import flat_list

def create_file(filename):
    """Equivalent of touch """
    f = open(filename, 'w')
    f.close()

class Text(str):
    """
        Extended str class, added few commonly usd function/source
    """
    @classmethod
    def from_file(cls, filename, method='r'):
        f = open(filename, method)
        content = f.read()
        f.close()
        return cls(content)

    def split_by_line(self):
        return self.split('\n')

    def split_by_words(self):
        return flat_list([line.split(' ') for line in self.split('\n')])
