# IOD 2025 Data Loader 🦆

A simple Python package and CLI for downloading and loading the latest English Indices of Deprivation 2025 data into DuckDB.

IOD Source Data -> [Click Here](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025)

## Installation

```bash
pip install iod-loader
```

Or with uv:

```bash
uv add iod-loader
```

## Quick Start

### CLI Usage (Recommended)

Use the CLI tool to load and query the data directly.

```bash
# Load all IOD 2025 data
iod load

# List all tables
iod list-tables

# Query the data
iod query "SELECT * FROM your_schema.your_table LIMIT 10"
```

### Python Library Usage

Or use in a Python script.

```python
from IodLoader import load_with_progress

if __name__ == "__main__":
    load_with_progress()
```

## Database Structure

The loader creates a DuckDB database with the following structure:

- **Schemas**: Named after the Excel filename
- **Tables**: Named after the Excel sheet names

## Querying the Data

You can query the data through:

- **CLI tool**: `iod query "SELECT * FROM ..."`
- **Python package**: Import `query` from `IodLoader`
- **DuckDB CLI**: Run `duckdb IOD2025.duckdb` in your terminal

### Example Query

```bash
iod query "SELECT * FROM file_2_iod2025_domains_of_deprivation.iod2025_domains LIMIT 10"
```
