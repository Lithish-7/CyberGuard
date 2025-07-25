import sys
from modules import url_scanner, log_analyzer, firewall_generator, threat_checker, file_hash_checker

def main():
    while True:
        print("\n=== CYBERGUARD - Security Automation Toolkit ===")
        print("1. Suspicious URL Scanner")
        print("2. Log File Analyzer")
        print("3. Firewall Rule Generator")
        print("4. Threat Intelligence Checker")
        print("5. File Integrity Checker")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            url = input("Enter URL to check: ")
            url_scanner.analyze_url(url)
        elif choice == '2':
            file_path = input("Enter log file path: ")
            log_analyzer.analyze_log(file_path)
        elif choice == '3':
            allowed_ports = input("Enter allowed ports (comma-separated): ").split(",")
            blocked_ips = input("Enter IPs to block (comma-separated): ").split(",")
            print(firewall_generator.generate_iptables_rules(allowed_ports, blocked_ips))
        elif choice == '4':
            ip = input("Enter IP or domain: ")
            threat_checker.check_ip(ip)
        elif choice == '5':
            file_path = input("Enter file path: ")
            file_hash_checker.check_file_integrity(file_path)
        elif choice == '6':
            print("Exiting CyberGuard. Stay Safe!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
