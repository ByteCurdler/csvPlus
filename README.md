# CSV+
A wrapper for the default `csv` library.
## Usage
```python3
import csvPlus as csv
csv.read(open("example.csv"), headers=True)
csv.write(open("example.csv", "w"), data=somedata)
