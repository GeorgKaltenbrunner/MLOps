import os

CATALOG = os.getenv("DATABRICKS_CATALOG", "ml_dev")

print(CATALOG)
