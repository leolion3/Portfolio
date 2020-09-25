@ECHO off
set args=%*
git add *
git commit -a
git pull %args%
