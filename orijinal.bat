@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo ===================================================
echo  Planet Coaster 2 Turkce Yama - Orijinal Geri Yukle
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

if not defined GAME_DIR (
    echo   Otomatik bulunamadi.
    echo.
    echo Lutfen oyunun kurulu oldugu ovldata dizinini gir.
    echo Ornek: C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata
    echo.
    set /p "GAME_DIR=Yol: "
    if not defined GAME_DIR goto :cancel
    if not exist "!GAME_DIR!" (
        echo HATA: "!GAME_DIR!" bulunamadi.
        pause
        exit /b 1
    )
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
echo   * !FOUND! adet Loc.ovl silinecek
echo   * Her Loc.ovl.bak, Loc.ovl olarak yeniden adlandirilacak
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
set /a FAILED=0

for %%P in (%PACKS%) do (
    for %%R in (UnitedStates UnitedKingdom) do (
        set "DST=!GAME_DIR!\%%P\Localised\English\%%R\Loc.ovl"
        set "BAK=!DST!.bak"

        if exist "!BAK!" (
            if exist "!DST!" del /F /Q "!DST!" >nul 2>&1
            ren "!BAK!" "Loc.ovl" >nul 2>&1
            if errorlevel 1 (
                echo   %%P\%%R: GERI YUKLEME HATASI
                set /a FAILED+=1
            ) else (
                set /a RESTORED+=1
            )
        )
    )
)

echo.
echo ===================================================
echo  Geri Yukleme Tamamlandi
echo ===================================================
echo   Geri yuklenen dosya : !RESTORED!
echo   Basarisiz islem     : !FAILED!
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
