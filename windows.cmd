echo ����host�ļ�
ftp -s:"windows.txt"
echo �������
@echo off
mode con lines=30 cols=60
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
:main
cls
color 2f


if exist "%SystemRoot%\System32\choice.exe" goto Win7Choice


echo.
goto host DNS
cls
echo ����������������ѡ��
ping 127.0.1 -n "2">nul
goto main

:Win7Choice
goto host DNS
cls
goto main

:host DNS
cls
color 2f
copy /y "hosts" "%SystemRoot%\System32\drivers\etc\hosts"
ipconfig /flushdns

del /F /S hosts

echo.-----------------------------------------------------------
echo.
echo ��ϲ�������Ǳ���hosts��ˢ�±���DNS��������ɹ�!
echo.
echo ����ȥ��Google��Twitter��Facebook��Gmail���ȸ�ѧ���ɣ�
echo.
echo.�ȸ���Щ��վ�ǵ�ʹ��https���м��ܷ��ʣ�
echo.
echo.����https://www.google.com
echo.
echo.���ߣ�https://www.google.com/ncr
echo.      https://www.google.com.hk/ncr
echo.
goto end

:CL
cls
color 2f
@echo 127.0.0.1 localhost > %SystemRoot%\System32\drivers\etc\hosts
echo ��ϲ����hosts�ָ���ʼ�ɹ�!
echo.
goto end

:end
echo �밴������˳���
@Pause>nul