Start-Process powershell.exe -NoNewWindow -ArgumentList "python calculator_server.py"
Start-Sleep -Seconds 1

Start-Process powershell.exe -NoNewWindow -ArgumentList "python calculator_spooler.py"
Start-Sleep -Seconds 1

Start-Process powershell.exe -NoNewWindow -ArgumentList "python calculator_client.py"
Start-Sleep -Seconds 1

Start-Process powershell.exe -NoNewWindow -ArgumentList "python calculator_A.py"
Start-Sleep -Seconds 1

Start-Process powershell.exe -NoNewWindow -ArgumentList "python calculator_B.py"
Start-Sleep -Seconds 1

Start-Process powershell.exe -NoNewWindow -ArgumentList "python calculator_logger.py"
