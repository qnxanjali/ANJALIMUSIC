import json
import os

from SUHANIMUSIC.core.bot import SUHANI
from SUHANIMUSIC.core.dir import dirr
from SUHANIMUSIC.core.git import git
from SUHANIMUSIC.core.userbot import Userbot
from VIPMUSIC.core.youtube import SUHANI
from SUHANIMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()
SUHANI()

app = SUHANI()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
HELPABLE = {}
