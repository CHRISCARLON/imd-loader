"""
IodLoader - Functional interface for loading Indices of Deprivation data into DuckDB.

Usage:
    from IodLoader import iod_data_loader, list_tables, query

    # Load all data
    for status in iod_data_loader():
        if status['stage'] == 'complete':
            print(f"Loaded {status['total_tables']} tables")

    # List tables
    tables = list_tables()

    # Query data
    df = query("SELECT * FROM schema.table LIMIT 10")
"""

from IodLoader.iod_loader import (
    iod_data_loader,
    load_with_progress,
    list_tables,
    query,
    IODLoaderError,
    DownloadError,
    ExtractionError,
    LoadError,
    DEFAULT_DATA_DIR,
    DEFAULT_DB_PATH,
    IOD_2025_URL,
)

__all__ = [
    "iod_data_loader",
    "load_with_progress",
    "list_tables",
    "query",
    "IODLoaderError",
    "DownloadError",
    "ExtractionError",
    "LoadError",
    "DEFAULT_DATA_DIR",
    "DEFAULT_DB_PATH",
    "IOD_2025_URL",
]

__version__ = "0.1.0"
