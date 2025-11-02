"""
CLI interface for IOD Loader.

Usage:
    iod load                                      # Load Indices of Deprivation data into DuckDB
    iod load --motherduck                         # Load locally, then push to MotherDuck
    iod load --motherduck --motherduck-db mydb    # Push to MotherDuck with custom name
    iod list-tables                               # List all tables in the database
    iod query "SELECT * FROM table"               # Execute a SQL query

MotherDuck Authentication (choose one):
    1. Environment variable: export motherduck_token='your_token_here'
    2. CLI argument: iod load --motherduck --motherduck-token 'your_token_here'
    3. Interactive: Let DuckDB open a browser for authentication
"""

import argparse
import sys
from pathlib import Path
from IodLoader.iod_loader import (
    load_with_progress,
    list_tables,
    query,
    push_to_motherduck,
    DEFAULT_DATA_DIR,
    DEFAULT_DB_PATH,
)


def cmd_load(args):
    """Load Indices of Deprivation data into DuckDB."""
    data_dir = Path(args.data_dir) if args.data_dir else DEFAULT_DATA_DIR
    db_path = Path(args.db_path) if args.db_path else DEFAULT_DB_PATH

    try:
        load_with_progress(data_dir=data_dir, db_path=db_path)

        # Push to MotherDuck if flag is set
        if args.motherduck:
            print(f"\nPushing database to MotherDuck...")
            motherduck_db = args.motherduck_db or "iod2025"
            motherduck_token = args.motherduck_token if hasattr(args, 'motherduck_token') else None
            push_to_motherduck(
                db_path=db_path,
                remote_db_name=motherduck_db,
                token=motherduck_token
            )
            print(f"✓ Database uploaded to MotherDuck as '{motherduck_db}'")
            print(f"  Connect with: duckdb -c 'ATTACH \"md:{motherduck_db}\"'")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_list_tables(args):
    """List all tables in the database."""
    db_path = Path(args.db_path) if args.db_path else DEFAULT_DB_PATH

    if not db_path.exists():
        print(f"Error: Database not found at {db_path}", file=sys.stderr)
        print("Run 'iod load' first to create the database.", file=sys.stderr)
        return 1

    try:
        tables = list_tables(db_path=db_path)
        if not tables:
            print("No tables found in database.")
        else:
            print(f"Found {len(tables)} tables:\n")
            for table in tables:
                print(f"  {table}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_query(args):
    """Execute a SQL query against the database."""
    db_path = Path(args.db_path) if args.db_path else DEFAULT_DB_PATH

    if not db_path.exists():
        print(f"Error: Database not found at {db_path}", file=sys.stderr)
        print("Run 'iod load' first to create the database.", file=sys.stderr)
        return 1

    try:
        result = query(args.sql, db_path=db_path)
        print(result)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="iod",
        description="IOD 2025 Data Loader - Download and load English Indices of Deprivation data into DuckDB",
    )

    # Global options
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.2",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Load command
    load_parser = subparsers.add_parser(
        "load",
        help="Download and load Indices of Deprivation 2025 data into DuckDB",
    )
    load_parser.add_argument(
        "--data-dir",
        type=str,
        help=f"Directory to store downloaded files (default: {DEFAULT_DATA_DIR})",
    )
    load_parser.add_argument(
        "--db-path",
        type=str,
        help=f"Path to DuckDB database (default: {DEFAULT_DB_PATH})",
    )
    load_parser.add_argument(
        "--motherduck",
        action="store_true",
        help="Push the database to MotherDuck after local load completes",
    )
    load_parser.add_argument(
        "--motherduck-db",
        type=str,
        help="Name for the MotherDuck database (default: iod2025)",
    )
    load_parser.add_argument(
        "--motherduck-token",
        type=str,
        help="MotherDuck authentication token (uses $motherduck_token env var if not provided)",
    )
    load_parser.set_defaults(func=cmd_load)

    # List tables command
    list_parser = subparsers.add_parser(
        "list-tables",
        help="List all tables in the database",
    )
    list_parser.add_argument(
        "--db-path",
        type=str,
        help=f"Path to DuckDB database (default: {DEFAULT_DB_PATH})",
    )
    list_parser.set_defaults(func=cmd_list_tables)

    # Query command
    query_parser = subparsers.add_parser(
        "query",
        help="Execute a SQL query against the database",
    )
    query_parser.add_argument(
        "sql",
        type=str,
        help="SQL query to execute",
    )
    query_parser.add_argument(
        "--db-path",
        type=str,
        help=f"Path to DuckDB database (default: {DEFAULT_DB_PATH})",
    )
    query_parser.set_defaults(func=cmd_query)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
