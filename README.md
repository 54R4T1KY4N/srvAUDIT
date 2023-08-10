                                     ______   __    __  _______   ______  ________ 
                                    /      \ /  |  /  |/       \ /      |/        |
      _______   ______   __     __ /$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$/ $$$$$$$$/ 
     /       | /      \ /  \   /  |$$ |__$$ |$$ |  $$ |$$ |  $$ |  $$ |     $$ |   
    /$$$$$$$/ /$$$$$$  |$$  \ /$$/ $$    $$ |$$ |  $$ |$$ |  $$ |  $$ |     $$ |   
    $$      \ $$ |  $$/  $$  /$$/  $$$$$$$$ |$$ |  $$ |$$ |  $$ |  $$ |     $$ |   
     $$$$$$  |$$ |        $$ $$/   $$ |  $$ |$$ \__$$ |$$ |__$$ | _$$ |_    $$ |   
    /     $$/ $$ |         $$$/    $$ |  $$ |$$    $$/ $$    $$/ / $$   |   $$ |   
    $$$$$$$/  $$/           $/     $$/   $$/  $$$$$$/  $$$$$$$/  $$$$$$/    $$/    
                                                                               
                                                                                                                                                              
# srvAUDIT
This repository contains two Python scripts designed to perform fast and comprehensive security audits on Linux and Windows servers. The scripts systematically execute a series of commands to gather essential system information, identify potential vulnerabilities, and generate detailed audit reports.

*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

    Below are descriptions for each script, along with the required software dependencies for running them:
*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
    1. Linux Server Security Audit Script

The Linux server security audit script performs a thorough examination of various aspects of a Linux server's configuration, helping identify security vulnerabilities and ensuring a robust server setup. This script requires the following software dependencies on the Linux system:

Python 3
The datetime module (usually included in Python standard library)
The subprocess module (usually included in Python standard library)
The os module (usually included in Python standard library)
The logging module (usually included in Python standard library)

    Usage:

Clone this repository and navigate to the directory containing the script: srvAUDIT_linux.py
Ensure Python 3 is installed on your Linux server.
Run the script using Python 3:

    python3 srvAUDIT_linux.py

    Note: This script should be used responsibly and with proper authorization. Review the generated report and take necessary actions to address any identified security concerns.
*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
    2. Windows Server Security Audit Script

The Windows server security audit script performs a comprehensive audit of a Windows server's configuration, examining various critical aspects of the system to ensure its security. This script requires the following software dependencies on the Windows system:

Python 3
The datetime module (usually included in Python standard library)
The subprocess module (usually included in Python standard library)
The os module (usually included in Python standard library)
The logging module (usually included in Python standard library)

    Usage:

Clone this repository and navigate to the directory containing the script: srvAUDIT_windows.py.
Ensure Python 3 is installed on your Windows server.
Run the script using Python 3:

    python3 srvAUDIT_windows.py

*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

    Installer

So if you want, you can use these scripts "srvAUDIT_ins.sh and srvAUDIT_ins.bat" to have them install all required dependencies on your host, or you can install them manually.

    Note: This script should be used responsibly and with proper authorization. Review the generated report and take necessary actions to address any identified security concerns.

These scripts provide valuable tools for conducting security audits on both Linux and Windows servers, systematically examining key aspects of the system's configuration to enhance overall security. It's essential to ensure responsible usage, obtain proper authorization, and align the scripts with the intended use case.
