from dhsalumni import __version__
from dhsalumni.league_config import LEAGUE_ID

def test_version():
    assert __version__ == '0.1.0'

def test_league_config():
    assert LEAGUE_ID == 470074