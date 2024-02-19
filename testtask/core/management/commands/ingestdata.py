from django.core.management.base import BaseCommand, CommandError
from core.ingest_utils.factories import FileReaderFactory
from core.ingest_utils.database_ingestor import DataIngestor
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Ingest data from specified files into the database.'

    def add_arguments(self, parser):
        parser.add_argument('files', type=str, help='Comma-separated list of file paths and their types in the format "path:type,path:type,...". Example: "path/to/file1.csv:csv,path/to/file2.json:json".')

    def handle(self, *args, **options):
        files_arg = options['files']
        files = [file.split(':') for file in files_arg.split(',')]

        for file_path, file_type in files:
            try:
                # Use the FileReaderFactory to get the appropriate reader
                reader = FileReaderFactory.get_reader(file_type, file_path)
                df = reader.read_data()
                if df is None or df.empty:
                    logger.warning(f'No data found in {file_path} or could not read the file.')
                    continue

                # Ingest data into the database using DataIngestor
                ingestor = DataIngestor(df, file_type)
                ingestor.ingest_data()
                self.stdout.write(self.style.SUCCESS(f'Successfully ingested data from {file_path}.'))

            except ValueError as e:
                logger.error(f'Error with file {file_path}: {e}')
            except Exception as e:
                logger.error(f'Unexpected error with file {file_path}: {e}')
                raise CommandError(f'Unexpected error with file {file_path}: {e}')
