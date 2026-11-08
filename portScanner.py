
import socket
import argparse
import time
from datetime import datetime


def scan_port(target, port, timeout=0.5):
    """Check whether a TCP port is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    start_time = time.perf_counter()

    try:
        result = sock.connect_ex((target, port))
        elapsed = (time.perf_counter() - start_time) * 1000

        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown"

            print(f"[OPEN]   Port {port:<5} | {service:<15} | {elapsed:.2f} ms")
            return True

    except socket.error as error:
        print(f"[ERROR]  Port {port}: {error}")

    finally:
        sock.close()

    return False


def main():
    parser = argparse.ArgumentParser(
        description="Simple Python TCP Port Scanner"
    )

    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument(
        "-p", "--ports",
        default="1-1024",
        help="Port range (example: 1-1000)"
    )

    args = parser.parse_args()

    try:
        target = socket.gethostbyname(args.target)
        start_port, end_port = map(int, args.ports.split("-"))

        if not (1 <= start_port <= end_port <= 65535):
            raise ValueError("Invalid port range")

    except (socket.gaierror, ValueError) as error:
        print(f"[ERROR] {error}")
        return

    print("=" * 55)
    print("          PYTHON TCP PORT SCANNER")
    print("=" * 55)
    print(f"Target: {target}")
    print(f"Time:   {datetime.now()}")
    print(f"Ports:  {start_port}-{end_port}")
    print("-" * 55)

    scan_start = time.perf_counter()
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            open_ports.append(port)

    duration = time.perf_counter() - scan_start

    print("-" * 55)
    print(f"Scan completed in {duration:.2f} seconds")
    print(f"Open ports found: {len(open_ports)}")
    print(f"Open ports: {open_ports}")
    print("=" * 55)


if __name__ == "__main__":
    main()
