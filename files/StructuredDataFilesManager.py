import csv
import json

class StructuredDataFilesManager():
    """Class to handle structured data files."""

    @staticmethod
    def read_csv(file: str):
        with open(file, newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)

    @staticmethod
    def read_csv_as_dict(file: str):
        with open(file, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                id_val = row['Id']
                score_val = row['Score']
                print(f'{id_val} - {score_val}')

    @staticmethod
    def write_rows_csv(file: str, values: list, delimiter: str=','):
        """Write rows to csv.

        Args:
            file (str): File to write data to.
            values (list): Values to write.
            delimiter (str, optional): Columns delimiter. Dafaults to ','.
        """
        with open(file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=delimiter)

            if any(isinstance(el, list) for el in values):
                writer.writerows(values)
            else:
                writer.writerow(values)

    @staticmethod
    def write_dicts_to_csv(file: str, fields_names: list, values):
        """Write single or multiple rows dict to CSV file.

        Args:
            file (str): Destination file.
            fields_names (list): Name of fields.
            values ([type]): Content to write.
        """
        print(type(values) is list)
        with open(file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fields_names)
            writer.writeheader()
            if type(values) is dict:
                writer.writerow(values)

            if type(values) is list:
                writer.writerows(values)

    @staticmethod
    def encode_to_json_str(obj: dict) -> str:
        """Encode dict to string (JSON).

        Args:
            obj (dict): Object to encode.

        Returns:
            str: returns an encoded string corresponding to a JSON.
        """
        return json.dumps(obj)

    @staticmethod
    def encode_to_file(file: str, obj: dict) -> None:
        """Encode dict to json file.

        Args:
            file (str): Destination file name.
            obf (dict): Object to encode to the file.
        """
        with open(file, 'w') as jf:
            json.dump(obj, jf)

    @staticmethod
    def decode_from_str(json_str: str) -> dict:
        """Decode a JSON string to a python dict.

        Args:
            json_str (str): JSON string to decode.

        Returns:
            dict: returns a dict with the JSON string content.
        """
        return json.loads(json_str)

    @staticmethod
    def decode_from_json_file(file: str) -> dict:
        """Decode a JSON file to a python dict.

        Args:
            file (str): JSON file to decode.

        Returns:
            dict: returns a dict with the JSON file content.
        """
        with open(file) as jf:
            result = json.load(jf)

        return result

if __name__ == '__main__':
    sdfm = StructuredDataFilesManager()
    file_name = 'files/sample_csv.csv'

    sdfm.read_csv(file_name)

    # write single row to csv file.
    file_name = 'files/output_csv.csv'
    value = ['col_1', 'col_2', 'col_3']
    sdfm.write_rows_csv(file_name, value)

    # Write multiple rows to csv file.
    file_name = 'files/output_csv_2.csv'
    values = [
        ['col_1', 'col_2', 'col_3'],
        [1, 2, 3],
        [8, 20, 5]
    ]
    sdfm.write_rows_csv(file_name, values, ';')

    # Open csv as dict.
    file_name = 'files/sample_csv_2.csv'
    sdfm.read_csv_as_dict(file_name)

    # Write single row dict.
    file_name = 'files/sample_csv_3.csv'
    fields_names = ['UserId', 'Name', 'Score']
    values = {'UserId': 1, 'Score': 100, 'Name': 'Esequiel Virtuoso'}
    sdfm.write_dicts_to_csv(file_name, fields_names, values)

    # Write multiple rows dict.
    file_name = 'files/sample_csv_4.csv'
    values = [{'UserId': 0, 'Score': 100, 'Name': 'Esequiel Virtuoso'},
                {'UserId': 1, 'Score': 50, 'Name': 'Ismael Virtuoso'},
                {'UserId': 2, 'Score': 160, 'Name': 'Jessica Correa'}]
    sdfm.write_dicts_to_csv(file_name, fields_names, values)

    # Encode to json string.
    values = {'first-name': 'Esequiel', 'last-name': 'Virtuoso', 'age': 29}
    print(sdfm.encode_to_json_str(values))

    # Encode to json file.
    file_name = 'files/sample_json.json'
    sdfm.encode_to_file(file_name, values)

    # Decode from JSON string.
    values = '{"first-name": "Esequiel", "last-name": "Virtuoso", "age": 29}'
    print(sdfm.decode_from_str(values))
    print(sdfm.decode_from_str(values)['first-name'])

    # Decode from JSON file.
    print(sdfm.decode_from_json_file(file_name))
    print(sdfm.decode_from_str(values)['last-name'])
