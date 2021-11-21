@echo off
echo ========== RADIO PLAYER ==========
taskkill /f /im vlc.exe >nul 2>&1
echo - Stopped Playback!
echo ==================================
exit
