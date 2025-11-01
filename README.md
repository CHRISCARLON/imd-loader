# IMD 2025 Data Loader 🦆

A simple Python package for downloading and loading the latest English Indices of Deprivation 2025 data into DuckDB.

IMD Source Data -> [Click Here](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025)

## Installation

```bash
pip install imd-loader
```

Or with uv:

```bash
uv add imd-loader
```

## Quick Start

### Simple Usage

Use in a Python script.

```python
from ImdLoader import load_with_progress

if __name__ == "__main__":
    load_with_progress()
```

Or use the cli tool to load directly.

```bash
imd load
```

## Database Structure

The loader creates a DuckDB database with the following structure:

- **Schemas**: Named after the Excel filename
- **Tables**: Named after the Excel sheet names

## Querying the Data

You can query the data through:

- The cli tool
- Via the package itself - just import 'query'
- Via a local duckdb seesion - just run duckdb -ui in your terminal and attach the .duckdb file
