import pandas as pd
from .base import FileReader
import logging

logger = logging.getLogger(__name__)

class CSVFileReader(FileReader):
    def __init__(self, file_path):
        super().__init__(file_path)  # Initialize with the file path

    def read_data(self):
        """
        Reads CSV data, processes it to calculate average ratings, and returns a DataFrame.
        """
        try:
            df = pd.read_csv(self.file_path, encoding='utf-8', dtype={
                'poi_id': 'int32',
                'poi_name': 'str',
                'poi_category': 'str',
                'poi_latitude': 'float',
                'poi_longitude': 'float',
                'poi_ratings': 'str',
            })
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

            df['poi_ratings'] = df['poi_ratings'].apply(lambda x:
                                                        sum(map(float, x.strip('{}').split(','))) / len(
                                                            x.strip('{}').split(',')) if x != '{}' else 0
                                                        )

            # Optionally, you could adjust the column names or the DataFrame structure here to match your database schema

            return df
        except Exception as e:
            logger.error(f"Error reading CSV data from {self.file_path}: {e}")
            return None
