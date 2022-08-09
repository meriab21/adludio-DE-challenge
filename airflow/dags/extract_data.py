import os
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator

deployment = os.environ.get("DEPLOYMENT", "dev")


default_args = {
    "owner": "airflow",
    "start_date": datetime(2022, 7, 25, 8, 25, 00),
    "concurrency": 1,
    "retries": 0,
}


dag = DAG(
    "data_load_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)
envs = ["dev", "stg", "prod"]


with dag:
    start = DummyOperator(task_id="start")
