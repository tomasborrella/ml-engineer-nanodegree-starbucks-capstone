from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
import pandas_profiling

from .constants import PATH_DATA, PATH_REPORTS, RANDOM_STATE


def read_portfolio_data() -> pd.DataFrame:
    """Reads portfolio data (offers data) and returned it as a clean dataframe
    """
    portfolio_raw = pd.read_json(PATH_DATA / 'portfolio.json',
                                 orient='records',
                                 lines=True)

    # Create new columns with the information in 'channels' column
    # 2nd row contains all possible channels
    channels_columns = portfolio_raw.loc[1, 'channels']

    for col in channels_columns:
        portfolio_raw[col] = portfolio_raw.channels.apply(
            lambda x: 1 if col in x else 0)
    portfolio = portfolio_raw.drop(columns='channels')

    # Convert duration column from days to hours
    portfolio['duration'] = portfolio['duration'].apply(lambda x: x * 24)
    return portfolio


def read_profile_data() -> pd.DataFrame:
    """Reads profile data (users data) and returned it as a clean dataframe
    """
    profile_raw = pd.read_json(PATH_DATA / 'profile.json',
                               orient='records',
                               lines=True)

    # Clean: Drop profiles with wrong data
    profile = profile_raw.dropna(subset=['gender']).copy()

    # New column with antiguity (days_since_became_member)
    profile['became_member_on'] = pd.to_datetime(profile['became_member_on'],
                                                 format='%Y%m%d')
    # Get the most recent date
    last_date = profile.sort_values(
        by=['became_member_on'], ascending=False
    ).iloc[0]['became_member_on']

    # Create de new column 'days_since_became_member'
    profile['days_since_became_member'] = (
                last_date - profile['became_member_on']).dt.days

    profile = profile.drop(columns='became_member_on')


    # Let's create profile groups using KMeans
    select_columns = ['gender', 'age', 'income', 'days_since_became_member']
    profile_for_kmeans = profile[select_columns]

    # gender dummy variable
    profile_for_kmeans = (
        profile_for_kmeans
            .join(pd.get_dummies(profile_for_kmeans['gender'], prefix='gender'))
            .drop(columns='gender')
    )

    # Fit KMeans with 2 cluster (Elbow result)
    kmeans = KMeans(n_clusters=2, random_state=RANDOM_STATE)
    kmeans.fit(profile_for_kmeans)

    # Make prediction and add the new group column
    kmeans_predictions = kmeans.predict(profile_for_kmeans)
    profile['profile_group'] = kmeans_predictions

    return profile


def read_transcript_data() -> pd.DataFrame:
    """Reads transcript data (events data) and returned it as a clean dataframe
    """
    transcript_raw = pd.read_json(PATH_DATA / 'transcript.json',
                                  orient='records',
                                  lines=True)

    # Clean: Create new columns with the information in 'value' column

    value_columns = ['offer_id', 'amount', 'offer_id_aux', 'reward_expected']

    transcript_raw[value_columns] = (
        pd.json_normalize(transcript_raw['value'])
    )

    # Combine offer columns in only one column
    transcript_raw['offer_id'] = (
        transcript_raw['offer_id'].combine_first(transcript_raw['offer_id_aux'])
    )

    # Drop original value column and offer aux column
    transcript = transcript_raw.drop(columns=['value', 'offer_id_aux'])
    return transcript


def read_complete_starbucks_data() -> pd.DataFrame:
    """Reads all starbucks data and formatted it
    getting a unique data frame with all info
    """
    # Get the three data sets (and clean it)
    profile = read_profile_data()
    portfolio = read_portfolio_data()
    transcript = read_transcript_data()

    # Merge the three data sets

    # Merge transcript with profile
    transcript_joined_profile = (
        transcript
            .merge(profile,
                   left_on='person',
                   right_on='id',
                   how='inner')
            .drop(columns='id')
    )

    # Final merge with portfolio
    df_transcript_joined_profile_and_portfolio = (
        transcript_joined_profile
            .merge(portfolio,
                   left_on='offer_id',
                   right_on='id',
                   how='left')
            .drop(columns='id')
    )

    return df_transcript_joined_profile_and_portfolio


def pandas_profiling_to_file(df_to_profile: pd.DataFrame,
                             title: str,
                             output_filename: Path) -> None:
    """Alias for `pandas_profiling`, just takes `df_to_profile`
    and builds a report, saving it in `PATH_REPORTS` defined
    in submodule `constants.py`
    """
    if (PATH_REPORTS / output_filename).exists():
        print(f'File {output_filename} already exists')
    else:
        (df_to_profile
         .profile_report(title=title)
         .to_file(output_file=PATH_REPORTS / output_filename))
