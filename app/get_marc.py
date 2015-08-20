#!/usr/bin/env python
"""
docstring get_marc.py

"""
import urllib2
from bz2 import BZ2Decompressor
from os import remove, path
# import sqlalchemy


# todo add code to compare with existing file
def download_success(in_file, out_file_name):
    return int(in_file.getcode()) == 200


# todo add function to handle marc file and store immediately in database
def get_bz2_from_file(in_file, out_file_name, file_is_good):
    if not file_is_good(in_file, out_file_name):
        return False
    bz2 = BZ2Decompressor()
    CHUNK = 16384
    if path.isfile(out_file_name):
        remove(out_file_name)
    with open(out_file_name, 'wb') as fp:
        while True:
            chunk = in_file.read(CHUNK)
            if not chunk:
                break
            fp.write(bz2.decompress(chunk))
    return True


def main():
    fp = urllib2.urlopen('http://www.gutenberg.org/feeds/catalog.marc.bz2')
    result = get_bz2_from_file(fp, 'test.marc', download_success)
    print str(result)


if __name__ == "__main__":
    main()
