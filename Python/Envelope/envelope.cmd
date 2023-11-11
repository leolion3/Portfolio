@echo off
cp /mypath/to\Envelope.docx .
cp /mypath/to\envelope.py .
python envelope.py %*
rm envelope.py
exit
