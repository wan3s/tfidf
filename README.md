# TFIDF

This is an impletation of tf-idf search model. This program works only with Russian language.


## How to use program

Just run one of this command:

* to use vector model: `python3 main.py --model=vect`

* to use tf-idf model: `python3 main.py --model=tfidf`

## How to change articles

There is 'articles' directory. My program recursively traverses this directory and extracts the contents of files with the extension '.txt'. So, if you want to use your own articles just remove all files and directorшуы from 'articles' and add any files in any order. But that's not all. See next paragraph.

## How to update collections

If you have changed the contents of the 'articles' directory, you should run the following command:

`python3 main.py --update-collections`

This command refresh 'collections.txt' and 'terms-freqs.txt' files, which are used while searching for documents. If you removed any of these files, programm will automatically update collections.