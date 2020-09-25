@echo off
set var=%*
netsh wlan show profile %var% key=clear
exit