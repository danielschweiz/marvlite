import os

class DataCube:
    # cube properties:
        # get_filename: takes file's name from given file path

    def __init__ (self, file_name):
    
        file_name = None

    def get_filename(self, fullpath):
        
        filename = os.path.basename(fullpath)
        return filename
    