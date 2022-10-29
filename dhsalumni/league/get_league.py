from espn_api.football import League

def get_league(league_id:int, year:int, espn_s2:str = None, swid:str = None):
    '''
    docstring placeholder
    '''
    league = League(league_id, year, espn_s2, swid)
    return league

