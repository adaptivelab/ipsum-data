# Ipsum Data

Simple tool for creating tabular series data from a data specification.

See the example data specification file in `examples` for an example of how to define the data characteristics.

## Example use

To get setup

    $ cd path/to/this/directory
    $ virtualenv env
    $ source env/bin/activate
    $ pip install

Then to generate a new csv file

    $ python main.py --spec="path/to/spec.json" --rows="10" > path/to/output.csv
