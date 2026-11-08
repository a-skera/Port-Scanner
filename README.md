# Python TCP Port Scanner

A lightweight TCP port scanner built with Python.
It identifies open TCP ports, attempts to identify
their associated services, and measures connection time.

## Features

- TCP port scanning
- Customizable port ranges
- Service identification
- Connection timeout
- Scan duration measurement
- Open port summary

## Requirements

- Python 3.8+
- No external dependencies

## Usage

```bash
python scanner.py 127.0.0.1
python scanner.py 127.0.0.1 -p 1-1000
```

## Disclaimer

This tool is intended for educational purposes
and authorized security testing only.

Always obtain permission before scanning
systems you do not own.
