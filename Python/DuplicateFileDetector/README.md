# Duplicate File Detector

This tool attempts to locate duplicate files and prompts you for deletion if files are found.

The script can be changed to only detect specific file extensions by commenting in the removed lines.
The detection sensitivity is set to 90% by default (just seemed to yield good results for my use-case) and can be adjusted as needed.

## Demo

```bash
python3 ./duplicate_filte_deleter.py
Enter the directory to search for duplicate files: ./
```

Output:

![Demo image](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/DuplicateFileDetector/media/demo.png)