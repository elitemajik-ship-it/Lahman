import requests
import zipfile
import io
import pandas as pd
from pathlib import Path
import sqlite3

def ingest_lahman_data(output_db: str = 'lahman.db'):
    """Ingest all Lahman Baseball Database tables from the repo's zip into a SQLite DB for fast querying and predictions."""
    print('Downloading Lahman baseballdatabank zip...')
    zip_url = 'https://raw.githubusercontent.com/elitemajik-ship-it/Lahman/master/source-data/baseballdatabank-master.zip'
    response = requests.get(zip_url)
    response.raise_for_status()
    
    print('Extracting and loading CSVs...')
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        # Find all CSV files in core/
        csv_files = [f for f in z.namelist() if f.startswith('baseballdatabank-master/core/') and f.endswith('.csv')]
        
        conn = sqlite3.connect(output_db)
        for csv_path in csv_files:
            table_name = Path(csv_path).stem  # e.g. Batting
            print(f'  Loading {table_name}...')
            with z.open(csv_path) as f:
                df = pd.read_csv(f)
                # Clean column names if needed
                df.columns = [col.strip() for col in df.columns]
                df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
    
    print(f'✅ All {len(csv_files)} tables ingested into {output_db}!')
    print('Ready for predictions. Example:')
    print("conn = sqlite3.connect('lahman.db')")
    print("pd.read_sql('SELECT * FROM Batting LIMIT 5', conn)")

if __name__ == '__main__':
    ingest_lahman_data()
    # Optional: also save parquets for ML
    # Path('data/parquet').mkdir(parents=True, exist_ok=True)
    # ... but SQLite is sufficient for now
