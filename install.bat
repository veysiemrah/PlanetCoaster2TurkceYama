@echo off
setlocal enabledelayedexpansion

echo ============================================
echo  Planet Coaster 2 Turkce Yama Kurulum
echo ============================================
echo.

set "GAME_DIR="

if exist "C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata" (
    set "GAME_DIR=C:\XboxGames\Planet Coaster 2\Content\Win64\ovldata"
    echo Xbox Game Pass kurulumu bulundu.
    goto :install
)

if exist "C:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata" (
    set "GAME_DIR=C:\Program Files (x86)\Steam\steamapps\common\Planet Coaster 2\Win64\ovldata"
    echo Steam kurulumu bulundu.
    goto :install
)

echo Oyun kurulumu otomatik bulunamadi.
echo.
set /p "GAME_DIR=Lutfen ovldata dizini yolunu gir: "

if not exist "%GAME_DIR%" (
    echo HATA: %GAME_DIR% bulunamadi.
    pause
    exit /b 1
)

:install
echo.
echo Hedef: %GAME_DIR%
echo.

if not exist "TurkceYama" (
    echo HATA: TurkceYama klasoru bu dizinde bulunamadi.
    echo Bu script TurkceYama klasoru ile ayni dizinde olmali.
    pause
    exit /b 1
)

echo Yama kopyalaniyor...
xcopy /E /I /Y "TurkceYama" "%GAME_DIR%\TurkceYama"

if errorlevel 1 (
    echo HATA: Kopyalama basarisiz.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  Kurulum tamamlandi!
echo ============================================
echo.
echo Simdi oyunu acip Ayarlar ^> Dil menusunden
echo "Cestina" secmelisin. Yama aktif olacak.
echo.
pause
