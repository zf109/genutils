"""
    collection of list operations
"""

def flat_list(ls):
    """
        Simple function that flats a list of iteratables.

        Args:
        --------
            ls: a list of nested lists

        Returns:
            a list of elements, which is flattened
    """
    return [item for sublist in ls for item in sublist]


class ListPairs:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def self_or_others(self, l1=None, l2=None):
        return self.l1 if not l1 else l1, self.l2 if not l2 else l2

    def intersection_ratio(self, l1=None, l2=None):
        l1, l2 = self.self_or_others(l1, l2)

        """Function determines how two sets intersects with each other."""
        return len([w for w in l1 if w in l2])/min(len(l1),len(l2))

    def length_ratio(self, l1=None, l2 =None):
        """Calculate the length ratio between two lists"""
        l1, l2 = self.self_or_others(l1, l2)
        return abs(len(l1)-len(l2))/max(len(l1),len(l2))

    def order_similarity(self, l1=None, l2=None):
        """Calculate the similarity in terms of order of words, normalized by 
        its length"""
        l1, l2 = self.self_or_others(l1, l2)
        s1 = enumerate(l1)
        s2 = enumerate(l2)
        ss1 = [w for w in s1 if w[1] in [x[1] for x in s2]]
        ss2 = [w for w in s2 if w[1] in [x[1] for x in s1]]

        return len([[x, y] for x,y in zip(ss1,ss2) if x[1]==y[1]])/min(len(l1),len(l2))

    def similarity(self, l1, l2):
        """Calculate how similar are two lists are, in terms of order/length/elements"""
        l1, l2 = self.self_or_others(l1, l2)
        return  self.intersection_ratio(l1,l2) +\
                self.order_similarity(l1, l2) -\
                self.length_ratio(l1, l2)

