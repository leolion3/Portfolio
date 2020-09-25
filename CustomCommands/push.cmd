@ECHO off
set var=%*
git add --ignore-errors *
git commit -a
git pull
git push %var%
