@REM Create Schedule Task windowns
SCHTASKS /CREATE /SC MINUTE /MO 10 /TN "MyTasks\Notepad task" /TR "C:\Windows\System32\notepad.exe"
@REM install psycopg2
pip install psycopg2-binary