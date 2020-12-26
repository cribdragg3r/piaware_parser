import requests
import json
import configparser


def _get_api_key() -> str:
    config = configparser.ConfigParser()
    config.read("enrichment_api.conf")
    return config.get("adsbexchange", "key")


def get_aircraft_by_icao(icao: str) -> dict:
    uri = f"https://adsbexchange-com1.p.rapidapi.com/icao/{icao.upper()}/"
    headers = {
    'x-rapidapi-key': _get_api_key(),
    'x-rapidapi-host': "adsbexchange-com1.p.rapidapi.com"
    }
    r = requests.get(uri, headers=headers)
    aircraft_data = r.json()
    return aircraft_data


def get_aircraft_by_registration(reg: str) -> dict:
    uri = f"https://adsbexchange-com1.p.rapidapi.com/registration/{reg.upper()}/"
    headers = {
    'x-rapidapi-key': _get_api_key(),
    'x-rapidapi-host': "adsbexchange-com1.p.rapidapi.com"
    }
    r = requests.get(uri, headers=headers)
    aircraft_data = r.json()
    return aircraft_data
