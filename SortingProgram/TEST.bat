@echo off
title TEST
set DESC=False
py Main.py %DESC%
fc /C Sorted.txt Expected.txt
set DESC=True
py Main.py %DESC%
fc /C SortedR.txt ExpectedR.txt
pause