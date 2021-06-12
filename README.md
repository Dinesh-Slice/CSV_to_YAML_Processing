# CSV to YAML Converter 

### Requirements
```
Python3
termcolor
```

### Instructions

```
$ python3 main.py <csv file path> <output yml file path>
```

Example
```
$ python main.py sample.csv sample.yml
```

### Issues

Strings are surrounded by both double quotes and single quotes. i.e 

```
'"string'"
```

- Fix: 
    - Simple find and replace to get rid of the single quotes 
    - Find `'` replace with an empty string in any text editor