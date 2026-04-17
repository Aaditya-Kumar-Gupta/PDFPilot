Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$fileOp = [Windows.Storage.StorageFile]::GetFileFromPathAsync('C:\Users\adity\pdf-tool\runtime_tests\sample1.png')
$method = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetGenericArguments().Count -eq 1 } | Select-Object -First 1
$task = $method.MakeGenericMethod([Windows.Storage.StorageFile]).Invoke($null, @($fileOp))
$task.Wait(-1) | Out-Null
$file = $task.Result
$op = $file.OpenAsync([Windows.Storage.FileAccessMode]::Read)
Write-Output ('TYPE=' + $op.GetType().FullName)
$op.GetType().GetInterfaces() | ForEach-Object { $_.FullName }
