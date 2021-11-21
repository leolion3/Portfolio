@echo off
set args=%*
powershell -Version 5.1 -NoProfile -ep Bypass -File /PATH/TO/FileHash.ps1 %args%
exit
