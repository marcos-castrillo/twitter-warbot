from services.images import *
from services.map_image import get_map_image_preview
from services.api import initialize_avatars
from services.simulation import write_tweet
from services.store import introduction_tweet_list

initialize_avatars()
print('Preparing preview...')
raw_map_img = Image.open(os.path.join(current_dir, config.file_paths.map, config.general.run_name + '.png'))
map_image = get_map_image_preview(raw_map_img)
if not os.path.exists('./simulations'):
    os.makedirs('./simulations')
if not os.path.exists('./simulations/preview'):
    os.makedirs('./simulations/preview')
map_image.save('./simulations/preview/map_preview.png')
if config.general.match_type == MatchType.districts:
    for i, tweet in enumerate(introduction_tweet_list):
        write_tweet(tweet)
print('Preview is ready')
