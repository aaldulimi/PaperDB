from rocksdict import Rdict 
import re


class DocumentDB():
    def __init__(self, path: str = "database/"):
        self.db = Rdict(path)
        
    def insert(self, document, primary_key = None):
        # encoding: primary_key/column_name -> value 

        if not primary_key:
            primary_key = list(document.keys())[0]

        primary_key_value = document.__dict__[primary_key]

        for key, value in document.__dict__.items():
            if key != primary_key:
                key_string = f"{primary_key_value}/{key}"
                self.db[key_string] = value

    
    def get(self, key):
        return self.db[key]

    
    def iterate_keys(self):
        for key in self.db.keys():
            yield key

    def get_id(self, field, value):
        for key in self.iterate_keys():
            key_column = re.findall("[^/]*", key)[2]

            if field == key_column:
                if value == self.get(key):
                    return re.findall("[^/]*", key)[0]



