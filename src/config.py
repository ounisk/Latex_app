import os

dirname = os.path.dirname(__file__)

data_file_path = os.path.join(dirname,"..","data" "data.csv")  

ALIST_FILENAME = os.getenv("ALIST_FILENAME") or "references.csv"
ALIST_FILE_PATH = os.path.join(dirname, "..", "data", ALIST_FILENAME) #luo data-hakemistoon filen references.csv

