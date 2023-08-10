import subprocess
import os
import datetime
import logging

def setup_logging(log_dir):
    log_file = os.path.join(log_dir, "audit_log.txt")
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"Error running command: {command}\nError: {e}"

def security_audit():
    audit_dir = f"audit_results_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    os.makedirs(audit_dir, exist_ok=True)
    
    setup_logging(audit_dir)
    logging.info("Starting security audit for Windows server.")

    security_checks = [
        ("System Information", "systeminfo"),
        ("Scheduled Tasks", "schtasks /query /fo LIST"),
        ("Network Connections", "netstat -ano"),
        ("User Accounts", "wmic useraccount"),
        ("Installed Software", "wmic product get name,version"),
        ("Running Processes", "tasklist"),
        ("Firewall Rules", "netsh advfirewall firewall show rule name=all"),
        ("Open Ports", "netstat -an"),
        ("Windows Updates", "wmic qfe list"),
        ("Listening Services", "netstat -anb"),
        ("Startup Programs", "wmic startup get caption,command"),
        ("Active Directory Configuration", "dcdiag"),
        ("File Permissions (C:)", "icacls C:\\ /T /C"),
        ("Disk Usage", "wmic logicaldisk get caption,description,freespace,size"),
        ("Installed Hotfixes", "wmic qfe"),
        ("Network Shares", "net share"),
        ("Group Memberships", "whoami /groups"),
        ("Local Administrators", "net localgroup administrators"),
        ("USB Devices History", "wmic diskdrive get caption,mediatype,PNPDeviceID"),
        ("Windows Event Logs", "wevtutil el"),
        ("Windows Services", "wmic service list brief"),
        ("Windows Firewall Status", "netsh advfirewall show currentprofile"),
        ("Scheduled Jobs (Task Scheduler)", "schtasks /query /fo LIST"),
        ("Installed Antivirus Software", "wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get displayName,productState"),
        ("System Startup Programs (Registry)", "reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"),
        ("System Environment Variables", "set"),
        ("Windows Registry (Software Hive)", "reg query HKEY_LOCAL_MACHINE\\Software"),
        ("Windows Registry (System Hive)", "reg query HKEY_LOCAL_MACHINE\\System"),
        ("Local Group Policies", "gpresult /Scope Computer /v"),
        ("User Group Policies", "gpresult /Scope User /v"),
        ("Logged-in Users", "query user"),
        ("Printers", "wmic printer list brief"),
        ("System Drivers", "driverquery"),
        ("Windows Firewall Rules (Advanced Security)", "netsh advfirewall firewall show rule name=all"),
        ("Network Configuration", "ipconfig /all"),
        ("Network Interfaces", "wmic nic get NetConnectionID,Speed"),
        ("Network Routing Table", "route print"),
        ("Network DNS Configuration", "ipconfig /all | findstr /i 'dns'"),
        ("Windows Event Logs (System)", "wevtutil qe System /c:20 /rd:true"),
        ("Windows Event Logs (Security)", "wevtutil qe Security /c:20 /rd:true"),
        ("Local Users and Groups (net localgroup)", "net localgroup"),
        ("Windows Firewall Rules (netsh advfirewall)", "netsh advfirewall firewall show rule name=all"),
        ("List of Scheduled Tasks (schtasks)", "schtasks /query /fo LIST /v"),
        ("Network Shares Information (net share)", "net share"),
        ("Local Security Policies (secpol.msc)", "secpol.msc"),
        ("Installed Drivers (driverquery)", "driverquery"),
        ("Local Users and Groups (lusrmgr.msc)", "lusrmgr.msc"),
        ("Windows Defender Status (mpcmdrun)", "mpcmdrun -getfilesignatures"),
        ("Windows Update Status (wuauclt)", "wuauclt /showwindowsupdate"),
        ("Logged-on Users (query user)", "query user"),
        ("Active Network Connections (netstat)", "netstat -ano"),
        ("Windows Modules (wmic qfe list)", "wmic qfe list"),
        ("Windows Firewall Status (netsh advfirewall)", "netsh advfirewall show allprofiles"),
        ("System Drivers (driverquery)", "driverquery"),
        ("System Environment Variables (set)", "set"),
        ("Software Installed (wmic product get)", "wmic product get name,version"),
        ("Task Scheduler Jobs (schtasks)", "schtasks /query /fo LIST /v"),
        ("Windows Services (wmic service list)", "wmic service list brief"),
        ("System Startup Programs (wmic startup)", "wmic startup get caption,command"),
        ("PowerShell Execution Policy", "Get-ExecutionPolicy"),
        ("Windows Defender Exclusions (mpcmdrun)", "mpcmdrun -getexclusion"),
        ("Windows Installer (wmic product)", "wmic product list"),
        ("Windows Registry (user hives)", "reg query HKU"),
        ("Windows Scheduled Tasks (AT command)", "at"),
        ("Windows Backup Configuration", "wbadmin get items"),
        ("Windows Firewall Rules (Group Policy)", "gpresult /R /SCOPE COMPUTER /Z"),
        ("Windows Group Policies (rsop.msc)", "rsop.msc"),
        ("Windows Audit Policies (auditpol)", "auditpol /get /category:*"),
        ("Windows Remote Desktop (RDP) Settings", "reg query \"HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\" /v fDenyTSConnections"),
        ("Windows Remote Desktop Users", "net localgroup \"Remote Desktop Users\""),
        ("Windows Remote Desktop Licensing (RDS)", "reg query \"HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\RCM\GracePeriod\""),
        ("Windows Active Directory Sites", "nltest /dsgetsite"),
    ]

    report = "Security Audit Report for Windows server\n\n"

    for check_name, check_command in security_checks:
        logging.info(f"Running {check_name} audit...")
        result = run_command(check_command)
        report += f"--- {check_name} ---\n{result}\n\n"
        logging.info(f"{check_name} audit completed.")

    report_path = os.path.join(audit_dir, "security_audit_report.txt")
    with open(report_path, "w") as report_file:
        report_file.write(report)

    logging.info("Security audit completed.")
    print(f"Security audit completed. Report saved in {report_path}")

if __name__ == "__main__":
    security_audit()
