class FilesManager():
    """Class responsible to manage files operations.
    """

    @staticmethod
    def open_and_return_str(file_path: str) -> str:

        with open(file_path) as f:
            lines = f.read()

        return lines

    @staticmethod
    def write_line_to_file(file_path: str, content: str, mode: str='append',
                      new_line: bool=True):
        """Write content to the file.

        Args:
            file_path (str): File Path.
            content (str): Content to write.
            mode (str): Mode (overwrite, append). Default to [append].
            new_line (bool): Write to a new line when True. Default to [True].
        """
        if new_line:
            content = f'{content}\n'
        if mode == 'overwrite':
            m = 'w'
        elif mode == 'append':
            m = 'a'

        with open(file_path, m) as f:
            f.write(content)

    @staticmethod
    def write_lines_to_file(file_path: str, content: list, mode: str='append',
                      new_line: bool=True):
        """Write multiple lines to the file.

        Args:
            file_path (str): File Path.
            content (list): Content (lines) to write.
            mode (str): Mode (overwrite, append). Default to [append].
            new_line (bool): Write to a new line when True. Default to [True].
        """
        if new_line:
            new_content = []
            for l in content:
                new_content.append(f'{l}\n')
                content = new_content

        if mode == 'overwrite':
            m = 'w'
        elif mode == 'append':
            m = 'a'

        with open(file_path, m) as f:
            f.writelines(content)

if __name__ == '__main__':
    fm = FilesManager()
    input_file = 'files/sample_1.txt'
    output_file = 'files/output.txt'
    print(fm.open_and_return_str(input_file))

    fm.write_line_to_file(output_file, 'Test message to write.', 'overwrite')
    print(fm.open_and_return_str(output_file))

    fm.write_line_to_file(output_file, 'Second test message to write.')
    print(fm.open_and_return_str(output_file))

    # Write multiple lines to the file.
    content = ['Hi', 'Hello', 'Hey']
    fm.write_lines_to_file(output_file, content)
    print(fm.open_and_return_str(output_file))
