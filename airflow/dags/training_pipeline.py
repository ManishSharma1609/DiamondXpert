from __future__ import annotations
from textwrap import dedent
import json
from airflow import DAG
from airflow.operators.python import PythonOperator 
import pendulum
from src.pipeline.training_pipeline import TrainingPipeline

training_pipeline = TrainingPipeline()

with DAG(
    "Gemstone_training_pipeline",
    default_args={"retries":2},
    description="Diamong price prediction training pipeline",
    schedule="@hourly",
    start_date=pendulum.datetime(2024, 8, 18, tz="UTC"),
    catchup=False,
    tags=["Machine_learing", "Classification", "Gemstone"]
) as dag:

    dag.doc_md = __doc__

    def data_ingestion(**kwargs):
        ti = kwargs["ti"]
        train_data_path, test_data_path = training_pipeline.start_data_Ingestion()
        ti.xcom_push("data_ingestion_artifacts", {"train_data_path" : train_data_path, "test_data_path": test_data_path })

    def data_transformation(**kwargs):
        ti = kwargs["ti"]
        data_ingestion_artifact = ti.xcom_pull(task_ids = "data_ingestion", key = "data_ingestion_artifacts")
        train_arr, test_arr = training_pipeline.start_data_transformation(data_ingestion_artifact["train_data_path"], data_ingestion_artifact["test_data_path"])
        train_arr = train_arr.tolist()
        test_arr = test_arr.tolist()
        ti.xcom_push("data_transformation_artifact", {"train_arr":train_arr, "test_arr": test_arr})

    def model_trainer(**kwargs):
        ti = kwargs["ti"]
        data_transformation_artifacts = ti.xcom_pull(task_ids = "data_transformation", key = "data_transformation_artifact")
        import numpy as np 
        train_arr = np.array(data_transformation_artifacts["train_arr"])
        test_arr = np.array(data_transformation_artifacts["test_arr"])
        training_pipeline.start_model_training(train_arr, test_arr)

    def push_to_s3(**kwargs):
        import os
        bucket_name = os.getenv("BUCKET_NAME")
