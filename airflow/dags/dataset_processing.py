from datetime import datetime

import pandas as pd

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def process_dataset():
    print("Datalens dataset processing started...")

    file_path = "/app/media/datasets/original/sales.csv"

    print(f"Reading file: {file_path}")

    df = pd.read_csv(file_path)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Columns: {list(df.columns)}")

    print("Datalens dataset processing completed.")


with DAG(
    dag_id="datalens_dataset_processing",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["datalens", "dataset"],
) as dag:

    process = PythonOperator(
        task_id="process_dataset",
        python_callable=process_dataset,
    )