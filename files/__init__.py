"""Package to handle files operations.

    Modes:
        - Optional.
        - Determines how the file will be used.
        - Made up of character codes.
        - Allowed actions:
            - r: Read mode (default).
            - w: Write mode - clears contents if file exists.
            - x: Write mode, exclusive creation - fails if file exists already.
            - a: Write mode, append - appends to existing file.
        - Type of file:
            - b: Binary mode.
            - t: Text mode.
        - Other:
            - +: Open for updating(add read or write to current mode).


    File object methods:
        - read() - Read contents of file (r, w+, a+).
        - readline() - Read next line in file (r, w+, a+).
        - write() - Write contents to file (e, w+, a+).
        - writelines() - Write lines to file (r, w+, a+).

"""
