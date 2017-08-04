"""
    collection of file operations
"""

def create_file(filename):
    """Equivalent of touch """
    f = open(filename, 'w')
    f.close()
