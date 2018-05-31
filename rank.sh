#!/bin/bash

# Update the local history and generate ranked list of playcounts.

script_name="$0"

IN=gbi_history.json
OUT=gbi_most_played.txt

while [ $# -gt 0 ]; do
   case $1 in
      -i|--in)
         shift
         IN="$1"
         ;;
      -o|--out)
         shift
         OUT="$1"
         ;;
      *)
        echo "Usage $script_name [-i HISTORY_FILE] [-o RANKED_OUTPUT_LIST]"
        exit 1
        ;;
   esac
   shift
done


python ./update_gbi_history.py

grep '"text"' "$IN" | sed -e 's/.*Live now on Giant Bomb Infinite: //' -e 's/.*Live now on Giant Bomb TV: //' -e 's/https:\/\/t.co\/.*//' | sort | uniq -c | sort -r > "$OUT"
