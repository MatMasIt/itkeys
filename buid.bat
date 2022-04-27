pushd %~dp0
pyinstaller main.py --icon="logo.ico" --onefile --add-data="logo.jpg;." --add-data="logo.ico;." --add-data="nircmd.exe;." --noconsole --clean --key tce9rur8932rmc2