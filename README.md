# Scripts
Some python scripts used to manage worldaffairscon.org, our main website, and Donna, the WAC registration platform.

## Usage
### csv2reg.py

`csv2reg` is a python tool that uses Firebase Admin SDK to bulk import mandatory delegates from UCC and BH. Provided with a csv file with two columns `name`, `email`, the script will add the delegate to the pre-defined school.
Sample usage:

```
python3 csv2reg.py ucc.csv <ACCESS_CODE>
```


