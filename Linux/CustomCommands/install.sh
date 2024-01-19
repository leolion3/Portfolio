#!/bin/bash
echo ''
echo '\033[0;33m===== Custom Commands by Leonard Haddad ====='
echo '\033[0;36mGithub: https://github.com/leolion3'
echo '\033[0;36mWebsite: https://leolion.tk/'
echo '\033[0;36mProvided in accords with the MIT licence'
echo '\033[0;33m=============================================\033[1;32m'
echo ''
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
cd ~

# Download components
mkdir -p commands
cd commands
echo '[INFO] Downloading executables...'
curl -LkSs https://api.github.com/repos/leolion3/Portfolio/tarball -o master.tar.gz
tar -xzf master.tar.gz --strip-components=1
cd ..

# Move to corrent location
cmd_dir='.commands'
echo "[INFO] Creating executables path $cmd_dir..."
mkdir -p "$cmd_dir"
mv commands/Linux/CustomCommands/* "./$cmd_dir/"
mv commands/Python/FileSender/ptransfer "./$cmd_dir/"
mv commands/Python/PasswordUtils/passtransfer "./$cmd_dir/"
mv commands/Python/KeepBusy/keepbusy* "./$cmd_dir/"
mv commands/Python/PasswordVault/passwordVault.py "./$cmd_dir/pv"

# Cleanup
rm -rf commands/

# Ready components
cd "$cmd_dir/"
rm "README.md"
rm "install.sh"
chmod +x ./ptransfer
chmod +x ./passtransfer
chmod +x ./keepbusy
chmod +x ./keepbusy_cross
chmod +x ./pv

echo "Please add this to your terminal's rc file: export PATH=\"$PWD:\$PATH\""
