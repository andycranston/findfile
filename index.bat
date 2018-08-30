@ECHO OFF

REM
REM @(!--#) @(#) index.bat, version 001, 30-august-2018
REM
REM create a listing.txt file
REM

TIME < NUL | FIND "current"

ECHO Creating index file.  This may take a few minutes - please wait

dir /o/b/s C:\ > listing.txt

ECHO.
ECHO. ######
ECHO. #     #   ####   #    #  ######
ECHO. #     #  #    #  ##   #  #
ECHO. #     #  #    #  # #  #  #####
ECHO. #     #  #    #  #  # #  #
ECHO. #     #  #    #  #   ##  #
ECHO. ######    ####   #    #  ######
ECHO.

TIME < NUL | FIND "current"
