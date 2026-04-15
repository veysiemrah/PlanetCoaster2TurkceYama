# Yerel build + zip + GitHub Release upload
# Kullanim: .\tools\release.ps1 -Version v1.0.1 -GameDir "C:\XboxGames\Planet Coaster 2"

param(
    [Parameter(Mandatory=$true)][string]$Version,
    [string]$GameDir = "C:\XboxGames\Planet Coaster 2"
)

$ErrorActionPreference = "Stop"
# Versionsuz dosya adi - /releases/latest/download/PC2_TR_Yama.zip ile dogrudan link
$ZipName = "PC2_TR_Yama.zip"

Write-Host "[1/4] Validator calistiriliyor..." -ForegroundColor Cyan
& .\venv\Scripts\python.exe tools/validate.py
if ($LASTEXITCODE -ne 0) { throw "Validator basarisiz." }

Write-Host "`n[2/4] OVL build aliniyor..." -ForegroundColor Cyan
& .\venv\Scripts\python.exe tools/build.py --game-dir $GameDir --output build/
if ($LASTEXITCODE -ne 0) { throw "Build basarisiz." }

Write-Host "`n[3/4] Zip paketi hazirlaniyor..." -ForegroundColor Cyan
if (Test-Path release_pkg) { Remove-Item -Recurse -Force release_pkg }
New-Item -ItemType Directory -Path release_pkg | Out-Null
Copy-Item -Recurse build/TurkceYama release_pkg/
Copy-Item kurulum.bat, orijinal.bat, README.md, LICENSE release_pkg/
Copy-Item -Recurse docs release_pkg/
if (Test-Path $ZipName) { Remove-Item $ZipName }
Compress-Archive -Path release_pkg/* -DestinationPath $ZipName

Write-Host "`n[4/4] GitHub Release'e yukleniyor..." -ForegroundColor Cyan
& gh release upload $Version $ZipName --clobber

Write-Host "`nTamamlandi: $ZipName" -ForegroundColor Green
Remove-Item -Recurse -Force release_pkg
Remove-Item $ZipName
