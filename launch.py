import os
import sys
import modules as m

if __name__ == "__main__":

    if len(sys.argv) != 2:
      print("ERROR! Invalid number of arguments provided.")
      print(f"Usage: python {sys.argv[0]} <argument>")
      sys.exit(1)

    input_path = sys.argv[1]

    if not input_path.endswith('/'):
      input_path += '/'

    sorted_jpg_files = m.exif.get_files_list(input_path)
    divided_files    = m.utils.divide_list(sorted_jpg_files)

    for idx, files in enumerate(divided_files):

      output = input_path + f"output{idx}.psd"

      if os.path.exists(output):

        print(f"The file '{output}' already exists")
        response = input(f"Do you want to overwrite it? (y/n): ").strip().lower()

        if response != 'y':
          print("Exiting.")
          sys.exit(1)

      print(f"Processing group #{idx} of {len(files)} files to {output}")
      m.layers.create_layers(files, output)

      print(f"Layered image saved as {output}")
