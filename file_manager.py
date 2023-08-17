import pandas as pd
from pandas import ExcelWriter
import os
import config
import gspread
logger = config.logger


class FileManager:

    @staticmethod
    def save_df(df, filename: str, extension: str, sep: str = ',', path: str = None, header: bool = True, index: bool = False, sheet_name: str = ''):
        """
        :param df: pandas DataFrame
        :param path: location to save the file
        :param filename: what to name the file
        :param extension: mime type: accepts xls,xlsx,csv
        :param sep: separator if csv
        :param headers: include headers?
        :param index: include index?
        :param sheet_name: if mime xls or xlsx name of the sheet in the file
        :return: location of created file
        """
        path = config.outpath if path is None else path
        if df.empty:
            raise Exception('Empty DataFrame')

        elif extension in ['xlsx', 'xlsx']:
            writer = ExcelWriter(f'{path}/{filename}.{extension}')
            created_file_path = df.to_excel(
                writer, sheet_name=sheet_name, index=index)
            writer.save()

        elif extension == 'csv':
            logger.info(f"{path}/{filename}.{extension}")
            created_file_path = df.to_csv(
                f"{path}/{filename}.{extension}", sep=sep, header=header, index=index)
        else:
            raise Exception('Unknown Mime Type')

        return f"{path}/{filename}.{extension}" if created_file_path is None else created_file_path

    @staticmethod
    def read_file(file_path: str, sep=','):
        """
        :param file_path:
        :return: pandas DataFrame
        """
        mime = file_path.split('.')[:-1]
        if mime in ('xlsx', 'xls'):
            return pd.read_excel(file_path, header=1)
        elif mime == 'csv':
            return pd.read_csv(file_path, header=1, sep=sep)
        else:
            raise Exception('Unknown Mime Type')
