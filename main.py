import contextlib

from bs4 import BeautifulSoup


def extraction(file):
    # Extract the text contained in seg tag
    with open(file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        text_list = soup.find_all('seg',)
        for item in text_list:
            lines_in_item = item.text.split('\n')
            with open(file.replace('sgm', 'txt'), 'a') as external_file:
                with contextlib.redirect_stdout(external_file):
                    [print(x.strip()) for x in lines_in_item if x.strip()!= ""]
            external_file.close()

extraction('test-fren-en.sgm')
extraction('test-fren-fr.sgm')
