# NetScan

NetScan is a small Python OSINT utility that fetches network intelligence for a target using:

- `ipinfo` for IP/domain geolocation and ASN/org metadata
- `dnspython` for DNS resolution

## Features

- Reads `IPINFO_TOKEN` from environment variables
- Queries IPInfo details for an IP address or domain
- Prints full IPInfo response data
- Attempts DNS resolution for the target and prints resolved records

## Project Structure

```text
src/NetScan/main.py      # CLI entry script
src/NetScan/NetScan.py   # Core logic (handler + target lookup)
pyproject.toml           # Project metadata and dependencies
```

## Requirements

- Python 3.10+
- An [IPInfo](https://ipinfo.io/) API token

## Installation

```bash
git clone <your-repo-url>
cd NetScan
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -U pip
pip install ipinfo python-dotenv dnspython
```

## Configuration

Create a `.env` file in the repository root:

```env
IPINFO_TOKEN=your_ipinfo_token_here
```

If `IPINFO_TOKEN` is missing, the script raises:

```text
RuntimeError: IPINFO_TOKEN not set
```

## Usage

From repository root:

```bash
python src/NetScan/main.py
```

You will be prompted:

```text
target:
```

Example inputs:

- `8.8.8.8`
- `example.com`

## Example Output (abridged)

```text
target: 8.8.8.8
{'ip': '8.8.8.8', 'city': '...', 'region': '...', 'country': '...', ...}
8.8.8.8
```

## Current Behavior Notes

- Exceptions inside data lookups are currently suppressed (`pass`), so some failures may not show explicit errors.
- The DNS query uses `dns.resolver.resolve(target)` with default record type behavior.

## License

Add a license file (for example `MIT`) if you plan to distribute this project publicly.