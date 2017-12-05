"""FB Markov Simulator
    Twitter Bot Version
"""

import json
import sys
import markovify
import markov_novel

def gen_from_graph_api_json(file_name, state_size=2, chapter_count=3):
    """
    Generates novel from Graph API result file
    """

    models_weights = []

    for post in json.load(open(file_name + '.json', encoding='utf-8'))['feed']['data']:
        try:
            if 'message' in post and 'count' in post['likes']:
                models_weights.append(
                    (
                        markovify.Text(post['message'], state_size),
                        post['likes']['count']
                    )
                )

        except KeyError:
            pass

    (models, weights), models_weights = (map(list, zip(*models_weights)), None)

    markov_novel.Novel(
        markovify.combine(models, weights), chapter_count
    ).write(novel_title=file_name, filetype='md')

def gen_from_twitter_api_json(file_name, state_size=2, chapter_count=1):
    """
    Generates Tweets from Twitter API result file
    """

    models_weights = []

    for post in json.load(open(file_name + '.json', encoding='utf-8')):
        post = json.loads(post)
        try:
            if 'text' in post and 'favorite_count' in post:
                models_weights.append(
                    (
                        markovify.Text(post['text'], state_size),
                        post['favorite_count']
                    )
                )

        except KeyError:
            pass

    (models, weights), models_weights = (map(list, zip(*models_weights)), None)

    markov_novel.Novel(
        markovify.combine(models, weights), chapter_count
    ).write(novel_title='tweet_{0}'.format(file_name), filetype='txt')
