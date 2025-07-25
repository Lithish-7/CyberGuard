def generate_iptables_rules(allowed_ports, blocked_ips):
    rules = []
    rules.append("# Allow loopback")
    rules.append("iptables -A INPUT -i lo -j ACCEPT")
    rules.append("# Allow established connections")
    rules.append("iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT")

    for port in allowed_ports:
        port = port.strip()
        if port.isdigit():
            rules.append(f"iptables -A INPUT -p tcp --dport {port} -j ACCEPT")

    for ip in blocked_ips:
        ip = ip.strip()
        if ip:
            rules.append(f"iptables -A INPUT -s {ip} -j DROP")

    rules.append("# Drop all other inbound traffic")
    rules.append("iptables -A INPUT -j DROP")

    return "\n".join(rules)
