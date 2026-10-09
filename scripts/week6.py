from pathlib import Path
import click
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import run_query

@click.command()
@click.option("--database", required=True)
@click.option("--query-file", required=True)
@click.option("--output-file", required=True)
def main(database, query_file, output_file):
    query = Path(query_file).read_text()
    df = run_query(database, query)
    print(df.head())
    df.to_csv(output_file)


if __name__ == "__main__":
    main()
