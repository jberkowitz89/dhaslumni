from dhsalumni.league.get_league import get_league
from dhsalumni.league.league_config import LEAGUE_ID, ESPN_S2, SWID
from dhsalumni.data.extract_data import get_settings, get_weekly_matchups

if __name__ == '__main__':
    league = get_league(league_id=LEAGUE_ID, year=2009, espn_s2=ESPN_S2, swid=SWID)
    settings = get_settings(league)
    matchups_lst = get_weekly_matchups(league)

    print(league)
    print(settings)
    print(matchups_lst[0:5])

