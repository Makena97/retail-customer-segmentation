"""
BrightCart Customer Segmentation Data Pipeline

This Airflow DAG orchestrates the end-to-end data pipeline:
1. Ingest raw Online Retail II data
2. Clean transaction data
3. Anonymize customer identifiers
4. Create customer-level RFM features
5. Validate data quality
6. Run bias/representation checks
7. Generate audit logs
8. Produce the final analytical dataset

Author: Bessy Makena
Project: BrightCart Online Retail Customer Segmentation
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.ingestion import ingest_data
from src.cleaning import clean_data
from src.anonymization import anonymize_data
from src.transformation import create_rfm_features
from src.validation import validate_data
from src.bias_detection import run_bias_checks
from src.audit_logging import log_pipeline_completion


# ---------------------------------------------------------
# DAG CONFIGURATION
# ---------------------------------------------------------

default_args = {
    "owner": "brightcart-data-team",
    "depends_on_past": False,
    "retries": 1,
}


with DAG(
    dag_id="brightcart_customer_segmentation_pipeline",
    default_args=default_args,
    description="End-to-end data pipeline for BrightCart customer segmentation",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["brightcart", "retail", "customer-segmentation", "module3"],
) as dag:

    # -----------------------------------------------------
    # 1. INGESTION
    # -----------------------------------------------------

    ingest = PythonOperator(
        task_id="ingest_raw_data",
        python_callable=ingest_data,
    )

    # -----------------------------------------------------
    # 2. DATA CLEANING
    # -----------------------------------------------------

    clean = PythonOperator(
        task_id="clean_transaction_data",
        python_callable=clean_data,
    )

    # -----------------------------------------------------
    # 3. DATA ANONYMIZATION
    # -----------------------------------------------------

    anonymize = PythonOperator(
        task_id="anonymize_customer_data",
        python_callable=anonymize_data,
    )

    # -----------------------------------------------------
    # 4. FEATURE ENGINEERING
    # -----------------------------------------------------

    transform = PythonOperator(
        task_id="create_customer_rfm_features",
        python_callable=create_rfm_features,
    )

    # -----------------------------------------------------
    # 5. DATA VALIDATION
    # -----------------------------------------------------

    validate = PythonOperator(
        task_id="validate_processed_data",
        python_callable=validate_data,
    )

    # -----------------------------------------------------
    # 6. BIAS / REPRESENTATION CHECKS
    # -----------------------------------------------------

    bias_check = PythonOperator(
        task_id="run_bias_detection",
        python_callable=run_bias_checks,
    )

    # -----------------------------------------------------
    # 7. AUDIT LOGGING
    # -----------------------------------------------------

    audit = PythonOperator(
        task_id="write_audit_log",
        python_callable=log_pipeline_completion,
    )

    # -----------------------------------------------------
    # PIPELINE DEPENDENCIES
    # -----------------------------------------------------

    ingest >> clean >> anonymize >> transform >> validate >> bias_check >> audit
