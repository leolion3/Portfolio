@echo off
set var=%*
netsh wlan show profile %var%
exit
