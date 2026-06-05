@echo off
echo ========================================
echo   Installing project dependencies...
echo ========================================

pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

if %errorlevel% neq 0 (
    echo [WARN] Aliyun mirror failed. Trying Tsinghua mirror...
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn
)

if %errorlevel% neq 0 (
    echo [ERROR] Installation failed. Check your network or try a different mirror.
    pause
    exit /b 1
)

echo.
echo Initializing database...
python ./init.py initdb
python ./manage.py makemigrations
python ./manage.py migrate --fake-initial
python ./init.py initsql
python ./manage.py shell -c "from django.contrib.auth.models import User;User.objects.filter(username='abo').exists() or User.objects.create_superuser('abo','abo@example.com', 'abo')"

echo.
echo ========================================
echo   Installation complete!
echo   Run: python manage.py runserver 0.0.0.0:8000
echo ========================================
pause
