#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import re
    
def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('artist', type=str)
    parser.add_argument('song', type=str)

    args = parser.parse_args()
    
    artist = args.artist.lower().strip()
    song = args.song.lower().strip()

    artist = re.sub(r'\s+', '_', artist)
    song = re.sub(r'\s+', '_', song)
    first_char = artist[0]


    url = f'https://www.amalgama-lab.com/songs/{first_char}/{artist}/{song}.html'
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, 'html.parser')
    original_text = soup.find_all(class_='original')
    translate_text = soup.find_all(class_='translate')
    
    print()
    for i in range(1, len(original_text)):
        if "перевод" in translate_text[i].text or "1 -" in translate_text[i].text:
            break
        elif original_text[i].text == "" or translate_text[i].text == "":
            print()
        else:
            print(original_text[i].text + " — " + translate_text[i].text)
    

if __name__ == "__main__":
    main()

