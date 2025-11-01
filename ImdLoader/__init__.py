"""
ImdLoader - Functional interface for loading IMD data into DuckDB.

Usage:
    from ImdLoader import imd_data_loader, list_tables, query

    # Load all data
    for status in imd_data_loader():
        if status['stage'] == 'complete':
            print(f"Loaded {status['total_tables']} tables")

    # List tables
    tables = list_tables()

    # Query data
    df = query("SELECT * FROM schema.table LIMIT 10")
"""

from ImdLoader.imd_loader import (
    imd_data_loader,
    load_with_progress,
    list_tables,
    query,
    IMDLoaderError,
    DownloadError,
    ExtractionError,
    LoadError,
    DEFAULT_DATA_DIR,
    DEFAULT_DB_PATH,
    IMD_2025_URL,
)

__all__ = [
    "imd_data_loader",
    "load_with_progress",
    "list_tables",
    "query",
    "IMDLoaderError",
    "DownloadError",
    "ExtractionError",
    "LoadError",
    "DEFAULT_DATA_DIR",
    "DEFAULT_DB_PATH",
    "IMD_2025_URL",
]

__version__ = "0.1.1"
