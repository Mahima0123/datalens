from datetime import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

def process_dataset():
    print("Datalens dataset processing started...")

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