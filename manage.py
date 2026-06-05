#!/usr/bin/env python
import os
import sys
import threading
import webbrowser

# Python 3.10+ compatibility shims for Django 2.0
import util.compat

def open_browser():
    # 等待一段时间，确保服务器启动
    threading.Timer(1, webbrowser.open, args=['http://localhost:8080/front/dist/index.html']).start()
    threading.Timer(1, webbrowser.open, args=['http://localhost:8080/admin/dist/index.html#login']).start()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj2.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 启动浏览器
    open_browser()
    execute_from_command_line(sys.argv)
