from __future__ import annotations
from textwrap import dedent
import json
from airflow import DAG
from airflow.operators.python import PythonOperator 