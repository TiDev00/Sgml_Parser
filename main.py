import os
import codecs
from pathlib import Path
import contextlib
from bs4 import BeautifulSoup

def extraction(file):
    # Extract the text contained in seg tag
    with codecs.open(file, 'r', encoding='ISO-8859-1') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        text_list = soup.find_all('seg')
        for item in text_list:
            lines_in_item = item.text.split('\n')
            # Open a new file
            with codecs.open(file.replace('sgm', 'txt'), 'a', encoding='ISO-8859-1') as external_file:
                # Redirect the output in the new file
                with contextlib.redirect_stdout(external_file):
                    [print(x.strip()) for x in lines_in_item if x.strip()!= ""]
            external_file.close()


# Fonction main 
if __name__ == '__main__':
    ask_filepath = True
    while ask_filepath:
        filepath = input("\nEnter a path to a sgml file : ")
        if filepath and Path(os.path.expanduser(filepath)).is_file():
            extraction(filepath)
            print("\nExtraction done...")
            ask_filepath = False
        else:
            print("\nInvalid filepath...")
