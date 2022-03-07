import re
import pytz
import requests
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from podgen import Podcast, Episode, Media


# Fetch and parse episode metadata
wikipedia_url = "https://en.wikipedia.org/wiki/The_Unbelievable_Truth_(radio_show)"
wikipedia_html = requests.get(wikipedia_url).text
wikipedia_soup = BeautifulSoup(wikipedia_html, 'html.parser')
raw_series_metadata = wikipedia_soup.find_all("table", class_="wikitable")

metadata = dict()
for raw_table in raw_series_metadata:
    for raw_row in raw_table.find_all("tr"):
        if raw_row.find_all('th'):
            # table header row, skip
            continue

        try:
            cells = raw_row.find_all("td")
            identifier = cells[0].text.replace('\n', '')
            metadata[identifier] = {
                'series': identifier[:2],
                'episode': identifier[3:],
                'guests': cells[2].text.replace('\n', ''),
                'topics': cells[3].text.replace('\n', ''),
                'first_broadcast': cells[1].text.replace('\n', ''),
            }
        except IndexError:
            pass


# Fetch and parse episode audio
archive_urls = [
    "https://archive.org/details/theunbelievabletruth1-5",
    "https://archive.org/details/theunbelievabletruth6-10",
    "https://archive.org/details/theunbelievabletruth11-15",
    "https://archive.org/details/theunbelievabletruth16-20",
    "https://archive.org/details/theunbelievabletruth21-23",  # 21-25
    "https://archive.org/details/the-unbelievable-truth-s-26"
]

raw_episodes = list()
for url in archive_urls:
    archive_html = requests.get(url).text
    archive_soup = BeautifulSoup(archive_html, 'html.parser')
    raw_episodes += archive_soup.find_all("a", class_="download-pill")

    # Process
    episodes = list()
    for raw_ep in raw_episodes:
        if raw_ep['href'][-4:] != '.mp3':
            # file does not end in mp3, so skip
            continue

        title = raw_ep.text
        title = title.replace('download', '')
        title = title.replace('.mp3', '').strip()
        regex = re.compile(r's(\d+) e(\d+)').search(title)
        identifier = f"{regex.group(1)}x{regex.group(2)}"  # e.g. 08x03

        # Handle edge case episodes
        edge_cases = {
            # File title: Custom metadata
            "The Unbelievable Truth (s00 e00) 'Pilot'": {
                "wikipedia_identifier": "Pilot",
                "series": "00",
                "episode": "00 - Pilot"
            },
            "The Unbelievable Truth (s02 e07) 'Christmas Special'": {
                "wikipedia_identifier": "Special",
                "series": "02",
                "episode": "07 - Christmas Special"
            },
            "The Unbelievable Truth (s04 e07) 'New Year's Special'": {
                "wikipedia_identifier": "Sp.",
                "series": "04",
                "episode": "07 - New Year's Special"
            }
        }
        if title in edge_cases.keys():
            identifier = edge_cases[title]["wikipedia_identifier"]
            metadata[identifier]["series"] = edge_cases[title]["series"]
            metadata[identifier]["episode"] = edge_cases[title]["episode"]

        try:
            ep_metadata = metadata[identifier]
            output_title = f"S{ep_metadata['series']} E{ep_metadata['episode']}: {ep_metadata['topics']}"
            first_broadcast_no_brackets = re.sub("[\(\[].*?[\)\]]", "", ep_metadata['first_broadcast'])
            first_broadcast_datetime = datetime.strptime(first_broadcast_no_brackets, "%d %B %Y").replace(tzinfo=pytz.UTC)
            description = f"Guests: {ep_metadata['guests']}.<br/><br/>" + \
            f"First broadcast: {first_broadcast_no_brackets}"
        except KeyError:
            output_title = title
            description = ""
            first_broadcast_datetime = datetime.now().replace(tzinfo=pytz.utc)
            pass

        ep = {
            'title': output_title,
            'url': urljoin(url, raw_ep['href']),
            'description': description,
            'first_broadcast': first_broadcast_datetime,
        }

        episodes.append(ep)


# Create the Podcast
podcast = Podcast(
    name="The Unbelievable Truth",
    description="Game show in which panellists compete to see how many nuggets of truth they are able to to hide amongst their lies.",
    website="https://www.bbc.co.uk/programmes/b007mf4f",
    explicit=False,
    image="https://ichef.bbci.co.uk/images/ic/1200x675/p09q7v6j.jpg"
)

podcast.episodes += [
    Episode(
        title=ep['title'],
        media=Media(ep['url']),
        publication_date=ep['first_broadcast'],
        summary=ep['description'],
    )
    for ep in episodes
]

# Generate and output the RSS feed
rss = podcast.rss_str()
with open('podcast.rss', 'w') as outfile:
    outfile.write(rss)
