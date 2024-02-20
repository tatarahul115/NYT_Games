from bs4 import BeautifulSoup
from requests_html import HTMLSession
from re import compile

alphabets = 'abcdefghijklmnopqrstuvwxyz'
text_file = open('words.txt', 'w')

for alphabet in alphabets:
    pg_no = 1

    while True:
        soup = BeautifulSoup(HTMLSession().get(f'https://www.merriam-webster.com/browse/dictionary/{alphabet}/{pg_no}').html.html,'html.parser')
        words = soup.select( 'div.mw-grid-table-list span')

        for word in words:
            text_file.write(f'{word.contents[0].lower()}\n' if compile('^[a-z]+$').match(str(word.contents[0]).lower()) else '')

        if soup.select( '.next.disabled'):
            break    

        pg_no += 1
    print(f'Parsed Alphabet: {alphabet.upper()}')
print('All Done')