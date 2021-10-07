# Youtube to MP3 Downloader

This tool allows you to simply copy a link of a youtube video to your clipboard, which will automatically start downloading that video to MP3.
It can also be used on playlists, where it will then download the entire thing.

## Requirements

To use this tools, the following libraries are required:

```python
youtube-dl
ffmpeg
ffprobe
```

Alternatively to ffprobe, one might use avprobe on Linux.

Using 

```bash
pip install ffmpeg
```

on Windows often doesn't work, thats why the file ffmpeg.encoded ist included. To get the exe, simply execute

```cmd
certutil -decode ffmpeg.encoded ffmpeg.exe
```

The SHA-256 checksum for the exe is

```
55720D404B2476631C82F1EFB636A2244BBEB1E197373D553EA724CA1B2A23FE
```

then paste the exe in 

```
Python3x/Scripts
```

and add the folder to PATH.

##  License

Provided under the MIT License. Please note that local regulations differ from region to region, and usage of this tool may therefor be prohibited! I do not take responsibility for any damages caused by the use of this script.

## Author

Author: Leonard Haddad
