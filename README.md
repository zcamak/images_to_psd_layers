# images_to_psd_layers
Make PSD files with layers created from JPG images and sorted by date of creation.

## Table of Contents
- [Usage](#usage)
- [Setup](#setup)
- [Installation](#installation)

## Usage
To create a PSD file with layers from JPG images sorted by date of creation, run the following command:
```bash
python launch.py /path/to/jpg/images
```

Output PSD files will be created inside directory with provided path as outputX.psd.

## Note
Due to limitation of file size in GIMP there might be created couple output files.
Number of output files is approximated. If you need to change of number of files
just edit function modules/utils.py/divide_list()

## Setup
1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/images_to_psd_layers.git
  cd images_to_psd_layers
  ```

2. Set up a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

## Installation
Install the required modules using pip:
```bash
pip install -r requirements.txt
```
