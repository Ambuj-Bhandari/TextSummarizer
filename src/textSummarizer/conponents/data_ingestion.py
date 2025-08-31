import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig
import os

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_Url,
                filename=self.config.local_data_file
            )
            logger.info("File is downloaded")
        else:
            logger.info("File already exists")
        
    
    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_file:
            zip_file.extractall(unzip_path)