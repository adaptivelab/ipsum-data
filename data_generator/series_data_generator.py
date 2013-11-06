import csv
import sys


class SeriesDataGenerator(object):

    def __init__(self, data_specification, incrementors):
        self.writer = csv.writer(sys.stdout)
        self.data_specification = data_specification
        self.incrementors = incrementors

    def write_header(self):
        column_headers = []

        for column in self.data_specification:
            column_headers.append(column['name'])

        self.writer.writerow(column_headers)

    def write_rows(self, rows):
        # for each column, store the last value to be incremented
        previous_values = {}

        for i in range(rows):
            row_values = []

            for column in self.data_specification:
                column_name = column['name']
                column_type = column['type']

                if column_name in previous_values:
                    previous_value = previous_values[column_name]
                    incrementor = self.incrementors[column_type]
                    next_value = incrementor.increment(
                            previous_values[column_name],
                            column)
                else:
                    next_value = column['start']

                previous_values[column_name] = next_value
                row_values.append(next_value)

            self.writer.writerow(row_values)

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
