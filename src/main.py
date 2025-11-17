from dns_lookup import resolve_domain
from port_scanner import scan_port
from system_info import get_system_info


print("=== NetDiag: Network Diagnostic Toolkit ===")


# 1. Ping Test
status, result = ping_host("google.com")
print("\n[Ping Test] google.com →", "Reachable" if status else "Unreachable")
print(result)


# 2. DNS Lookup
status, result = resolve_domain("google.com")
print("\n[DNS Lookup] google.com →", result)


# 3. Port Scan
port_status = scan_port("google.com", 80)
print(f"\n[Port Scan] Port 80 on google.com → {'Open' if port_status else 'Closed'}")


# 4. System Info
info = get_system_info()
print("\n[System Info]")
for k, v in info.items():
print(f"{k}: {v}")
