import argparse
import sys


def get_args():
    try:
        parser = argparse.ArgumentParser(description='default argument')
        parser.add_argument("-sport", "--sport_id", help="oddsbox.meta_cmm_sport.sport_id", required=True)
        return parser.parse_args()
    except:
        sys.exit(1)
