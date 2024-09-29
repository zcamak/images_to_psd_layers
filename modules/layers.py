import sys
from psd_tools import PSDImage
from psd_tools.api.layers import PixelLayer
from PIL import Image

def progress_bar(iteration, total, name, length=30):

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled  = int(length * iteration // total)
    bar     = '#' * filled + '.' * (length - filled)

    sys.stdout.write(f'\r[{bar}] {percent}% [{name}]')
    sys.stdout.flush()

def create_layers(jpg_files, output):

    try:

      count = 0
      total = len(jpg_files)

      width, height = Image.open(jpg_files[0]).size

      print(f"Creating a layered image with dimensions {width}x{height}")

      psd = PSDImage.new("RGBA", (width, height), 0, 8)

      print(f"Processing {total} input image to layers")

      for jpg_file in jpg_files:
        #print(f"Adding {jpg_file} as a layer")
        image = Image.open(jpg_file).convert("RGBA")
        layer = PixelLayer.frompil(image, psd)

        psd.append(layer)

        count += 1
        progress_bar(count, total, jpg_file)

      print(f"\nSaving layered image with {count} layers to output file")
      psd.save(output)

      return

    except Exception as e:
      print(f"ERROR! Failed to create layered image: {e}")
      sys.exit(1)
