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

## Working with Streams

While this module allows writing a 2D-List as the CSV values, often we're working with streams instead for reduced memory overhead.
Furthermore, one might want to manipulate the stream or extract values prior to writing the data to the csv file.

This can be done by replacing the `List[List[str]]` type hint with a `Generator` in the `__write_content` method. Then, instead of using `writer.writerows` directly,
one can perform the required manipulation and call `writer.writerows([csv_row])`. Here is an example implementation:

```python
def __write_content(self, writer: csv, data_stream: Generator) -> None:
  """
  Write the csv rows.
  :param data_stream: the data stream.
  :return:
  """
  logger.info('Writing CSV rows...', module=Module.CSV)
  for record in record_stream:
    row = [
      # Perform data manipulation. Output still needs to be a List[str] as required by csv.writer
    ]
    # Optionally filter empty values using this module's method.
    row = self.__filter_empty_cells(row)
    # Write the streamed item as a single row. Note: writerows takes a 2D list
    writer.writerows([row])
```

While the regular export will fail if an error occurs during the export, one might not want this when handling data streams. Add exception handling as necessary.

## CSV Delimiter and Escape Character

To change the default delimiter and escape characters, either change the hard coded values, or use the environment variables:

```bash
export CSV_DELIMITER=","
export CSV_ESCAPE_CHARACTER="\\"
```
