import logging
import pandas as pd
from .base import FileReader

logger = logging.getLogger(__name__)

class JSONFileReader(FileReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def read_data(self):
        try:
            # df = pd.read_json(self.file_path, encoding='utf-8')
            # df['latitude'] = df['coordinates'].apply(lambda x: x.get('latitude', 0))
            # df['longitude'] = df['coordinates'].apply(lambda x: x.get('longitude', 0))
            # df['average_rating'] = df['ratings'].apply(lambda x: sum(x) / len(x) if x else 0)
            # df = df.drop(columns=['coordinates', 'ratings']).rename(columns={
            #     'id': 'internal_id',
            #     'name': 'name',
            #     'category': 'category',
            #     'latitude': 'latitude',
            #     'longitude': 'longitude',
            #     'average_rating': 'average_rating'
            # })
            # return df

            df = pd.read_json(self.file_path, encoding='utf-8')
            logger.info(df.head())
            df['pois_latitude'] = df['coordinates'].apply(lambda x: x.get('latitude', 0))
            df['pois_longitude'] = df['coordinates'].apply(lambda x: x.get('longitude', 0))
            df['ratings'] = df['ratings'].apply(lambda x: sum(x) / len(x) if x else 0)
            df = df.drop(columns=['coordinates'])
            return df
        except Exception as e:
            logger.error(f"Error reading JSON data from {self.file_path}: {e}")
            return None
