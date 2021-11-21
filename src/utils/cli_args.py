import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='count', default=0, help="verbosity level")

args = parser.parse_args()
