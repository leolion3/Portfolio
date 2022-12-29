# Customize Powershell to look amazing

These customizations make powershell look sick :) 
Install Windows Terminal to make it look and function even better!

## Unix Tools

To use unix tools like nano/vim either install Chocolatey or install Git-SCM with the optional Unix Tools checked (latter is easier/quicker).

## Chocolatey

Install the choco package manager for Windows

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

## Fonts

Install CaskaydiaCove nerd fonts from

```html
https://www.nerdfonts.com/font-downloads
```

## Update PowershellGet

```powershell
Install-Module -Name PowerShellGet -Force
```

## Install PSReadLine

```powershell
Install-Module PSReadLine -AllowPrerelease -Force
```

## Install Posh-Git and Oh-My-Posh

```powershell
Install-Module posh-git -Scope CurrentUser
winget install JanDeDobbeleer.OhMyPosh -s winget
```

## Add Theme to powershell profile

```
nano $PROFILE
Import-Module posh-git
oh-my-posh init pwsh --config ~/.aliens.omp.json | Invoke-Expression
Set-PoshPrompt -Theme aliens
```

Themes available under 

```html
https://ohmyposh.dev/docs/themes/
```

## Add File Icons and Colors

```powershell
Install-Module -Name Terminal-Icons -Repository PSGallery
```

Add this to the $PROFILE file

```powershell
Import-Module -Name Terminal-Icons
```

## Add Autocomplete

Add this to the $PROFILE file

```powershell
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows
```

## Start New Windows Terminal Window in Last Location

Add this function to the end of the $PROFILE file:

```powershell
function z {
  param ([string]$newpath)
  cd $newpath
  $path = "$env:USERPROFILE\AppData\Local\Packages\Microsoft.WindowsTerminal_[YOUR_WT_VERSION]\LocalState\settings.json" 
  $todir = ("$pwd") -replace "\\","\\"  
   ((Get-Content -path $path)  -replace '("startingDirectory":)(.*")(.*)', ("`$1`"$todir`"`$3")) | Set-Content -Path $path
}
```

Now to change the working directory use the command 

```powershell
z target_directory
```

instead of "cd".

Kudos to the creator of the caching function 

```html
https://github.com/microsoft/terminal/issues/3158#issuecomment-817515727
```

## Powershell Profile File

The complete $PROFILE file looks like this:

```powershell
Import-Module posh-git
oh-my-posh init pwsh --config ~/.aliens.omp.json | Invoke-Expression
Import-Module -Name Terminal-Icons
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows

$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}

function z {
  param ([string]$newpath)
  cd $newpath
  $path = "$env:USERPROFILE\AppData\Local\Packages\Microsoft.WindowsTerminal_[YOUR_WT_VERSION]\LocalState\settings.json" 
  $todir = ("$pwd") -replace "\\","\\"  
   ((Get-Content -path $path)  -replace '("startingDirectory":)(.*")(.*)', ("`$1`"$todir`"`$3")) | Set-Content -Path $path
}
```

## Windows Terminal Settings

Add/Modify these in the **settings.json** File:

```json
"colorScheme": "myCampbell",
"fontFace": "CaskaydiaCove NF",
```

## Background

To add a background to your terminal, paste it in: 

```powershell
%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_[YOUR_VERSION_PATH]\RoamingState
```

Add this to the Windows Terminal JSON File under "default":

```json
"backgroundImage" : "ms-appdata:///roaming/yourimage.jpg",
"backgroundImageStretchMode" : "fill",
"useAcrylic" : true,
"acrylicOpacity" : 0.5,
```

# WSL

```bash
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
chmod +x /usr/local/bin/oh-my-posh
mkdir ~/.poshthemes
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip
unzip ~/.poshthemes/themes.zip -d ~/.poshthemes
chmod u+rw ~/.poshthemes/*.json
rm ~/.poshthemes/themes.zip
```

