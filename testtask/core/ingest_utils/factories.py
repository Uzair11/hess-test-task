from .readers.csv_reader import CSVFileReader
from .readers.json_reader import JSONFileReader
from .readers.xml_reader import XMLFileReader


class FileReaderFactory:

    @staticmethod
    def get_reader(file_type, file_path):
        """
        Factory method to instantiate the appropriate FileReader subclass
        based on the file type.

        Args:
            file_type (str): The type of the file to be read (e.g., 'csv', 'json', 'xml').
            file_path (str): The path to the file that needs to be read.

        Returns:
            FileReader: An instance of a FileReader subclass suitable for the given file type.

        Raises:
            ValueError: If an unsupported file type is provided.
        """
        readers = {
            'csv': CSVFileReader,
            'json': JSONFileReader,
            'xml': XMLFileReader,
        }

        reader_class = readers.get(file_type.lower())
        if reader_class:
            return reader_class(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
