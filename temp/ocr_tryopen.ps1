Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$method = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetGenericArguments().Count -eq 1 } | Select-Object -First 1
$fileOp = [Windows.Storage.StorageFile]::GetFileFromPathAsync('C:\Users\adity\pdf-tool\runtime_tests\sample1.png')
$fileTask = $method.MakeGenericMethod([Windows.Storage.StorageFile]).Invoke($null, @($fileOp))
$fileTask.Wait(-1) | Out-Null
$file = $fileTask.Result
$op = [Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]]($file.OpenAsync([Windows.Storage.FileAccessMode]::Read))
$task = $method.MakeGenericMethod([Windows.Storage.Streams.IRandomAccessStream]).Invoke($null, @($op))
$task.Wait(-1) | Out-Null
Write-Output $task.Result
