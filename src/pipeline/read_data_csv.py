import pandas as pd
from typing import Protocol
import hashlib


class DataReader(Protocol):
    def read_data(self) -> pd.DataFrame:
        ...


class CSVReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)


class ExcelReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_data(self) -> pd.DataFrame:
        return pd.read_excel(self.file_path)


class Pseudonymizer(Protocol):
    def get_pseudo(self, df: pd.DataFrame) -> pd.DataFrame:
        ...


class HashPseudo:
    def __init__(self, salt: str) -> None:
        self.salt = salt

    def _hash(self, value):
        if pd.isna(value):
            return value
        value = str(value)
        to_hash = f"{self.salt}::{value}"
        return hashlib.sha256(to_hash.encode("utf-8")).hexdigest()

    def get_pseudo(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["pseudo_customerId"] = df["customerId"].apply(self._hash)
        return df


class Pipeline:
    def __init__(self, reader: DataReader, pseudo: Pseudonymizer) -> None:
        self.reader = reader
        self.pseudo = pseudo

    def run(self) -> pd.DataFrame:
        df = self.reader.read_data()
        return self.pseudo.get_pseudo(df)


pipeline = Pipeline(
    CSVReader("/Workspace/Users/kaltenbrunnergeorg@googlemail.com/MLOps/Churn Modeling.csv"),
    HashPseudo(salt="pipeline123hLkyZct"),
)

d = CSVReader("/Workspace/Users/kaltenbrunnergeorg@googlemail.com/MLOps/Churn Modeling.csv").read_data()

print(d)
