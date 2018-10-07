# anki_scripts
Helper scripts to move my learning sets from Quizlet to Anki.

# Usage example:
1. Export Quizlet sets as text files, with links, separated by tabs.
1. Concatenate all input files to one
`awk '{print $0}' 3k-*.txt > 3k.txt`
1. Convert "term (example)" to "term\texample" and fix all formatting error or missing info
`./detach_example.py raw/3k.txt > detached/3k-detached.txt`
1. Load 3k-detached.txt in libreoffice calc
    Use only single terms in the translation column. It is easier to make sensible reverse cards.
1. Copy first column with english terms
1. Paste to https://tophonetics.com/ and convert to pronounciation symbols (IPA).
1. Copy back the ipa result to a new second column in the sheet
1. Copy the whole new table to a new text file in the ipa directory
1. Convert to a new format usable for Anki. It also generates a "downloader" script for the image links.
`./to_anki_notes.py ipa/3k-ipa.txt 3k > import/3k-import.txt`
1. Download the images and move to their place.
```mv download_media_3k.sh downloaders/
cd downloaders
./download_media_3k.sh
cd ..
cp -r downloaders/media/* ~/.local/share/Anki2/User\ 1/collection.media/
```
1. Import in Anki (enable html tags)

