@echo off
set args=%*
python -m http.server %args%
exit
