class FunctionsSample():
    """Class for creating sample functions.
    """

    @staticmethod
    def output_generating(input: str) -> None:
        """Print the input string.

        Args:
            input (str): String to print.
        """
        print(f'\n{input}')

    @staticmethod
    def simple_calculator(a: int=0, b: int=0, op: str='add') -> int:
        """Sum or subtract two integer numbers based on operation parameter.

        Args:
            a (int, optional): First element. Defaults to 0.
            b (int, optional): Second Element. Defaults to 0.
            op (str: optional): Indicates the operation (add/sub).
                                             Defaults to 0.

        Returns:
            int: Returns the operation result.
        """
        if op == 'add':
            return a + b

        return a - b

    @staticmethod
    def conv_bool_to_str(input: bool) -> str:
        """Convert a boolean input to string.

        Args:
            input (bool): Boolean value to convert.

        Returns:
            str: Return 'T' when input is True, otherwise return 'F'.
        """
        if input:
            return 'T'

        return 'F'

if __name__ == "__main__":
    FunctionsSample().output_generating('Test message')
    print(FunctionsSample().simple_calculator(5,5))
    print(FunctionsSample().simple_calculator(5,2, 'sub'))
    print(FunctionsSample().conv_bool_to_str(True))
    print(FunctionsSample().conv_bool_to_str(False))
