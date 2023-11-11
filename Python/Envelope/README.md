# DL Envelope Generator

This script allows quickly generating printable DL envelope docx files.

## Setup

### Libs

First, install the required python modules:

```bash
pip install -r requirements.txt
```

### Docx

Then open the `.docx` file and enter your personal details (And replace the IsraTech logo with your own. If you decide to remove it, change the image in the python script from `word/media/image2.png` to `word/media/image1.png`. It would be easier to replace it with a blank image). **Do not replace the default stamp or the BLANK entries!**

### Shell

The script comes with a `.cmd` script which allows you to generate the stamp in any directory you want. **Never execute the script in the default directory, as then the template will be overwritten!**

To use this script, add it to a folder within your system's PATH, and replace the `/mypath/to` within it to the paths of the `docx` template and `.py` script's.

If done correctly, this allows you to execute `envelope` within any path to quickly generate printable docx files.

## Usage

The script allows you to generate DL envelope templates with and without stamps. To quickly generate a docx template without a stamp, just execute `envelope` within a path and fill out the details as shown in the screenshot below.

![Demo picture <i class="fa fa-external-link"></i>](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/Envelope/media/demo.png)

To add a stamp, get yourself a printable PDF stamp from your post office provider with cut-out marks around the corners ([see the `testprint_deutsche_post.pdf` file <i class="fa fa-external-link"></i>](https://raw.githubusercontent.com/leolion3/Portfolio/master/Python/Envelope/testprint_deutsche_post.pdf)) and execute the script with the pdf file as the first argument `envelope test_deutsche_post.pdf`. This will make you enter the details like in the default mode, but substitute the template file within the docx template with the printable stamp. If you'd like to try this mode, go ahead and do some with the provided stamp.

Now just open the docx file and print it! Viola!