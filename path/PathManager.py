import os


class PathManager():
    """Class to manage path functions."""

    @staticmethod
    def cwd() -> str:
        """Returns current working directory.

        Returns:
            str: returns current working directory.
        """
        return os.getcwd()

    def generate_path_str(self, sub_dir: str, file_name: str='',
                    from_cwd: bool=True) -> str:
        """Create a path from working dir.

        Args:
            sub_dir (str): Sub directory to be appended to working dir.
            file_name (str: optional): File name to be appended to the
                                       end of the path. Defaults to ''.
            from_cwd (bool: optional): Build path from current working
                                       directory? Default to True.

        Returns:
            str: returns a string with the full path.
        """
        if sub_dir[0] in ('/', '\\'):
            sub_dir = sub_dir[1:]

        if from_cwd:
            sub_dir = f'{self.cwd()}/{sub_dir}'

        if sub_dir[-1] in ('/', '\\'):
            sub_dir = sub_dir[:1]

        sub_dir.strip()

        if file_name != '':
            return str(os.path.join('/', sub_dir, file_name)).strip()

        return str(os.path.join('/', sub_dir)).strip()

    @staticmethod
    def create_directories(path: str):
        """Create directories based on input path.

        Args:
            path (str): Path to be created
        """
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as err:
            print(f'Error when trying to create directories')
            raise

    @staticmethod
    def home_dir() -> str:
        return os.path.expanduser('~')


if __name__ == '__main__':
    pm = PathManager()

    print(pm.cwd())

    # With current directory appended.
    print(pm.generate_path_str('/path', 'PathManager.py'))

    # Without current directory appended.
    print(pm.generate_path_str('/path', 'PathManager.py', False))

    # Without file name.
    print(pm.generate_path_str('/path', from_cwd=False))

    # Without file name, with current directory.
    print(pm.generate_path_str('/path'))

    # create directories
    pm.create_directories(pm.generate_path_str('/test_file'))

    print(pm.home_dir())
