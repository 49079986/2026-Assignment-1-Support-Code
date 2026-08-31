@echo off
setlocal

cd /d "%~dp0"

echo Running COMP3702 A1 tests L1-L4...
echo.

echo ===== L1 UCS =====
python tester.py ucs testcases/L1.txt
echo.

echo ===== L1 A* =====
python tester.py a_star testcases/L1.txt
echo.

echo ===== L2 UCS =====
python tester.py ucs testcases/L2.txt
echo.

echo ===== L2 A* =====
python tester.py a_star testcases/L2.txt
echo.

echo ===== L3 UCS =====
python tester.py ucs testcases/L3.txt
echo.

echo ===== L3 A* =====
python tester.py a_star testcases/L3.txt
echo.

echo ===== L4 UCS =====
python tester.py ucs testcases/L4.txt
echo.

echo ===== L4 A* =====
python tester.py a_star testcases/L4.txt
echo.

echo Done.
pause
