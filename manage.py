# Python modules:
from pathlib import Path
from os import path
import argparse


# Argument parsing
parser = argparse.ArgumentParser(
    description="Organize & Timestamp Nintendo Switch Captures"
)

parser.add_argument(
    "input_filepath",
    type=Path,
    help="The full filepath for the 'Nintendo/Album' folder."
)

parser.add_argument(
    "output_filepath",
    type=Path,
    help="The folder where you want re-sorted files to go."
)

args = parser.parse_args()



from PIL import Image
image_thing = Image.open('./Output/droplet.png')
image_thing.show()