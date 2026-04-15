@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo ===================================================
echo  Planet Coaster 2 Turkce Yama - Kurulum
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

REM ----- 2. Kaynak klasoru kontrol -----
set "SRC_ROOT=TurkceYama\Main"
if not exist "!SRC_ROOT!\Content0\Localised\English\UnitedStates\Loc.ovl" (
    echo HATA: Kaynak dosyalar bulunamadi.
    echo Bu script, icerisinde "TurkceYama" klasoru bulunan dizinde calistirilmalidir.
    echo.
    echo Aranan: %CD%\!SRC_ROOT!\Content0\Localised\English\UnitedStates\Loc.ovl
    pause
    exit /b 1
)

REM ----- 3. Yedek durumunu tara -----
echo [2/3] Mevcut dosya durumu kontrol ediliyor...

set "PACKS=Content0 Content1 Content2 Content3 Content4 Content5 Content6 Content7 Content8 ContentAnniversary ContentFestive ContentPDLC1 ContentPDLC2 ContentPDLC3"
set /a HAS_BACKUP=0
set /a NO_BACKUP=0
set /a NO_TARGET=0

for %%P in (%PACKS%) do (
    for %%R in (UnitedStates UnitedKingdom) do (
        if exist "!GAME_DIR!\%%P\Localised\English\%%R\Loc.ovl.bak" (
            set /a HAS_BACKUP+=1
        ) else (
            if exist "!GAME_DIR!\%%P\Localised\English\%%R\Loc.ovl" (
                set /a NO_BACKUP+=1
            ) else (
                set /a NO_TARGET+=1
            )
        )
    )
)

echo.
echo --- Durum Raporu ---
echo   Orijinal yedegi zaten alinmis       : !HAS_BACKUP!
echo   Yedegi olmayan orijinal dosya       : !NO_BACKUP!
echo   Hedef dosya yok ^(yeni olusturulacak^): !NO_TARGET!
echo.
echo --- Yapilacak Islemler ---
if !NO_BACKUP! gtr 0 (
    echo   * Yedegi olmayan !NO_BACKUP! orijinal Ingilizce dosyanin .bak yedegi
    echo     ALINACAK, ardindan Turkce cevirisi ile degistirilecek.
)
if !HAS_BACKUP! gtr 0 (
    echo   * Yedegi zaten bulunan !HAS_BACKUP! dosya icin mevcut ceviri silinerek
    echo     yenisi ile degistirilecek. Orijinal .bak yedekleri korunacak.
)
if !NO_TARGET! gtr 0 (
    echo   * Hedefte olmayan !NO_TARGET! konuma yeni Turkce dosya kopyalanacak.
)
echo.

set "ANSWER="
set /p "ANSWER=Devam etmek istiyor musun? (E/H): "
if not defined ANSWER goto :cancel
if /i not "!ANSWER:~0,1!"=="E" goto :cancel

REM ----- 4. Kopyalama -----
echo.
echo [3/3] Dosyalar kopyalaniyor...
set /a COPIED=0
set /a BACKED_UP=0
set /a FAILED=0

for %%P in (%PACKS%) do (
    set "SRC=!SRC_ROOT!\%%P\Localised\English\UnitedStates\Loc.ovl"
    if exist "!SRC!" (
        for %%R in (UnitedStates UnitedKingdom) do (
            set "DST_DIR=!GAME_DIR!\%%P\Localised\English\%%R"
            set "DST=!DST_DIR!\Loc.ovl"
            set "BAK=!DST!.bak"

            if not exist "!DST_DIR!" mkdir "!DST_DIR!" >nul 2>&1

            if exist "!DST!" (
                if not exist "!BAK!" (
                    copy /Y "!DST!" "!BAK!" >nul 2>&1
                    if errorlevel 1 (
                        echo   %%P\%%R: YEDEK ALMA HATASI
                        set /a FAILED+=1
                    ) else (
                        set /a BACKED_UP+=1
                    )
                )
            )

            copy /Y "!SRC!" "!DST!" >nul 2>&1
            if errorlevel 1 (
                echo   %%P\%%R: KOPYALAMA HATASI
                set /a FAILED+=1
            ) else (
                set /a COPIED+=1
            )
        )
    ) else (
        echo   %%P: kaynak dosya yok, atlandi
    )
)

echo.
echo ===================================================
echo  Kurulum Tamamlandi
echo ===================================================
echo   Kopyalanan dosya   : !COPIED!
echo   Yedek alinan dosya : !BACKED_UP!
echo   Basarisiz islem    : !FAILED!
echo.
echo Oyunu ac, Ayarlar ^> Dil menusunden
echo   "English (United States)" veya "English (United Kingdom)"
echo sec. Turkce ceviriler etkin olacak.
echo.
pause
exit /b 0

:cancel
echo.
echo Kurulum iptal edildi.
pause
exit /b 0
