#!/usr/bash/env python3

import requests
import json
from config import API_KEY

def get_player_stats(platform, epic_nickname):
    url = f'https://api.fortnitetracker.com/v1/profile/{platform}/{epic_nickname}'
    headers = {'TRN-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None


def parse_player_stats(data):
    stats = data['stats']['p2']
    overall_stats = {}

    overall_stats['kills'] = stats['kills']['value']
    overall_stats['matches'] = stats['matches']['value']
    overall_stats['wins'] = stats['top1']['value']
    overall_stats['kd'] = stats['kd']['value']
    overall_stats['win_rate'] = stats['winRatio']['value']

    return overall_stats