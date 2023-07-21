from dhsalumni import __version__

def get_settings(league):
    '''
    docstring placeholder
    '''
    settings = league.settings
    attrs = vars(settings)
    attrs['year'] = league.year
    return vars(settings)

def get_weekly_matchups(league):
    '''
    docstring placeholder
    '''
    for i in range(len(league.settings.matchup_periods)):
        matchups_lst = league.scoreboard(week=i)
        all_scores = [matchup.data for matchup in matchups_lst]
    return all_scores


