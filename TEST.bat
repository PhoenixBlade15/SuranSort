@echo off
title TEST
START Main.py
fc /C Sorted.txt Expected.txt
pause