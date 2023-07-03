# Check if Python is already installed
$pythonInstalled = winget list --name "Python"

if ($pythonInstalled -like "*Python*") {
    Write-Output "Python is already installed."
} else {
    # Install Python using winget
    Write-Output "Installing Python..."
    winget install --name "Python"
}

# Check if pip is already installed
$pipInstalled = Get-Command pip -ErrorAction SilentlyContinue

if ($pipInstalled) {
    Write-Output "pip is already installed."
} else {
    # Install pip using the embedded Python installer
    Write-Output "Installing pip..."
    & python -m ensurepip --upgrade
}

# Verify Python and pip installation
$pythonVersion = python --version
$pipVersion = pip --version

Write-Output "Python version: $pythonVersion"
Write-Output "pip version: $pipVersion"

# Check if requirements.txt file exists in current directory
$requirementsFile = Join-Path $PSScriptRoot "requirements.txt"

if (Test-Path $requirementsFile) {
    Write-Output "Installing packages from requirements.txt..."
    & pip install -r $requirementsFile
} else {
    Write-Output "No requirements.txt file found in the current directory."
}
