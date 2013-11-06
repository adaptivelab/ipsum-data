import textwrap
import json
import docopt

from data_generator import SeriesDataGenerator
from data_generator import DateIncrementor
from data_generator import IntIncrementor


if __name__ == "__main__":

    incrementors = {
        'date': DateIncrementor(),
        'integer': IntIncrementor()
    }

    usage = textwrap.dedent("""
    Generate tabular series data
    ----------------------------

    Takes standard in containing ES documents to download from S3.
    Designed to be used in conjunction with download_es_doc script.

    Usage:
        generate_series_data.py [--rows=<rows> --spec=<spec>]

    Options:
        --rows=<rows>               The number of rows to create
        --spec=<spec>               The data spec
    """)

    args = docopt.docopt(usage)

    rows = None
    if args.get('--rows'):
        rows = int(args.get('--rows'))

    spec_file = None
    if args.get('--spec'):
        spec_file = args.get('--spec')

    spec_json = open(spec_file)
    spec = json.load(spec_json)

    generator = SeriesDataGenerator(spec, incrementors)
    generator.write_header()
    generator.write_rows(rows)
