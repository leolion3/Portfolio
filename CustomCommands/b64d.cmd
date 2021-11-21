@echo off
set var=%1
if NOT "%~2"=="" goto b
set svar="decoded"

:a
certutil -decode %var% %svar%
exit

:b
set svar=%2
goto a
