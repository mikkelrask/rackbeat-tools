function Show-Menu {
    Write-Host "====================="
    Write-Host "  PRODUCT MANAGEMENT"
    Write-Host "====================="
    Write-Host "Please choose an option:`n"
    Write-Host "1. Import products"
    Write-Host "2. Update products`n"
}

function Run-ImportProducts {
    Write-Host "Running import-products.py..."
    python import-products.py
}

function Run-UpdateProducts {
    Write-Host "Running update-products.py..."
    python update-products.py
}

do {
    Show-Menu
    $choice = Read-Host "Enter your choice (1 or 2), or 'q' to quit"

    switch ($choice) {
        '1' {
            Run-ImportProducts
            break
        }
        '2' {
            Run-UpdateProducts
            break
        }
        'q' {
            break
        }
        default {
            Write-Host "Invalid choice. Please select a valid option.`n" -ForegroundColor Red
            Start-Sleep -Milliseconds 750
        }
    }
} while ($choice -ne 'q')
