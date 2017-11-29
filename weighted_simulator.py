"""Facebook Markov Simulator"""

import json
import sys
import markovify
import markov_novel

def gen_from_graph_api_json(file_name, state_size=2):
    """
    Generates novel from Graph API result file
    You curl it using `/[id]/`
    """

    models_weights = []

    for post in json.load(open(file_name + '.json', encoding='utf-8'))['feed']['data']:
        try:
            if 'message' in post and 'count' in post['likes']:
                try:
                    models_weights.append(
                        (
                            markovify.NewlineText(post['message'], state_size),
                            post['likes']['count']
                            )
                        )
                except KeyError:
                    pass
        except KeyError:
            pass

    models, weights = map(list, zip(*models_weights))
    markov_novel.Novel(
        markovify.combine(models, weights), chapter_count=1
    ).write(novel_title='novel', filetype='md')

if __name__ == '__main__':
    gen_from_graph_api_json(sys.argv[1])
