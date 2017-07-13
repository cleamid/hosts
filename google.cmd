echo 下载处理脚本
ftp -s:"google.txt"
echo 下载完毕
call windows.cmd

del /F /S windows.cmd windows.txt

@ pause > nul