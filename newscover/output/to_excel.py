from processor import process_json
import argparse
import pandas as pd 
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fileName", required = True)

arg = parser.parse_args()

path1 = Path(__file__).parent / arg.fileName

df = process_json(path1)

