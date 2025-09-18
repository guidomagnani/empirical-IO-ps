import requests
import html
from io import StringIO
import pandas as pd

list_url = 'https://fabiosacerdote.github.io/ScrapingData/top_paid_apps_to_share.html'


def fetch_app_list(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def build_dataframe(html_content: str) -> pd.DataFrame:
    clean_html = html.unescape(html_content)
    df = pd.read_html(StringIO(clean_html))[0]
    return df


if __name__ == "__main__":
    html_content = fetch_app_list(list_url)
    app_df = build_dataframe(html_content)
    print(app_df.head())
