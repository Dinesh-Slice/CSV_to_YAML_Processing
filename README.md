# CSV to YAML Converter 

### Requirements

- Python3 
- Termcolor 
- Pandas 
- Numpy

**To install all requirements, run:**
```
pip3 install -r requirements.txt
```

### Instructions

```
$ python3 main.py <csv file path> 
```

Example
```
$ python main.py sample.csv 
```

### Issues (Windows machines only)

Strings are surrounded by both double quotes and single quotes. i.e 

```
'"string"'
```

- Fix: 
    - Simple find and replace to get rid of THE single quotes 
    - Find `'` replace with an empty string in any text editor


### Expected Results 

- If on Mac OS, the formatted yaml file should open automatically in a file named `final_file.yml`

- On windows, single quotes have to be removed manually using find and replace in a text editor

