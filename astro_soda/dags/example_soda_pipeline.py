# /Library/anaconda3/envs/stenv/lib/python3.9/site-packages/airflow/example_dags/example_soda_pipeline.py

from airflow import DAG
from datetime import datetime

from airflow.operators.bash import BashOperator

SODA_PATH = "/Users/pravashpanigrahi/PycharmProjects/python_streamlit_lib/astro_soda/include"  # can be specified as an env variable
ASTRO_SODA_PATH = "/Users/pravashpanigrahi/PycharmProjects/python_streamlit_lib/astro_soda"

with DAG(
    dag_id="example_soda_pipeline",
    default_args={"retries": 0},
    schedule='@once',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example"]
) as dag:

    soda_test = BashOperator(
        task_id="soda_test",
        bash_command=f"conda init bash && source /Library/anaconda3/etc/profile.d/conda.sh "
                     f"&& conda activate stenv && pip install soda-core && "
                     f"soda scan -d soda_test -c {SODA_PATH}/configuration.yml {SODA_PATH}/checks.yml "
    )
