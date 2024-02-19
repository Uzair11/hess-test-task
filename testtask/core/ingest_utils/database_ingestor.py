import logging
from django.db import transaction
from core.models import POI

logger = logging.getLogger(__name__)

class DataIngestor:
    def __init__(self, df, data_type):
        self.df = df
        self.data_type = data_type

    def ingest_data(self):
        # Select the appropriate ingestion method based on the data type
        if self.data_type == 'csv':
            self._ingest_csv_data()
        elif self.data_type == 'json':
            self._ingest_json_data()
        elif self.data_type == 'xml':
            self._ingest_xml_data()
        else:
            logger.error(f"Unsupported data type: {self.data_type}")
            return

        logger.info(f"Successfully ingested {self.data_type} data into the database.")

    def _ingest_csv_data(self):
        self._batch_insert('poi_id', 'poi_name', 'poi_category', 'poi_latitude', 'poi_longitude', 'poi_ratings')

    def _ingest_json_data(self):
        self._batch_insert('id', 'name', 'category', 'pois_latitude', 'pois_longitude', 'ratings')

    def _ingest_xml_data(self):
        self._batch_insert('internal_id', 'name', 'category', 'latitude', 'longitude', 'average_rating')

    def _batch_insert(self, id_field, name_field, category_field, latitude_field, longitude_field, rating_field):
        objects_list = []
        for _, row in self.df.iterrows():
            poi = POI(
                internal_id=str(row[id_field]),
                name=row[name_field],
                category=row[category_field],  # Directly using category data from row
                latitude=row[latitude_field],
                longitude=row[longitude_field],
                average_rating=row[rating_field]
            )
            objects_list.append(poi)

        # Using batch insertion for efficiency
        batch_size = 100
        for i in range(0, len(objects_list), batch_size):
            POI.objects.bulk_create(objects_list[i:i+batch_size])
