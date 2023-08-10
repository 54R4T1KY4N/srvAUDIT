@echo off

REM Install Python (ensure Python installer is in the same directory as this script)
if not exist "python-installer.msi" (
    echo Python installer not found. Please place "python-installer.msi" in the same directory as this script.
    exit /b 1
)

REM Install Python (change the installer filename if needed)
msiexec /i python-installer.msi /quiet ALLUSERS=1 ADDLOCAL=ALL

REM Install required Python packages (subprocess is already part of Python standard library)
python -m pip install datetime logging

REM Run the security audit Python script
python security_audit_script.py

REM End of the script
