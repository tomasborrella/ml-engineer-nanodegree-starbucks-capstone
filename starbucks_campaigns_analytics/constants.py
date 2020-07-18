from pathlib import Path


# PATH_PROJECT will be called from the root of the project or from a subfolder
PATH_PROJECT = (
    Path('.') if Path('.').resolve().name == 'starbucks-capstone-challenge'
    else Path('..')
)

PATH_DATA = PATH_PROJECT / 'data'
PATH_MODELS = PATH_PROJECT / 'models'
PATH_REPORTS = PATH_PROJECT / 'reports'

RANDOM_STATE = 42
MIN_VALUE_TRANSACTION = 10
