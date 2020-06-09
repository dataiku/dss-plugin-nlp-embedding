import json
from dataiku.customrecipe import get_recipe_resource
import requests
import shutil
import gzip

class word2vec_downloader():
    def __init__(self,folder,language):
        self.folder = folder

        self.language = language
        if self.language != 'english':
            raise NotImplementedError("Word2vec vectors are only available for English. Use fastText for other languages.")
        
        self.params = json.load(os.path.join(get_recipe_resource(),"models_download_links.json"))["word2vec"]
        self.CHUNK_SIZE = 32768
        
    def get_stream(self):
        session = requests.Session()
        response = session.get(self.params["link_model"], params={'id': self.params["id_model"]}, stream=True)
        token = self.__get_confirm_token(response)

        if token:
            params = {'id': self.params["id_model"], 'confirm': token}
            response = session.get(URL, params=params, stream=True)
        else:
            raise NotImplementedError("Token")

        return response

    def download(self):
        response = self.get_stream()
        destination_file_name = "word2vec_" + str(self.language)
        destination_writer = self.folder.get_writer()

        #Write .gz file to folder
        for chunk in response.iter_content(self.CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                destination_writer.write(chunk)
        destination_writer.close()

        #Unzip file
        with self.folder.get_writer(destination_file_name) as f_out, self.folder.get_download_stream("GoogleNews-vectors-negative300.bin.gz") as f_in:
            shutil.copyfileobj(gzip.open(f_in), f_out)

    def __get_confirm_token(self,response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None   

