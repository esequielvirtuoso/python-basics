import pprint


class DictionariesSample():
    """Sample class to explore Dictionaries Data Structure.

        - Key/ Value mappings. {'some-key': 'some-value'}
        - Unordered.
        - Referred to as 'dict'.

        Benefits of using tuples:

            - Security - it cannot be modified for sure.
            - Reliability.
            - Better performance compared to list (large scale).
    """
    def exists(self, d: dict, key) -> bool:
        """Check if key is present within a given dictionary.

        Args:
            d (dict): Dictionary to check.
            key ([type]): Key to lookup.

        Returns:
            bool: returns True if key was found, otherwise False.
        """
        if d.get(key) != None:
            return True
        return False

    def set_key_value(self, d: dict, key, value) -> dict:
        """Set key value of a dict.

        Args:
            d (dict): Dict to set a key value.
            key: Key to set the value.
            value: New value to assign to the key.

        Returns:
            dict: return a new dict with the new value.
        """
        if self.exists(d, key):
            d[key] = value
            return d
        return None

    def remove_key(self, d: dict, key) -> dict:
        """Remove key from a dictionary.

        Args:
            d (dict): Dictionary.
            key ([type]): Key to be removed from the dicitonary.

        Returns:
            dict: returns a new dictionary without the key.
        """
        if self.exists(d, key):
            d.pop(key)
            return d
        return d

    @staticmethod
    def loop_through_dict(d: dict):
        for k, v in d.items():
            print(f'Key - {k} | Value - {v}\n')

if __name__ == '__main__':
    dc = DictionariesSample()
    sample_dict = {
                    'name': 'Esequiel',
                    'hobbies': ['gym', 'running', 'netflix'],
                    'age': '29'}
    print(type(sample_dict))

    print(sample_dict)
    dc.set_key_value(sample_dict, 'name', 'Jessica')
    dc.set_key_value(sample_dict, 'age', 30)
    print(sample_dict)

    print(dc.exists(sample_dict, 'name'))

    print(dc.remove_key(sample_dict, 'age'))

    # clear dictionary
    print(sample_dict.clear())

    nested_dict = {
        'model': 'C3',
        'brand': 'Citroen',
        'plate': 'MKF-9J05',
        'release-year': 2013,
        'owner': {
            'first-name': 'Esequiel',
            'last-name': 'Virtuoso',
            'birth-date': '10/06/1992',
            'gender': 'Male',
            'marital-status': 'married'
        },
        'released_by_year': {
            2010: 30000,
            2011: 35000,
            2012: 40000,
            2013: 50000
        }
    }
    pprint.pprint(nested_dict)
    print(nested_dict.get('owner', {}).get('first-name'))

    dc.loop_through_dict(nested_dict)

    # Get keys from dictionary
    print(nested_dict.keys())
