@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo ===================================================
echo  Planet Coaster 2 Turkce Yama - Kurulum
echo ===================================================
echo.

REM Yonetici olarak yeniden baslatma icin yardimci degiskenler
set "PC2TR_SELF=%~f0"
set "PC2TR_PATHFILE=%TEMP%\pc2tr_oyun_yolu.txt"

REM ----- 1. Oyun dizinini bul -----
set "GAME_DIR="
echo [1/3] Oyun kurulum yolu araniyor...
echo.

REM Yonetici olarak yeniden baslatildiysa onceki pencerenin buldugu yolu kullan
if /i "%~1"=="/yonetici" if exist "%PC2TR_PATHFILE%" (
    set /p GAME_DIR=<"%PC2TR_PATHFILE%"
    del /f /q "%PC2TR_PATHFILE%" >nul 2>&1
    if defined GAME_DIR echo   Onceki pencerede bulunan yol kullaniliyor.
)

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

REM ----- Yazma izni kontrolu -----
call :check_write
if errorlevel 1 goto :need_admin

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
if !FAILED! gtr 0 (
    echo  Kurulum TAMAMLANAMADI
) else (
    echo  Kurulum Tamamlandi
)
echo ===================================================
echo   Kopyalanan dosya   : !COPIED!
echo   Yedek alinan dosya : !BACKED_UP!
echo   Basarisiz islem    : !FAILED!
echo.
if !FAILED! gtr 0 (
    echo UYARI: !FAILED! islem basarisiz oldu, yama eksik kurulmus olabilir.
    echo Oyunu kapat, kurulum.bat dosyasina sag tikla ve
    echo "Yonetici olarak calistir" ile tekrar dene. Sorun devam ederse
    echo bu ekranin goruntusunu GitHub'daki sorun bildirimine ekle.
    echo.
    pause
    exit /b 1
)
echo Oyunu baslat; Turkce metinler aktif olacak.
echo.
pause
exit /b 0

:cancel
echo.
echo Kurulum iptal edildi.
pause
exit /b 0

REM ----- Yardimci: oyun klasorune yazma izni var mi? -----
:check_write
set "WT=!GAME_DIR!\Content0\pc2tr_yazma_testi.tmp"
((echo test)>"!WT!") >nul 2>&1
if not exist "!WT!" exit /b 1
del /f /q "!WT!" >nul 2>&1
exit /b 0

REM ----- Yazma izni yoksa yonetici olarak yeniden baslat -----
:need_admin
echo.
echo UYARI: Oyun klasorune yazma izni yok.
echo Oyun "Program Files" gibi korumali bir klasorde kurulu olabilir.
if /i "%~1"=="/yonetici" (
    echo.
    echo Yonetici izniyle de yazilamadi. Oyunun ve Epic/Steam'in kapali
    echo oldugundan emin olup tekrar dene.
    echo.
    pause
    exit /b 1
)
echo.
echo Islem yonetici izniyle yeni bir pencerede yeniden baslatilacak.
echo Acilan Windows izin penceresinde "Evet"e tikla.
echo.
pause
>"%PC2TR_PATHFILE%" echo !GAME_DIR!
powershell -NoProfile -ExecutionPolicy Bypass -Command "try { Start-Process -FilePath $env:PC2TR_SELF -ArgumentList '/yonetici' -Verb RunAs -ErrorAction Stop } catch { exit 1 }"
if errorlevel 1 (
    del /f /q "%PC2TR_PATHFILE%" >nul 2>&1
    echo.
    echo Yonetici izni verilmedi. Dosyaya sag tiklayip
    echo "Yonetici olarak calistir" secenegiyle tekrar dene.
    echo.
    pause
    exit /b 1
)
echo Islem yeni pencerede devam ediyor. Bu pencere kapanacak.
timeout /t 3 >nul
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
