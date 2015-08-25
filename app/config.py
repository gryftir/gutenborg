#!/usr/bin/env python
"""
docstring settings

"""
from os.path import join, dirname, abspath
from dotenv import load_dotenv


dotenv_path = abspath(join(dirname(__file__), '../env', '.env'))
load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_DATABASE_URI = ''


class DevConfig(Config):
    DEBUG = True


config = {'development': DevConfig}


def main():
    pass

if __name__ == "__main__":
    main()
    pass
