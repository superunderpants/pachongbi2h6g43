@echo off
echo ========================================
echo   Installing spider dependencies...
echo ========================================

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] pip install failed. Try running manually:
    echo   pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
    echo.
)

pause
