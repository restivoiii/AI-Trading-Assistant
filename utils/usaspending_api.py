import requests

BASE_URL = "https://api.usaspending.gov/api/v2/agency"

def fetch_agency_overview(top_tier_code):
    """Returns agency overview information."""
    url = f"{BASE_URL}/{top_tier_code}/"
    response = requests.get(url)
    return response.json()

def fetch_agency_awards(top_tier_code):
    """Returns agency award information."""
    url = f"{BASE_URL}/{top_tier_code}/awards/"
    response = requests.get(url)
    return response.json()
