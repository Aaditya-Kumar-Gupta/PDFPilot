param([string]$ImagePath)
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics, ContentType=WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime]

function Await($Operation) {
    $iface = $Operation.GetType().GetInterfaces() | Where-Object {
        $_.IsGenericType -and (
            $_.GetGenericTypeDefinition().FullName -eq 'Windows.Foundation.IAsyncOperation`1' -or
            $_.GetGenericTypeDefinition().FullName -eq 'Windows.Foundation.IAsyncOperationWithProgress`2'
        )
    } | Select-Object -First 1
    if ($null -eq $iface) {
        $task = [System.WindowsRuntimeSystemExtensions]::AsTask([Windows.Foundation.IAsyncAction]$Operation)
        $task.Wait(-1) | Out-Null
        return $null
    }
    $args = $iface.GetGenericArguments()
    $methods = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod }
    if ($args.Count -eq 1) {
        $method = $methods | Where-Object { $_.GetGenericArguments().Count -eq 1 -and $_.GetParameters().Count -eq 1 } | Select-Object -First 1
        $task = $method.MakeGenericMethod($args).Invoke($null, @($Operation))
    } else {
        $method = $methods | Where-Object { $_.GetGenericArguments().Count -eq 2 -and $_.GetParameters().Count -eq 1 } | Select-Object -First 1
        $task = $method.MakeGenericMethod($args).Invoke($null, @($Operation))
    }
    $task.Wait(-1) | Out-Null
    return $task.Result
}

$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($ImagePath))
$stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read))
$decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream))
$bitmap = Await ($decoder.GetSoftwareBitmapAsync())
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
$result = Await ($engine.RecognizeAsync($bitmap))
Write-Output $result.Text
