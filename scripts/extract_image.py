"""
Author: Alex Reichenbach
Date: May 5, 2022

The goal of this script is to test whether
the image extraction works.
"""

import click
import matplotlib.pyplot as plt

from GraphWorld.config import ImageExtractorOptions
from GraphWorld.src.data import get_data_source
from GraphWorld.src.nn.image.ObjectExtractor import ImageExtractor

def extract_object(image):
    """
    Extract an object from an image using the specified
    criterium
    """
    opts = ImageExtractorOptions()
    
    extractor = ImageExtractor(opts)
    obj = extractor.extract_image()
    return obj

def visualize_object(obj, visualize=False, save_path=None):
    """
    Just visualize the segmentation
    """
    plt.imshow(obj)
    plt.show()

@click.command()
@click.argument("image")
@click.option("--object_database")
@click.option("--visualize/--no-visualize", type=bool, default=True)
@click.option("--save_path", type=str)
def main(image, object_database, visualize, save_path):
    obj = extract_object(image)
    if visualize:
        visualize_object(obj)

    if save_path is not None:
        visualize_object(obj, visualize=False, save_path=True)

if __name__ == "__main__":
    main()
