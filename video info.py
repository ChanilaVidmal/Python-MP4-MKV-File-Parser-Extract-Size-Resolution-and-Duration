import av
import os
import warnings

# Define the directory containing the video files
directory = input("Enter the directory path: ")

# Loop through each directory and subdirectory in the directory
for root, _, files in os.walk(directory):
    # Loop through each file in the current directory or subdirectory
    for file in files:
        # Check if the file is an MP4 or MKV file
        if file.endswith('.mp4') or file.endswith('.mkv'):
            # Open the video file
            container = av.open(os.path.join(root, file))

            # Get the video stream
            stream = container.streams.video[0]

            # Get the file size
            size = os.path.getsize(os.path.join(root, file))

            # Convert the file size to a more human-readable format
            size_name = ("", "KB", "MB", "GB", "TB", "PB")
            i = 0
            while size >= 1024 and i < len(size_name) - 1:
                size /= 1024
                i += 1
            size = f"{round(size, 2)} {size_name[i]}"

            # Get the resolution
            resolution = f"{stream.width}x{stream.height}"

            # Get the duration
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                duration_sec = container.duration / av.time_base

            duration_hms = str(int(duration_sec // 3600)).zfill(2) + ':' + \
                           str(int((duration_sec % 3600) // 60)).zfill(2) + ':' + \
                           str(int(duration_sec % 60)).zfill(2)

            # Print the file name, size, resolution, and duration in hh:mm:ss format
            print("File: {}\nSize: {}\nResolution: {}\nDuration: {}\n".format(
                os.path.join(root, file),
                size,
                resolution,
                duration_hms if stream.index == 0 else "unknown"
            ))
