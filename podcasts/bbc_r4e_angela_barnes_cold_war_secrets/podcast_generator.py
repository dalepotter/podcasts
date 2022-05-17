import pytz
from datetime import datetime, timedelta
from podgen import Podcast, Episode, Media


# Create the Podcast
podcast = Podcast(
    name="Angela Barnes' Cold War Secrets",
    description="Angela Barnes explores one of modern history’s most fascinating, frightening and relevant periods.",
    website="https://www.bbc.co.uk/programmes/m000mdbq",
    explicit=False,
    image="https://ia801501.us.archive.org/17/items/bbc-radio-4-extra-angela-barnes-cold-war-secrets/BBC%20Radio%204%20Extra%20-%20Angela%20Barnes%27%20Cold%20War%20Secrets.png"
)

podcast.episodes = [
    Episode(
        title="Le Carre on Spying",
        media=Media(
            "https://archive.org/download/bbc-radio-4-extra-angela-barnes-cold-war-secrets/BBC%20Radio%204%20Extra%20-%20Angela%20Barnes%27%20Cold%20War%20Secrets%20-%201.mp3",
            size=56203674,
            duration=timedelta(minutes=59, seconds=21)
        ),
        publication_date=datetime(year=2020, month=9, day=9, hour=11).replace(tzinfo=pytz.timezone('Europe/London')),
        summary="""Angela Barnes explores one of modern history’s most fascinating, frightening and relevant periods.

In the first of three programmes – she brings a unique and surprising insight into the Cold War.

Using a perfect blend of both factual and comic archive and studio interviews, Angela reveals what we didn't know then but we do know now - from bunkers and other civil defence plans, to the Royal Observer Corps, numbers stations and the secret police services behind the Iron Curtain.

Featuring:

* The Penny Dreadfuls Present: Le Carre on Spying [BBC Radio 4 08/04/2017]
* A very special comedy offering from sketch group. Prepare to enter 1960s Germany and a hotbed of intrigue and espionage, starring Miles Jupp and Mark Heap.

Producer: Adnan Ahmed

Made for BBC Radio 4 Extra by for BBC Studios and first broadcast in January 2019,
""".replace('\n', '<br />')
    ),
    Episode(
        title="Bunkers and Jigsaws",
        media=Media(
            "https://archive.org/download/bbc-radio-4-extra-angela-barnes-cold-war-secrets/BBC%20Radio%204%20Extra%20-%20Angela%20Barnes%27%20Cold%20War%20Secrets%20-%202.mp3",
            size=45927629,
            duration=timedelta(minutes=57, seconds=18)
        ),
        publication_date=datetime(year=2020, month=9, day=16, hour=11).replace(tzinfo=pytz.timezone('Europe/London')),
        summary="""Comedian Angela Barnes is an ardent nuclear bunker enthusiast with a passion for all things Cold War. Angela's Edinburgh show - Fortitude - featured nuclear bunkers heavily and whilst at The Festival, Angela performed her show in a decommissioned Cold War bunker in Fife.

Featuring a perfect blend of archive and studio interviews, Angela Barnes explores this fascinating, frightening and relevant period in modern history. Over three episodes, she uses both factual and comic archive to reveal what we didn't know then but we do know now, the show brings a unique and surprising insight into the Cold War - from bunkers and other civil defence plans, to the Royal Observer Corps, numbers stations and the secret police services behind the Iron Curtain.

Angela speaks to ‘Stasiland’ author Anna Funder, ‘German Comedy Ambassador’, Henning When and Edinburgh Comedy Award-winner John Robins.

The second of three selections features:

’Beyond the Fringe’
‘Broadcasts from the Bunker’
‘The Stasi Jigsaw Puzzle’

Producer: Adnan Ahmed for BBC Studios

Made for BBC Radio 4 Extra and first broadcast in January 2019.
""".replace('\n', '<br />')
    ),
    Episode(
        title="The Bed Sitting Room",
        media=Media(
            "https://archive.org/download/bbc-radio-4-extra-angela-barnes-cold-war-secrets/BBC%20Radio%204%20Extra%20-%20Angela%20Barnes%27%20Cold%20War%20Secrets%20-%203.mp3",
            size=55993958,
            duration=timedelta(minutes=59, seconds=39)
        ),
        publication_date=datetime(year=2020, month=9, day=23, hour=11).replace(tzinfo=pytz.timezone('Europe/London')),
        summary="""Comedian Angela Barnes is an ardent nuclear bunker enthusiast with a passion for all things Cold War.

Angela's Edinburgh show - Fortitude - featured nuclear bunkers heavily and whilst at The Festival, Angela performed her show in a decommissioned Cold War bunker in Fife.

In this final instalment of interviews, clips and programmes, Angela chooses the remake of a bleak post-apocalyptic classic.

‘The Bed Sitting Room’ [Radio 4, 2015]

Producer: Adnan Ahmed for BBC Studios

Made for BBC Radio 4 Extra and first broadcast in January 2019.
""".replace('\n', '<br />')
    ),
]

# Generate and output the RSS feed
rss = podcast.rss_str()
with open('podcast.rss', 'w') as outfile:
    outfile.write(rss)
