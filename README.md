# Ipsum Data

Simple tool for creating tabular series data from a data specification.

See the example data specification file in `examples` for an example of how to define the data characteristics.

## Example use

Install the module dependencies, e.g.

    $ cd path/to/this/directory
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Output to ipsum data to stdout

    $ python main.py --spec="path/to/spec.json" --rows="10"

Pipe stdout to a new csv file

    $ python main.py --spec="path/to/spec.json" --rows="10" > path/to/output.csv

## Demo

Run the demo using the using the spec file provided:

    $ python main.py --spec="examples/example-spec.json" --rows="10" > output.csv

This should generate a CSV file, output.csv, containing 10 rows of data.
