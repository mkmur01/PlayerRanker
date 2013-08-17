#!/usr/bin/env python

# -------
# imports
# -------

import sys
import os

APP_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(APP_PATH + '/app')
sys.path.append(APP_PATH + '/app/league')

from Ranker import Ranker
from LeagueFactory import LeagueFactory
from PlayerFactory import PlayerFactory

# ----
# main
# ----

leagueFactory = LeagueFactory()
league = leagueFactory.getLeague(sys.stdin, sys.stdout)

ranker = Ranker(league, sys.stdin, sys.stdout)
ranker.run()