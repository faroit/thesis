#!/usr/bin/env python

from PIL import Image
import sys

im = Image.open(sys.argv[1])

im.resize((int(sys.argv[2]), int(sys.argv[3])), Image.NEAREST).save(sys.argv[4])