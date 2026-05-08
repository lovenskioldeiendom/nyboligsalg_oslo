"""
Konfigurasjon for nybolig-monitor Oslo.

Oslo er én kommune i én fylkesgruppe — Finn-locationkoden begynner med 0.20061
"""

MUNICIPALITIES = [
    {"name": "Oslo", "finn_location": "0.20061"},
]

PROJECT_AD_TYPE = "project"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

DELAY_BETWEEN_REQUESTS_S = 4
REQUEST_TIMEOUT_S = 25
