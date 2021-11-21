param(
    [string]$hash,
    [string]$file,
    [string]$algorithm
)

if ($hash -eq '' -or $file -eq '' -or $algorithm -eq ''){
    echo "Missing a parameter!"
    echo "Usage: hashcmp integrity_hash file_path algorithm"
    exit
}

Function Get-FileHash
{
    param (
        [String] $FileName,
        [String] $HashName
    )
    $FileStream = New-Object System.IO.FileStream($FileName,[System.IO.FileMode]::Open)
    $StringBuilder = New-Object System.Text.StringBuilder
    [System.Security.Cryptography.HashAlgorithm]::Create($HashName).ComputeHash($FileStream)|%{[Void]$StringBuilder.Append($_.ToString("x2"))}
    $FileStream.Close()
    return $StringBuilder.ToString()
}

$filehash = Get-FileHash $file $algorithm
if ($filehash -eq $hash) {echo "Hashes match!"} else {echo "Filehash doesn't match!"}
