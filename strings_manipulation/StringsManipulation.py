NAME = 'Mark'
AGE = 31

def concatenate_first_method(name: str, age: int) -> str:
    """Hard to read and hard to maintain - Old way of doing things.

    Args:
        name (str): Person name.
        age (int): Person age.

    Returns:
        str: Return a Hello to the given person.
    """
    print("\n Concatenate method")
    return 'Hello ' + name + ' (' + str(age) + ')'

def concatenate_old_style_formating(name: str, age: int) -> str:
    """Concatenate old style. Avoid using this method.

    Args:
        name (str): Person name.
        age (int): Person age.

    Returns:
        str: Return a Hello to the given person.
    """
    print("\n Old style formatting")
    return 'Hello %s (%i)' % (name, age)

def concatenate_format_function(name: str, age: int) -> str:
    """Format Function.
        It is a modern approach and automatically convert the types to string.

    Args:
        name (str): Person name.
        age (int): Person age.

    Returns:
        str: Return a Hello to the given person.
    """
    print("\n Format function")
    return 'Hello {} ({})'.format(name, age)

def concatenate_format_function_order(name: str, age: int) -> str:
    """Format Function with order.
        It is a modern approach and automatically convert the types to string.

    Args:
        name (str): Person name.
        age (int): Person age.

    Returns:
        str: Return a Hello to the given person.
    """
    print("\n Format function with order")
    return 'Hello {1} ({0})'.format(age, name)

def concatenate_format_string_literals(name: str, age: int) -> str:
    """Formated string literals.
        It is a modern approach and automatically convert the types to string.

    Args:
        name (str): Person name.
        age (int): Person age.

    Returns:
        str: Return a Hello to the given person.
    """
    print("\n Format string literals")
    return f'Hello {name} ({age})'

if __name__ == "__main__":
    print(concatenate_first_method(NAME, AGE))
    print(concatenate_old_style_formating(NAME, AGE))
    print(concatenate_format_function(NAME, AGE))
    print(concatenate_format_function_order(NAME, AGE))
    print(concatenate_format_string_literals(NAME, AGE))
