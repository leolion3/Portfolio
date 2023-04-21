# Customize Powershell to look amazing

These customizations make powershell look sick :) 

## Prerequisites

For the installation to run successfully, please make sure you are using [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701) and are using [Powershell 7](https://apps.microsoft.com/store/detail/powershell/9MZ1SNWT0N5D?hl=de-de&gl=de&rtc=1) (otherwise PowerShellGet and other modules will not be installable). Also, make sure that running of Powershell scripts is enabled with `Set-ExecutionPolicy RemoteSigned`.

## Contents

This guide offers multiple add-ons for Powershell (and Windows Terminal) in general. These are:

- **Unix Toolkit** (installable using Git SCM): Allows using tools like standard curl, OpenSSL and similar unix tools.
- **Chocolatey** as a package manager.
- **Oh-My-Posh** (Powershell version of `oh-my-zsh`)
- **WSL Customization**

**Note** that if you would like to use regular `curl`, you have to add the command `Remove-Item Alias:curl` to your PowerShell's `$PROFILE` file, since it has an alias for `Invoke-WebRequest` in PowerShell, which does not support the native curl syntax.

---

## Unix Tools

To use unix tools like nano/vim either install Chocolatey or install [Git-SCM](https://git-scm.com/) **with the optional Unix Tools checked** (latter is easier/quicker).

---

## Chocolatey

Install the choco package manager for Windows

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

---

## Fonts

The Caskaydia Cove Nerd Font allows rendering Documents, Git and other Icons within Windows Terminal. To install them, either download the **Caskaydia Cove Nerd Font** from here:

```html
https://www.nerdfonts.com/font-downloads
```

Or [click here](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/CascadiaCode.zip).

---

## Oh-My-Posh

This section describes how to install `Oh-My-Posh` to decorate your terminal in a fashion similar to `oh-my-zsh`. The available themes can be found [here](https://ohmyposh.dev/docs/themes).

### Update PowerShellGet

First of all, update `PowerShellGet` since it is probably outdated.

```powershell
Install-Module -Name PowerShellGet -Force
```

### Install PSReadLine

Then install `PSReadLine` to allow shell line customization and recoloring.

```powershell
Install-Module PSReadLine -AllowPrerelease -Force
```

### Install Posh-Git and Oh-My-Posh

Next up, install `Oh-My-Posh` and `Posh-Git`.

```powershell
Install-Module posh-git -Scope CurrentUser
winget install JanDeDobbeleer.OhMyPosh -s winget
```

### Add Theme to powershell profile

Add the following to your PowerShell's `$PROFILE` file to enable `Oh My Posh` on terminal launch. Note that the theme (below set to `aliens`) can be changed to any of the ones available [here](https://ohmyposh.dev/docs/themes) by changing the name `aliens` to the corresponding one.

```bash
nano $PROFILE
Import-Module posh-git
oh-my-posh init pwsh --config ~/.aliens.omp.json | Invoke-Expression
Set-PoshPrompt -Theme aliens
```

### Add File Icons and Colors

To enable file type highlighting and icons, install the following package.

```powershell
Install-Module -Name Terminal-Icons -Repository PSGallery
```

Then add this to your PowerShell's `$PROFILE` file

```powershell
Import-Module -Name Terminal-Icons
```

### Add Autocomplete

To enable autocompleting commands and command history, add the following to your PowerShell's `$PROFILE` file

```powershell
Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView
Set-PSReadLineOption -EditMode Windows
```

---

## Start New Windows Terminal Window in Last Location

If you would like new PowerShell instances to be launched from the folder you were lastly inside of, add the following function to your PowerShell's `$PROFILE` file:

```powershell
function z {
  param ([string]$newpath)
  cd $newpath
  $path = "$env:USERPROFILE\AppData\Local\Packages\Microsoft.WindowsTerminal_[YOUR_WT_VERSION]\LocalState\settings.json" 
  $todir = ("$pwd") -replace "\\","\\"  
   ((Get-Content -path $path)  -replace '("startingDirectory":)(.*")(.*)', ("`$1`"$todir`"`$3")) | Set-Content -Path $path
}
```

Now when changing directories, use the `z targetDirectory/` command instead of `cd targetDirectory/`. Do note that if the directory gets deleted you might encounter a PowerShell launch error and need to start it in a profileless mode to change the directory. 

```powershell
z target_directory
```

Kudos to the creator of the caching function[^1]

[^1]: https://github.com/microsoft/terminal/issues/3158#issuecomment-817515727

---

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

---

## Windows Terminal Settings

### New way (2023)

Change the Color Scheme and font used within Windows Terminal's Settings to **colorScheme** - `myCampbell` and **font face** - `CaskaydiaCove NF`.

### Old way

Add/Modify these in the **settings.json** File:

```json
"colorScheme": "myCampbell",
"fontFace": "CaskaydiaCove NF",
```

## Background

### New Way (2023)

Open Windows Terminal's settings and add the background in the designated spot.

To increase readability, change the **foreground font's color** to `lime` or `pink` and **enable opacity**, while setting the **background's opacity** to `50%`. If the background does not fill the entire console, set its mode to `stretch`.

### Old Way

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

---

## Custom Commands

For advanced users who wish to make their lives easier, you can use the custom command toolkit provided by me [here](https://github.com/leolion3/Portfolio/tree/master/CustomCommands). These are regularily updated with increasing functionality, so it might be wise to keep them within the repository and somehow link them to your environment variables (symlinks in Windows can be created with `mklink /D target/directory linkName` for directories and `mklink target/file/path linkName`).

---

# WSL

The bellow commands add `oh-my-zsh` to your WSL installation (they have to be executed in a valid WSL installation). To further customize the shell, check out [this README](https://github.com/leolion3/Portfolio/tree/master/Linux/Customization/Oh-My-Zsh).

```bash
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
chmod +x /usr/local/bin/oh-my-posh
mkdir ~/.poshthemes
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip
unzip ~/.poshthemes/themes.zip -d ~/.poshthemes
chmod u+rw ~/.poshthemes/*.json
rm ~/.poshthemes/themes.zip
```

