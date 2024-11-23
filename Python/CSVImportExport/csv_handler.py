#!/usr/bin/env python3
"""
Open-Source csv import/export module by Leonard Haddad, 2024.
Provided in accords with the MIT License.
More on GitHub at https://leolion.tk/
"""
import csv
import os

from typing import Tuple, List, Optional
from log_handler import Logger, Module, get_instance

logger: Logger = get_instance()


class CSVHandler:
    """
    Handles csv import/export.
    Default delimiter is semicolon (;) for higher compatability.
    Default escape char is double quotes (") for Microsoft Excel compatability.
    """
    CSV_DELIMITER: str = os.getenv('CSV_DELIMITER') or ';'
    CSV_ESCAPE_CHARACTER: str = os.getenv('CSV_ESCAPE_CHARACTER') or '"'

    @staticmethod
    def __write_header(writer: csv, headers: List[str]) -> None:
        """
        Write the csv headers to the export file.
        :param headers: the csv headers as a list of strings.
        :return:
        """
        logger.info('Writing CSV headers...', module=Module.CSV)
        writer.writerow(headers)

    @staticmethod
    def __filter_empty_cells(row: List[str]) -> List[str]:
        """
        Replaces empty cells with empty strings to keep csv consistent.
        :param row: The current csv row data.
        :return: The filtered csv row data.
        """
        return [str(item) if item is not None else '' for item in row]

    def __write_content(self, writer: csv, rows: List[List[str]]) -> None:
        """
        Write the csv rows.
        :param rows: the csv rows as a list of cells.
        :return:
        """
        logger.info('Writing CSV rows...', module=Module.CSV)
        filtered: List[List[str]] = [self.__filter_empty_cells(row) for row in rows]
        writer.writerows(filtered)

    def export(self, headers: List[str], rows: List[List[str]], filepath: str) -> None:
        """
        Exports the given csv rows to a new file.
        :param headers: the csv headers as a list of strings.
        :param rows: The csv rows as a list, each consisting of a list of cells.
        :param filepath: The name of the file to write to.
        :return:
        """
        logger.info(f'Exporting csv data to file \"{filepath}\".', module=Module.CSV)
        with open(filepath, 'w+') as f:
            writer = csv.writer(
                f,
                delimiter=self.CSV_DELIMITER,
                quotechar=self.CSV_ESCAPE_CHARACTER,
                escapechar='\\',
                lineterminator='\n'
            )
            self.__write_header(writer=writer, headers=headers)
            self.__write_content(writer=writer, rows=rows)
            f.flush()
        logger.info('CSV data exported successfully.', module=Module.CSV)

    def __read_csv_values(self, file_ptr) -> List[List[str]]:
        """
        Read the csv data as a list of rows, each consisting of a list of cells.
        :param file_ptr: Pointer for reading csv file.
        :return: A list of csv rows, each as a list of cells.
        """
        logger.debug(f'Setting up parser with delimiter \"{self.CSV_DELIMITER}\" '
                     + f'and escape char \"{self.CSV_ESCAPE_CHARACTER}\"...', module=Module.CSV)
        csv_reader = csv.reader(file_ptr, delimiter=self.CSV_DELIMITER, quotechar=self.CSV_ESCAPE_CHARACTER)
        file_ptr.seek(0)
        next(csv_reader, None)
        values: List[List[str]] = [row for row in csv_reader]
        return values

    def __read_csv_header(self, file_ptr) -> List[str]:
        """
        Read the csv headers.
        :param file_ptr: CSV-file file-pointer.
        :return: The csv headers as a list of strings.
        """
        csv_reader = csv.reader(file_ptr, delimiter=self.CSV_DELIMITER)
        headers: List[str] = next(csv_reader, None)
        logger.debug(f'Reading Headers: {headers}, length: {len(headers)}', module=Module.CSV)
        return headers

    def import_csv(self, filepath: str) -> Tuple[List[str], List[List[str]]]:
        """
        Import csv data from the given file path.
        :param filepath: Path to the csv file.
        :return: A tuple of csv headers as a list, and csv data as a list of rows (each as a list of cells).
        """
        logger.info(f'Reading CSV file \"{filepath}\"...', module=Module.CSV)
        with open(filepath, 'r') as f:
            logger.debug('Reading CSV headers...', module=Module.CSV)
            headers = self.__read_csv_header(file_ptr=f)
            logger.debug('Reading CSV rows...', module=Module.CSV)
            content = self.__read_csv_values(file_ptr=f)
            logger.info('CSV file imported successfully.', module=Module.CSV)
            return headers, content


__instance: Optional[CSVHandler] = None


def get_instance() -> CSVHandler:
    """
    Get the CSV handler singleton instance.
    :return: The CSV handler singleton instance.
    """
    global __instance
    if __instance is None:
        __instance = CSVHandler()
    return __instance
