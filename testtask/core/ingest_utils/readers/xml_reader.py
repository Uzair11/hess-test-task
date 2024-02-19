import re
import logging
import pandas as pd
from io import StringIO
from .base import FileReader


logger = logging.getLogger(__name__)

class XMLFileReader(FileReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def escape_ampersands_in_xml_content(self, xml_content: str) -> str:
        return re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+);)', '&amp;', xml_content)

    def read_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                xml_content = file.read()

            xml_content_escaped = self.escape_ampersands_in_xml_content(xml_content)
            df = pd.read_xml(StringIO(xml_content_escaped), xpath=".//DATA_RECORD")

            # Process 'pratings' to calculate 'average_rating'
            df['average_rating'] = df['pratings'].apply(lambda x:
                                                        sum(map(float, x.split(','))) / len(x.split(',')) if x else 0)
            df.drop(columns=['pratings'], inplace=True)

            # Ensure the column names are correctly mapped to your model's fields
            df.rename(columns={
                'pid': 'internal_id',  # Assuming 'pid' maps to 'internal_id'
                'pname': 'name',
                'pcategory': 'category',
                'platitude': 'latitude',
                'plongitude': 'longitude',
            }, inplace=True)

            return df
        except Exception as e:
            logger.error(f"Failed to read XML data from {self.file_path}: {e}")
            return None