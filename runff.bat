@ECHO OFF

REM
REM @(!--#) @(#) runff.bat, version 001, 25-august-2018
REM
REM create a listing.txt file and then run the
REM bulitin Python HTTP server with CGI support
REM

mkdir cgi-bin > NUL

copy findfile.py cgi-bin\findfile.py

ECHO.
ECHO Open a browser and enter this URL:
ECHO.
ECHO     http://127.0.0.1:8000/cgi-bin/findfile.py
ECHO.
ECHO. ######
ECHO. #     #  ######    ##    #####    #   #
ECHO. #     #  #        #  #   #    #    # #
ECHO. ######   #####   #    #  #    #     #
ECHO. #   #    #       ######  #    #     #
ECHO. #    #   #       #    #  #    #     #
ECHO. #     #  ######  #    #  #####      #
ECHO.

python -m http.server --cgi
