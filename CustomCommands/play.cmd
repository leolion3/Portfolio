@echo off
echo ========== RADIO PLAYER ==========

if "%~1"=="" (
goto help
)

set player=%1
goto %player%

:ndr2
start vlc --intf dummy https://ndr-ndr2-niedersachsen.cast.addradio.de/ndr/ndr2/niedersachsen/mp3/128/stream.mp3
goto playing

:ffn
start vlc --intf dummy https://stream.ffn.de/ffn/mp3-192/?ref=radioplayer
goto playing

:rotana
start vlc --intf dummy http://curiosity.shoutca.st:6035
goto playing

:help
echo Plays different radio stations
echo Usage: 
echo [ play.cmd station_name ] 
echo [ play.cmd stop ]
echo ----------------------------------
echo Current list of stations:
echo - ffn 
echo - ndr2
echo - rotana (Rotana Radio Jordan)
if "%~1"=="" (
	echo ----------------------------------
	echo No station selected, using default!
	set player=ffn
	goto ffn
)
goto exit

:playing
echo - Playing Radio: %player%%
goto exit

:stop
taskkill /f /im vlc.exe >nul 2>&1
echo - Stopped Playback!
goto exit

:exit
echo ==================================
exit
