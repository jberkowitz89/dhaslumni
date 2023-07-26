from dhsalumni import __version__
from dhsalumni.league.get_league import get_league
from dhsalumni.league.league_config import LEAGUE_ID, ESPN_S2, SWID
from espn_api.football import League

import pytest

@pytest.fixture
def league():
    return League(league_id=470074, year=2018, espn_s2='AEBGBBUoNwFhTvh%2F%2Bt6fqRvaWPeXVCxhtEmmtWSSFuyZQWjJURqWS4fXxVHzaYOiNZgR3AOkbFZXUyX1yU%2FZKvvCmeT01wZNG0l%2FkkFhJLeS3jMD0lBfG6WTnUdRbVsynLk78g2lSNce4Jx4Pb17yXEQaTUWfMVcW%2Fovjl06eBl%2BJAtm8ClWXTlOe98XqtFBaTLbFyt0BgcpBDCWxv1RDpcQ4qX%2BmkwPE9szi5ifm0gjhtJchx06E5S5uYElFLYpoUpg7CqUvs4ID4uInwjZgiAs',
    swid='{0E55E5A5-3637-4BE0-86CF-E2E39B9938C9}')

def test_version():
    assert __version__ == '0.1.0'

def test_is_league(league):
    assert isinstance(league, League)
    assert league.league_id == 470074

def test_get_league(league):
   my_league = get_league(league_id=LEAGUE_ID, year=2018, espn_s2=ESPN_S2, swid=SWID)
   assert my_league.league_id == league.league_id
   assert my_league.year == league.year

