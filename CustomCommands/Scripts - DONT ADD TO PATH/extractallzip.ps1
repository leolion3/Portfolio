gci -Recurse -Filter *.zip |ForEach-Object {$n=($_.Fullname.trimend('.zip')); Expand-Archive -Path $_.Fullname -DestinationPath $n -Force}
