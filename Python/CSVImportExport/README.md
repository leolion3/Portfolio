# CSV Import/Export Module

The provided interface allows importing and exporting csv data with ease.

The provided logging operations require my [Logging module](https://github.com/leolion3/Portfolio/tree/master/Python/Logger) but can also be replaced by any generic logging framework.

## Import/Export Operations

To Import csv data, get the singleton instance of the csv handler and use the `import_csv` method:

```python
from typing import List
...
import csv_handler
from csv_handler import CSVHandler


csv: CSVHandler = csv_handler.get_instance()

# Import data from file 'test.csv'
headers, rows = csv.import_csv(filepath='test.csv')
# headers: List[str]
# rows: List[List[str]]

```

Similarily, to export data, get the singleton instance and call the `export` method:

```python
from typing import List
...
import csv_handler
from csv_handler import CSVHandler


csv: CSVHandler = csv_handler.get_instance()

# Export data to file 'export_test.csv'
headers: List[str] = [...]
rows: List[List[str]] = [[...]]
filepath: str = 'export_test.csv'
csv.export(headers=headers, rows=rows, filepath=filepath)
```

## CSV Delimiter and Escape Character

To change the default delimiter and escape characters, either change the hard coded values, or use the environment variables:

```bash
export CSV_DELIMITER=","
export CSV_ESCAPE_CHARACTER="\\"
```
