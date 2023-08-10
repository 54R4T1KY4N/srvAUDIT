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
    logging.info("Starting security audit for Linux server.")

    security_checks = [
        ("System Information", "uname -a"),
        ("Network Configuration", "ifconfig -a"),
        ("User Accounts", "cat /etc/passwd"),
        ("Group Memberships", "cat /etc/group"),
        ("Home Directory Permissions", "ls -ld /home/*"),
        ("SSH Configuration", "cat /etc/ssh/sshd_config"),
        ("Filesystem Mounts", "mount"),
        ("Kernel Modules", "lsmod"),
        ("Running Processes", "ps aux"),
        ("Listening Ports (netstat)", "netstat -tuln"),
        ("Listening Ports (ss)", "ss -tuln"),
        ("Firewall Rules (iptables)", "iptables -L"),
        ("Firewall Rules (nftables)", "nft list ruleset"),
        ("SELinux Status", "sestatus"),
        ("AppArmor Status", "apparmor_status"),
        ("Sudo Configuration", "sudo -l"),
        ("Cron Jobs", "crontab -l"),
        ("Uptime", "uptime"),
        ("Last Logged-in Users", "last"),
        ("Disk Usage", "df -h"),
        ("Top Memory-Consuming Processes", "ps aux --sort=-%mem | head"),
        ("Top CPU-Consuming Processes", "ps aux --sort=-%cpu | head"),
        ("List of Installed Packages (rpm)", "rpm -qa"),
        ("List of Installed Packages (deb)", "dpkg --list"),
        ("System Logs (journalctl)", "journalctl -n 50"),
        ("Network Routes", "ip route"),
        ("SSH Key Files", "ls -l /home/*/.ssh"),
        ("Failed Login Attempts", "grep 'Failed password' /var/log/auth.log"),
        ("Root Privileged Commands (sudo history)", "sudo cat /root/.bash_history"),
        ("Listening Network Services (netstat)", "netstat -tuln"),
        ("Opened Files (lsof)", "lsof"),
        ("System Users (getent)", "getent passwd"),
        ("System Startup Services (systemd)", "systemctl list-units --type=service --all"),
        ("System Startup Services (chkconfig)", "chkconfig --list"),
        ("DNS Configuration", "cat /etc/resolv.conf"),
        ("System File Changes (rpm)", "rpm -Va"),
        ("System File Changes (debsums)", "debsums -c"),
        ("System Environment Variables", "env"),
        ("IPTables Configuration", "iptables-save"),
        ("Users with Shell Access", "cat /etc/passwd | grep -E '/bin/bash|/bin/sh'"),
        ("SUID and SGID Files", "find / -type f \( -perm -4000 -o -perm -2000 \) -exec ls -ld {} \\;"),
        ("Executable Files in User Directories", "find /home -type f -executable -ls"),
        ("World-Writable Files", "find / -xdev -type f -perm -0002"),
        ("Sudoers Configuration", "cat /etc/sudoers"),
        ("Network Configuration (ifcfg)", "find /etc/sysconfig/network-scripts -type f -name 'ifcfg-*' -exec cat {} \\;"),
        ("Cron Jobs (systemd timers)", "systemctl list-timers"),
        ("Installed Web Server Software", "apache2ctl -V 2>/dev/null | grep 'Server version' || nginx -v 2>&1"),
        ("Running Docker Containers", "docker ps -a"),
        ("Mounted Filesystems", "mount | grep -v 'tmpfs'"),
        ("System File Permissions (important directories)", "find /etc /usr /bin /sbin /lib -type d -exec ls -ld {} \\;"),
        ("SSH Key Permissions", "find /home -type f -name 'id_*' -exec ls -l {} \\;"),
        ("NTP Configuration", "cat /etc/ntp.conf"),
        ("Listening SSH Sessions", "netstat -tnpa | grep 'ESTABLISHED.*sshd'"),
        ("IPv6 Configuration", "cat /proc/sys/net/ipv6/conf/all/disable_ipv6"),
        ("System Banner", "cat /etc/issue.net"),
    ]

    report = "Security Audit Report for Linux server\n\n"

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
