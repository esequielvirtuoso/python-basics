import string
import os

class LargeFiles():
    """Class with sample functions to handle large files."""

    @staticmethod
    def read_line_by_line(file_path: str):
        """Reading a file line by line."""
        with open(file_path) as f:
            for l in f:
                print(l)

    @staticmethod
    def read_part_by_part(file_path: str, chunk_size: int):
        """Read file part by part.

        Args:
            file_path (str): File to read.
            chunk_size (int): Part size.
        """
        with open(file_path) as f:
            print(f.read(chunk_size))
            print(f.read(chunk_size))
            print(f.read(chunk_size))

    @staticmethod
    def generate_file():

        with open('files/alphabet_file.txt', 'w') as af:
            af.write(string.ascii_lowercase)

        print('Alphabet file created.')

    @staticmethod
    def read_seek(file: str, mode: str=''):
        if mode == '':
            with open(file) as f:
                print(f'Location when opening: {f.tell()}')
                print(f'First letter: {f.read(1)}')
                print(f'Second letter: {f.read(1)}')

                # changing the pointer manually
                f.seek(4)
                print(f'5th letter: {f.read(1)}')

        if mode == 'binary':
            with open(file, 'rb') as f:
                print('Every other letter:')
                while True:
                    letter = f.read(1)
                    if letter:
                        print(letter.decode())
                        f.seek(1, os.SEEK_CUR) # seek from the cursor
                    else:
                        break
                print('Last letter:')
                f.seek(-1, os.SEEK_END)
                print(f.read(1).decode())


if __name__ == '__main__':
    fm = LargeFiles()
    input_file = 'files/sample_1.txt'

    fm.read_line_by_line(input_file)

    input_file = 'files/sample_2.txt'
    fm.read_part_by_part(input_file, 4)

    fm.generate_file()

    input_file = 'files/alphabet_file.txt'
    fm.read_seek(input_file)

    # binary mode
    fm.read_seek(input_file, 'binary')
