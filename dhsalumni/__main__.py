from dhsalumni.league.get_league import get_league
from dhsalumni.league.league_config import LEAGUE_ID, ESPN_S2, SWID
from dhsalumni.extract_data import get_settings, get_draft, get_weekly_matchups

if __name__ == '__main__':
    league = get_league(league_id=LEAGUE_ID, year=2009, espn_s2=ESPN_S2, swid=SWID)
    settings = get_settings(league)
    draft = get_draft(league)
    matchups = get_weekly_matchups(league)

    print(league)
    print(settings)
    print(draft[0:5])
    print(matchups[0])


