import os

def get_catalog() -> str:
    """
    Catalog wird über ENV gesteuert:
    - dev: default ml_dev (wenn ENV nicht gesetzt)
    - test: CI setzt DATABRICKS_CATALOG=ml_test
    - main: CI setzt DATABRICKS_CATALOG=ml_prod
    """
    return os.getenv("DATABRICKS_CATALOG", "ml_dev")

CATALOG = get_catalog()
