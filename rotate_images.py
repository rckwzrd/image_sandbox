"""
rotate lazy-d images 90 degrees
"""

from PIL import Image
from pathlib import Path
import os

LAZY_IMAGES = Path('lazy_d_core_photos')
imgs = list(LAZY_IMAGES.glob('*.jpg'))

print(imgs[0])

for img in imgs:
    base = os.path.basename(img)
    root = os.path.dirname(img)
    SAVE_PATH = root + "/" + "ROTATED_" + base
    Image.open(img).rotate(90, expand=1).save(SAVE_PATH)
