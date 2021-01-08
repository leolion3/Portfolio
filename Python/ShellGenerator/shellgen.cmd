@echo off
set exportpath=%cd%
set templatepath=path_to_template_file\Template.txt
set vars=%*
python path_to_script\shellgen.py %exportpath% %templatepath% %vars%
exit
