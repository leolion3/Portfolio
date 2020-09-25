@ECHO off
set param=%*
git add --ignore-errors %param% *
git commit -a
