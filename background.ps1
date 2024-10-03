# Define the URL of the image
$imageUrl = "https://en.wikipedia.org/wiki/WannaCry_ransomware_attack#/media/File:Wana_Decrypt0r_screenshot.png"

# Define the local path where the image will be saved
$imagePath = "$env:USERPROFILE\Downloads\background.jpg"

# Download the image
Invoke-WebRequest -Uri $imageUrl -OutFile $imagePath

# Define the registry key for desktop background settings
$regKey = "HKCU:\Control Panel\Desktop"

# Update the registry to set the new wallpaper
Set-ItemProperty -Path $regKey -Name Wallpaper -Value $imagePath

# Refresh the desktop to apply the new wallpaper
RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters
