# anki_scripts
Helper scripts to move my learning sets from Quizlet to Anki.

# Usage example:
1. Export Quizlet sets as text files, with links, separated by tabs.
1. Concatenate all input files to one
`awk '{print $0}' 3k-*.txt > 3k.txt`
1. Convert "term (example)" to "term\texample"
`./detach_example.py 0_raw_input/3k.txt > 1_detached_examples/3k-detached.txt`
1. load 3k-detached.txt in libreoffice calc
    Use only single terms in the translation column. It is easier to make sensible reverse cards.
1. copy first column with english terms
1. paste to https://tophonetics.com/ and convert to pronounciation symbols (IPA).
1. copy back the ipa result to a new second column in the sheet
1. copy the whole new table to a new text file in 2_added_ipa directory
1. Convert to a new format usable for Anki. It also generates a "downloader" script for the image links.
`./to_anki_notes.py 2_added_ipa/3k-ipa.txt 3k > 3_anki_import/3k-import.txt`
1. Download the images and move to their place.
```mv download_media_3k.sh 4_downloaders/
cd 4_downloaders/
./download_media_3k.sh
cd ..
cp -r 4_downloaders/media/* ~/.local/share/Anki2/User\ 1/collection.media/
```
1. import in Anki (enable html tags)

