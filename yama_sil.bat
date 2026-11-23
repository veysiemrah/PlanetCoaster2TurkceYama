@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo ===================================================
echo  Planet Coaster 2 Turkce Yama - Kaldirma
echo ===================================================
echo.

REM ----- 1. Oyun dizinini bul -----
set "GAME_DIR="
echo [1/3] Oyun kurulum yolu araniyor...
echo.

for %%D in (C D E) do (
    if not defined GAME_DIR if exist "%%D:\XboxGames\Planet Coaster 2\Content\Win64\ovldata" (
        set "GAME_DIR=%%D:\XboxGames\Planet Coaster 2\Content\Win64\ovldata"
        echo   Xbox Game Pass bulundu: %%D:
    )
)

for %%D in (C D E) do (
    if not defined GAME_DIR if exist "%%D:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata" (
        set "GAME_DIR=%%D:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata"
        echo   Steam bulundu: %%D:\Program Files ^(x86^)\Steam
    )
    if not defined GAME_DIR if exist "%%D:\Program Files\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata" (
        set "GAME_DIR=%%D:\Program Files\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata"
        echo   Steam bulundu: %%D:\Program Files\Steam
    )
    if not defined GAME_DIR if exist "%%D:\SteamLibrary\steamapps\common\Planet Coaster 2\Win64\ovldata" (
        set "GAME_DIR=%%D:\SteamLibrary\steamapps\common\Planet Coaster 2\Win64\ovldata"
        echo   Steam kutuphanesi bulundu: %%D:\SteamLibrary
    )
    if not defined GAME_DIR if exist "%%D:\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata" (
        set "GAME_DIR=%%D:\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata"
        echo   Steam bulundu: %%D:\Steam
    )
)

REM Epic Games: once launcher manifestlerinden gercek kurulum yolunu oku
set "EPIC_MANIFESTS=%ProgramData%\Epic\EpicGamesLauncher\Data\Manifests"
if not defined GAME_DIR if exist "%EPIC_MANIFESTS%\*.item" (
    for /f "delims=" %%F in ('findstr /m /i /c:"Planet Coaster 2" "%EPIC_MANIFESTS%\*.item" 2^>nul') do (
        if not defined GAME_DIR (
            for /f "tokens=1,* delims=:" %%A in ('findstr /i /c:"InstallLocation" "%%F" 2^>nul') do (
                if not defined GAME_DIR (
                    set "EPIC_LOC=%%B"
                    call :normalize_path EPIC_LOC
                    if exist "!EPIC_LOC!\Content0" (
                        set "GAME_DIR=!EPIC_LOC!"
                        echo   Epic Games bulundu: !GAME_DIR!
                    )
                )
            )
        )
    )
)

REM Epic Games: varsayilan kurulum klasorleri
for %%D in (C D E) do (
    for %%N in ("PlanetCoaster2" "Planet Coaster 2") do (
        if not defined GAME_DIR if exist "%%D:\Program Files\Epic Games\%%~N\Win64\ovldata" (
            set "GAME_DIR=%%D:\Program Files\Epic Games\%%~N\Win64\ovldata"
            echo   Epic Games bulundu: %%D:\Program Files\Epic Games\%%~N
        )
        if not defined GAME_DIR if exist "%%D:\Epic Games\%%~N\Win64\ovldata" (
            set "GAME_DIR=%%D:\Epic Games\%%~N\Win64\ovldata"
            echo   Epic Games bulundu: %%D:\Epic Games\%%~N
        )
    )
)

if not defined GAME_DIR (
    echo   Otomatik bulunamadi.
    echo.
    echo Lutfen oyunun kurulu oldugu ovldata dizinini gir.
    echo Ornek: C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata
    echo.
    set /p "GAME_DIR=Yol: "
    if not defined GAME_DIR goto :cancel
    call :normalize_path GAME_DIR
    if not defined GAME_DIR goto :cancel
    if not exist "!GAME_DIR!" (
        echo HATA: "!GAME_DIR!" bulunamadi.
        pause
        exit /b 1
    )
)

if not exist "!GAME_DIR!\Content0" (
    echo.
    echo HATA: "!GAME_DIR!" gecerli bir ovldata dizini degil.
    echo Bu klasorun icinde Content0, Content1 ... klasorleri olmali.
    echo Oyunun ana klasorunu girdiysen sonuna \Win64\ovldata ekleyerek dene.
    pause
    exit /b 1
)

echo.
echo Hedef dizin: !GAME_DIR!
echo.

REM ----- 2. Yedek durumunu tara -----
echo [2/3] Yedek dosyalar kontrol ediliyor...

set "PACKS=Content0 Content1 Content2 Content3 Content4 Content5 Content6 Content7 Content8 ContentAnniversary ContentFestive ContentPDLC1 ContentPDLC2 ContentPDLC3"
set /a FOUND=0
set /a NO_BACKUP=0

for %%P in (%PACKS%) do (
    for %%R in (UnitedStates UnitedKingdom) do (
        if exist "!GAME_DIR!\%%P\Localised\English\%%R\Loc.ovl.bak" (
            set /a FOUND+=1
        ) else (
            if exist "!GAME_DIR!\%%P\Localised\English\%%R\Loc.ovl" (
                set /a NO_BACKUP+=1
            )
        )
    )
)

echo.
echo --- Durum Raporu ---
echo   Geri yuklenecek yedek dosya        : !FOUND!
echo   Yedegi olmayan dosya ^(atlanacak^)  : !NO_BACKUP!
echo.

if !FOUND! == 0 (
    echo HATA: Hicbir yedek dosya ^(.bak^) bulunamadi.
    echo Muhtemelen yama kurulmamis ya da yedekler silinmis.
    echo.
    echo Alternatif olarak oyun dosyalarini dogrulayabilirsin:
    echo   * Steam: "Dosya butunlugunu dogrula"
    echo   * Xbox Game Pass: oyunu kaldirip yeniden kur
    echo.
    pause
    exit /b 1
)

echo --- Yapilacak Islemler ---
echo   * Yalnizca YEDEKLI !FOUND! dosya silinip .bak ile geri yuklenecek
echo   * Yedegi olmayan dosyalar korunacak, ASLA silinmeyecek
echo   * Turkce yama kaldirilacak, orijinal Ingilizce metinler geri gelecek
echo.

set "ANSWER="
set /p "ANSWER=Devam etmek istiyor musun? (E/H): "
if not defined ANSWER goto :cancel
if /i not "!ANSWER:~0,1!"=="E" goto :cancel

REM ----- 3. Geri yukleme -----
echo.
echo [3/3] Orijinal dosyalar geri yukleniyor...
set /a RESTORED=0
set /a SKIPPED=0
set /a FAILED=0

for %%P in (%PACKS%) do (
    for %%R in (UnitedStates UnitedKingdom) do (
        set "DST=!GAME_DIR!\%%P\Localised\English\%%R\Loc.ovl"
        set "BAK=!DST!.bak"

        if exist "!BAK!" (
            REM Yedek var - guvenli sekilde sil+geri yukle
            if exist "!DST!" del /F /Q "!DST!" >nul 2>&1
            ren "!BAK!" "Loc.ovl" >nul 2>&1
            if errorlevel 1 (
                echo   %%P\%%R: GERI YUKLEME HATASI
                set /a FAILED+=1
            ) else (
                set /a RESTORED+=1
            )
        ) else (
            REM Yedek yok - mevcut dosya korunur, SILINMEZ
            if exist "!DST!" (
                echo   %%P\%%R: yedek yok, dosya korundu
                set /a SKIPPED+=1
            )
        )
    )
)

echo.
echo ===================================================
echo  Yama Kaldirma Tamamlandi
echo ===================================================
echo   Geri yuklenen dosya       : !RESTORED!
echo   Yedek yok, korunan dosya  : !SKIPPED!
echo   Basarisiz islem           : !FAILED!
echo.
echo Oyunu baslat; orijinal Ingilizce metinler aktif olacak.
echo.
pause
exit /b 0

:cancel
echo.
echo Islem iptal edildi.
pause
exit /b 0

REM ----- Yardimci: yol temizleme / ovldata tamamlama -----
REM Tirnaklari, bas/son bosluklari, JSON kacislarini (\\) ve sondaki \ ile ,
REM karakterlerini temizler. Oyun ana klasoru verilmisse ovldata'yi ekler.
:normalize_path
set "NP=!%~1!"
if not defined NP goto :normalize_done
set "NP=!NP:"=!"
set "NP=!NP:\\=\!"
for /f "tokens=*" %%X in ("!NP!") do set "NP=%%X"
:normalize_trim
if not defined NP goto :normalize_done
if "!NP:~-1!"==" " set "NP=!NP:~0,-1!" & goto :normalize_trim
if "!NP:~-1!"=="," set "NP=!NP:~0,-1!" & goto :normalize_trim
if "!NP:~-1!"=="\" set "NP=!NP:~0,-1!" & goto :normalize_trim
if not exist "!NP!\Content0" (
    if exist "!NP!\Win64\ovldata\Content0" (
        set "NP=!NP!\Win64\ovldata"
    ) else if exist "!NP!\Content\Win64\ovldata\Content0" (
        set "NP=!NP!\Content\Win64\ovldata"
    ) else if exist "!NP!\ovldata\Content0" (
        set "NP=!NP!\ovldata"
    )
)
:normalize_done
set "%~1=!NP!"
exit /b 0
