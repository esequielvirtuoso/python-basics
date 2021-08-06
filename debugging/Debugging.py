class DebuggingSample():
    """Sample Class for debugging alternatives."""

    def __init__(self) -> None:
        self.default_name = 'Esequiel'
        self.default_age = 29

    def print_sample_data(self, name: str=None, age: int=None) -> None:
        """Saple function to print sample data

        Args:
            name (str): Name to print.
            age (int): Age to print
        """
        if name and age:
            message = f'Name: {name}.\n Age: {age}.'
        else:
            message = f'Name: {self.default_name}.\n Age: {self.default_age}'

        breakpoint()
        print(message)

if __name__ == '__main__':
    DebuggingSample().print_sample_data()
