from league_config import LEAGUE_ID, ESPN_S2, SWID
from espn_api.football import League

def get_league(league_id:int, year:int, espn_s2:str = None, swid:str = None):
    '''
    docstring placeholder
    '''
    league = League(league_id, year, espn_s2, swid)
    return league

if __name__ == "__main__":
    get_league(league_id=LEAGUE_ID, year=2018, espn_s2=ESPN_S2, swid=SWID)
