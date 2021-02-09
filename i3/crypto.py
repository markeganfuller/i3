"""
i3pystatus Crypto Prices.

Displays crypto spot prices.
"""
import datetime

import i3pystatus
import requests


class Crypto(i3pystatus.IntervalModule):
    """Crypto Price."""

    # pylint: disable=too-few-public-methods

    currency = "GBP"
    currency_symbol = "£"
    crypto = "BTC"
    color_up = "#00F000"
    color = "#FFFFFF"
    color_down = "#F00000"
    interval = 120
    settings = (
        ("currency", "Currency to display values in"),
        ("currency_symbol", "Symbol of Currency to display values in"),
        ("crypto", "Crypto currency to check"),
        ("color_up", "Color when Prices are rising"),
        ("color", "Color when Prices are stable"),
        ("color_down", "Color when Prices are falling")
    )

    last_value = None
    yesterdays_value = None
    yesterday_last_checked_date = None

    def get_price(self, date=''):
        """Get Price of crypto."""
        if date:
            date = f"?date={date}"

        resp = requests.get(
            f"https://api.coinbase.com/v2/prices/{self.crypto}-{self.currency}/spot{date}"
        )

        return float(resp.json()["data"]["amount"])

    def update_yesterdays_value(self):
        """Update yesterdays value (used for rising / falling)."""
        yesterday = (datetime.datetime.now() - datetime.timedelta(1))
        yesterday = yesterday.date()
        if self.yesterday_last_checked_date != yesterday:
            self.yesterday_last_checked_date = yesterday
            self.yesterdays_value = self.get_price(date=yesterday.isoformat())

    def run(self):
        """Run."""
        response = {"full_text": "", "name": f"crypto_{self.crypto}"}

        current = self.get_price()
        self.update_yesterdays_value()

        if current > self.yesterdays_value:
            response["color"] = self.color_up
        elif current < self.yesterdays_value:
            response["color"] = self.color_down
        else:
            response["color"] = self.color

        response["full_text"] \
            = f"{self.currency_symbol}{current:.2f} {self.crypto}"

        # pylint: disable=attribute-defined-outside-init
        self.output = response
        self.last_value = current
