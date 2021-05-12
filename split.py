from pyimagesearch import config
import splitfolders

# Split with a ratio.
# To only split into training and validation set, set a tuple to ratio, i.e, (.8, .2).

splitfolders.ratio(config.ORIG_INPUT_DATASET, output=config.BASE_PATH, seed=1337, ratio=(.5, .2, .3), group_prefix=None)  # default values
