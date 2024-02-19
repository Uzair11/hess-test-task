from abc import ABC, abstractmethod

class FileReader(ABC):

    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read_data(self):
        pass