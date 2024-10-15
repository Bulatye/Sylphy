#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import re
    
def main():

    parser = argparse.ArgumentParser()
    # Parse arguments
    parser.add_argument('artist', type=str)
    parser.add_argument('song', type=str)
    parser.add_argument('-o', '--original', action='store_true', help='Get only original text')
    parser.add_argument('-t', '--translate', action='store_true', help='Get only translate text')
    args = parser.parse_args()

    # processing user input, replacing spaces in words with underscores
    artist = re.sub(r'\s+', '_', args.artist).lower().strip()
    song = re.sub(r'\s+', '_', args.song).lower().strip()

    # create url
    url = f'https://www.amalgama-lab.com/songs/{artist[0]}/{artist}/{song}.html'
    # I get html with data about the song
    html_content = requests.get(url).text

    # Get the original text and translation
    soup = BeautifulSoup(html_content, 'html.parser')
    original_text = soup.find_all(class_='original')
    translate_text = soup.find_all(class_='translate')
    
    # Print text in terminal
    print()
    for i in range(1, len(original_text)):
        if 'перевод' in translate_text[i].text or '1 -' in translate_text[i].text:
            break
        elif original_text[i].text == '' or translate_text[i].text == '':
            print()
        else:
            if args.original:
                print(original_text[i].text)
            elif args.translate:
                print(translate_text[i].text)
            else:
                print(original_text[i].text + ' — ' + translate_text[i].text)
    

if __name__ == '__main__':
    main()

