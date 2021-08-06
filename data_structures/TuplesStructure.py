class TupleSample():
    """Sample class to explore Tuple     Data Structure.

        - Stores a sequence of objects.
        - Immutable (cannot change (add or remove items)).
        - uses indexes.
        - Ulike sets the tuples can keep equal elements.

        Note:
            For creating a tuple with only one item use trailing comma.
            a = (1,)
            or
            a = ([1]) - Not useful option

        Tuple methods:
            - Count elements. - a.count(1) - how many times 1 appear in the tuple.
            - Index - a.index(1) - Get index value of first occurence of value 1.

        Benefits of using tuples:

            - Security - it cannot be modified for sure.
            - Reliability.
            - Better performance compared to list (large scale).
    """

    @staticmethod
    def conv_list_to_tuple(l: list) -> tuple:
        """Convert a list to a tuple.

        Args:
            l (list): List to be converted

        Returns:
            tuple: return a tuple with same elements of input list.
        """
        return tuple(l)

    @staticmethod
    def check_duplicated_element(t: tuple, element) -> bool:
        """Verify if a given element is repeated in the tuple.

        Args:
            t (tuple): Tuple to verify.
            element ([type]): Element to lookup.

        Returns:
            bool: returns True when duplicated, otherwise False.
        """
        if t.count(element) > 1:
            return True

        return False

    @staticmethod
    def lookup_in_tuple(t: tuple, element) -> bool:
        """Verify if element is present within the input tuple.

        Args:
            t (tuple): Tuple to verify.
            element ([type]): Element to lookup.

        Returns:
            bool: returns True when found, otherwise False.
        """
        if element in t:
            return True
        return False

if __name__ == '__main__':
    items = ['Apple', 'Banana', 'Apple', 'Orange']
    tup = ('Esequiel', 'Jessica', 'Bento', 'Bento')

    print(TupleSample().conv_list_to_tuple(items))
    print(TupleSample().check_duplicated_element(tup, 'Bento'))
    print(TupleSample().lookup_in_tuple(tup, 'Jessica'))
