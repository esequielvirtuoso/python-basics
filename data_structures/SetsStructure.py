class SetsSample():
    """Sample class to explore Sets Data Structure.

        - Unordered collection of unique elements.
        - No indexes.
        - Faster lookups compared to lists.
        - Support various mathematical operations.
        - Items in a set must be hashable.
            - Immutable (do not change).
            - Used for performance behind-the-scenes.

        Examples of items that can be added to a set:

            - Strings.
            - Integers.
            - Booleans.

        Examples of items that cannot be added to a set:

            - Lists.
            - Dictionaries.
            - Sets.

        How to create an empty set?

            - a = {} - not allowed once it is reserved for Dictionaries.
            - a = set() - this is the correct way.

        Use cases:

            - Make a list Unique.
            - Perform lookups witho more performance.
            - Perform mathematical operations with more performance.
                - Union.
                - Difference.
                - Intersection.
    """

    @staticmethod
    def keep_unique_list(items: list) -> list:
        """Keep only unique values within the list.

        Args:
            items (list): List to be changed.

        Returns:
            list: returns a list with unique values only.
        """
        print(f"List with duplicates: {items}")
        items_unique = list(set(items))
        print(f"List with no duplicates: {items_unique}")
        return items_unique

    @staticmethod
    def check_if_duplicates(items: list) -> bool:
        """Check if a list has duplicated items.

        Args:
            items (list): List to be checked.

        Returns:
            bool: returns True whan it has duplicated values, otherwise False.
        """
        items.sort()
        unique = list(set(items))
        unique.sort()

        if items == unique:
            return False
        return True

    @staticmethod
    def make_some_sets():
        names = {'Jessica', 'Bento', 'Jane'}
        print(names)

        # Add new element
        names.add('Esequiel')
        print(names)

        # Remove element
        names.remove('Jane')
        print(names)

        # Clear a set
        names.clear()
        print(names)

    @staticmethod
    def keep_common_elements(a: set, b: set) -> set:
        """Keep only common elements between two sets.

        Args:
            a (set): Set a.
            b (set): Set b.

        Returns:
            set: return set with common elements.
        """
        print(a)
        print(b)
        return a.intersection(b)

    @staticmethod
    def unify_sets(a: set, b: set) -> set:
        """Unify two sets.

        Args:
            a (set): Set a.
            b (set): Set b.

        Returns:
            set: return a set with all elements of the two input sets.
        """
        print(a)
        print(b)
        return a.union(b)

    @staticmethod
    def symmetric_difference_sets(a: set, b: set) -> set:
        """Keep only elements that not match between two sets.

        Args:
            a (set): Set a.
            b (set): Set b.

        Returns:
            set: return set with elements that not match between two sets.
        """
        print(a)
        print(b)
        return a.symmetric_difference(b)

if __name__ == '__main__':
    items = ['Apple', 'Banana', 'Apple', 'Orange']
    a = {'Jessica', 'Bento'}
    b = {'Esequiel', 'Bento'}

    SetsSample().keep_unique_list(items)
    print(SetsSample().check_if_duplicates(items))
    SetsSample().make_some_sets()
    print(SetsSample().keep_common_elements(a, b))
    print(SetsSample().unify_sets(a, b))
    print(SetsSample().symmetric_difference_sets(a, b))
