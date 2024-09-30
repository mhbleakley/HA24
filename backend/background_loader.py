import os
import random

def shuffle_bgs(background_dir):
    backgrounds = os.listdir(background_dir)
    shuffled = random.sample(backgrounds, 10)
    return shuffled


def generate_background_html(backgrounds, background_dir, target_dir):
    html_str = ''
    for background in backgrounds:
        backgrounds_from_public = './'  + background_dir[9:]
        html_str += f'<img class="background_img" src="{backgrounds_from_public}/{background}" alt="background">\n'

    with open(target_dir + '/backgrounds.txt', 'w') as f:
        f.write(html_str)


# generate_background_html('./resources/backgrounds', './public/data')