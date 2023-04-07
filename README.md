# MP4 and MKV file parser

This Python script is used to parse MP4 and MKV files and extract their file size, resolution, and duration in hh:mm:ss format.

## Requirements

This script requires the `av` package to be installed. You can install it via pip:

```bash
pip install av
```

## Usage

To use this script, run it from the command line and enter the directory path containing the MP4 and MKV files when prompted:

```bash
python mp4_mkv_parser.py
Enter the directory path: /path/to/directory
```
The script will then loop through each file in the specified directory and its subdirectories, and output the file name, size, resolution, and duration in hh:mm:ss format:

```bash
File: /path/to/directory/video.mp4
Size: 12.34 MB
Resolution: 1920x1080
Duration: 00:10:05

File: /path/to/directory/subdirectory/video.mkv
Size: 4.56 GB
Resolution: 3840x2160
Duration: 01:23:45
```
If the start time for stream 2 is not set, the duration for that stream will be displayed as "unknown".
## License

This script is released under the [MIT License.](https://choosealicense.com/licenses/mit/)

## Authors

- [@ChanilaVidmal](https://github.com/ChanilaVidmal)

