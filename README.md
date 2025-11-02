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

# Load locally and push to MotherDuck
iod load --motherduck

# Load and push to MotherDuck with custom database name
iod load --motherduck --motherduck-db my_iod_db

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

## MotherDuck Integration

You can push your local DuckDB database to MotherDuck for cloud-based querying and sharing.

### Setup & Authentication

Get your MotherDuck token from [motherduck.com](https://motherduck.com), then choose one of these authentication methods:

#### Option 1: Environment Variable (Recommended)

```bash
export motherduck_token='your_token_here'
iod load --motherduck
```

#### Option 2: CLI Argument

```bash
iod load --motherduck --motherduck-token 'your_token_here'
```

#### Option 3: Interactive Browser Auth

```bash
# Just run without a token - DuckDB will open a browser for authentication
iod load --motherduck
```

### Usage Examples

```bash
# Load data locally and push to MotherDuck (uses env var or browser auth)
iod load --motherduck

# Use token directly in command
iod load --motherduck --motherduck-token 'your_token'

# Specify custom database name in MotherDuck
iod load --motherduck --motherduck-db my_custom_name

# All options together
iod load --motherduck --motherduck-token 'token' --motherduck-db my_iod_data
```

The process:

1. Downloads and loads all data into a local DuckDB file
2. Pushes the complete database to MotherDuck
3. Your data is now available in the cloud!

## Querying the Data

You can query the data through:

- **CLI tool**: `iod query "SELECT * FROM ..."`
- **Python package**: Import `query` from `IodLoader`
- **DuckDB CLI**: Run `duckdb IOD2025.duckdb` in your terminal

### Example Query

```bash
iod query "SELECT * FROM file_2_iod2025_domains_of_deprivation.iod2025_domains LIMIT 10"
```
