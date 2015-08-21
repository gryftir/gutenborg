#!/usr/bin/env python
"""
docstring settings

"""
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), 'env', '.env')
load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_DATABASE_URI = ''
    pass


class DevConfig(Config):
    DEBUG = True
    pass

config = {'development': DevConfig}


def main():
    pass

if __name__ == "__main__":
    main()
    pass
