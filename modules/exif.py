import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

########################################
# Check if the directory exists.

def check_directory(directory):

    if not os.path.isdir(directory):
      print(f"ERROR! {directory} is not a valid directory or does not exist.")
      sys.exit(1)

########################################
# Get the creation date of the image
# based on the EXIF metadata.

def get_date(image_path):

    try:
      image = Image.open(image_path)
      exif  = image._getexif()
      
      if not exif:
        return None
      
      for tag, value in exif.items():
        tag_name = TAGS.get(tag, tag)

        if tag_name == 'DateTimeOriginal':
          return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')

    except Exception as e:
      print(f"ERROR! Failed to read EXIF from {image_path}: {e}")
      sys.exit(1)
    
    return None

########################################
# Return a sorted list of JPG files
# based on their creation date.

def get_sorted(directory):

    jpg_files = []

    print(f"Reading EXIF data from JPG files in {directory}")
    
    for filename in os.listdir(directory):

      if not filename.lower().endswith('.jpg') and not filename.lower().endswith('.jpeg'):
        continue
      
      filepath      = os.path.join(directory, filename)
      creation_date = get_date(filepath)
      
      if not creation_date:
        continue
      
      jpg_files.append((filename, creation_date))
    
    # Sort by creation date
    jpg_files.sort(key=lambda x: x[1])
    
    # Return only the filenames, sorted by date
    return [filename for filename, _ in jpg_files]

########################################
# Return a list of JPG files from the
# provided directory.

def get_files_list(directory):

    check_directory(directory)

    sorted = get_sorted(directory)

    return [os.path.join(directory, filename) for filename in sorted]