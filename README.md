# Sylphy

#### This script fetches song lyrics and their translations in russian from [Amalgama Lab](https://www.amalgama-lab.com/).

## Installation

#### To use this script, you need Python 3 and a few additional libraries. You can install them using pip:

> pip install requests beautifulsoup4

##  You must give the program execution rights

> chmod +x ~/your/path/sylphy.py

## Optional: if you don't want to use ./ to call the script, create a symbolic link

> bash cd /usr/local/bin
> sudo ln -s /path/to/your/sylphy.py sylphy

## Usage

#### The script takes several command-line arguments to fetch song lyrics and their translations.

## Arguments:
    artist: The name of the artist (default positional argument)
    song: The title of the song (default positional argument)
    -o, --original: Get only the original text (optional argument)
    -t, --translate: Get only the translated text (optional argument)

## Examples

Get the original text and its translation into russian:
> sylphy "pink floyd" "money"

#### Get only the original text:
> ./sylphy -o wardruna helvegen

#### Get only the translated text:
> python3 sylphy -t "the doors" "the end"

## Example Output

> Money, get away  — Деньги прочь,
Get a good job with more pay and you're O.K.  — Когда есть хорошая работа, приличная зарплата и с тобой все так, как надо,
Money, it's a gas  — Деньги — это блеск,
Grab that cash with both hands and make a stash  — Хватаю звонкую монету обеими руками, пакуюсь до отказа,
New car, caviar, four star daydream,  — Новая машина, икра, полный сон наяву,
Think I'll buy me a football team. — Я думаю купить футбольную команду.

> Money, get back  — Деньги, вернитесь,
I'm alright, Jack, keep your hands off of my stack  — Пусть мне будет хорошо, прочь руки с моей кучи,
Money, it's a hit  — Деньги — это успех,
Don't give me that do goody good bullshit  — Не указывай мне, что делать сентиментальное дерьмо,
I'm in the hi-fidelity first class travelling set  — Я путешествую в каюте первым классом
And I think I need a Lear jet. — И думаю, что мне необходим авиалайнер.

> Money, it's a crime  — Деньги — это преступление,
Share it fairly but don't take a slice of my pie  — Дели честно, не покушаясь на часть моего пирога.
Money, so they say  — Деньги, так они говорят,
Is the root of all evil today  — Это корень сегодняшнего зла,
But if you ask for a rise it's no surprise that  — Но если ты потребуешь надбавки, неудивительно,
They're giving none away, away, away — Что они ничего не дадут.

