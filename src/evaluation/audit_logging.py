"""
Audit logging module for the BrightCart pipeline.

Records important pipeline activities for traceability,
governance and privacy monitoring.
"""

from pathlib import Path
from datetime import datetime
import logging


LOG_DIRECTORY = Path("logs")
LOG_FILE = LOG_DIRECTORY / "pipeline_audit.log"


LOG_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)


def log_event(
    event,
    dataset=None,
    records=None,
    status="SUCCESS"
):
    """
    Record a pipeline event.
    """

    message = (
        f"Event={event} | "
        f"Dataset={dataset} | "
        f"Records={records} | "
        f"Status={status}"
    )

    logging.info(message)

    print(message)


def log_pipeline_completion():
    """
    Record successful completion of the pipeline.
    """

    log_event(
        event="PIPELINE_COMPLETED",
        dataset="brightcart_customer_rfm.csv",
        status="SUCCESS"
    )

    return True


if __name__ == "__main__":
    log_pipeline_completion()
