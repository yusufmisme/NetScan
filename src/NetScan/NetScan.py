import ipinfo, os, socket
from dotenv import load_dotenv

def Handler():
    global handler
    load_dotenv()
    TOKEN = os.getenv("IPINFO_TOKEN")
    if not TOKEN:
        raise RuntimeError("IPINFO_TOKEN not set")
    handler = ipinfo.getHandler(TOKEN)

def Details(target: str):
    details = handler.getDetails(target)
    try:
        print(details.all)
    except Exception as e:
        pass
    '''
    print(f"IP Address: {details.ip}")
    print(f"City: {details.city}")
    print(f"Region: {details.region}")
    print(f"Country: {details.country_name}")
    print(f"Postal Code: {details.postal}")
    print(f"Coordinates: {details.loc}")
    print(f"Organization: {details.org}")
    print(f"Timezone: {details.timezone}")
    '''
