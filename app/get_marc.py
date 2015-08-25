#!/usr/bin/env python
"""
docstring get_marc.py

"""
import urllib2
from bz2 import BZ2Decompressor
from os import remove, path
import pymarc
import json
import io

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
    with open(out_file_name, 'wb') as fh:
        while True:
            chunk = in_file.read(CHUNK)
            if not chunk:
                break
            fh.write(bz2.decompress(chunk))
    return True


def get_list_from_marc(in_file):
    data = []
    reader = pymarc.MARCReader()
    for record in reader:
        d = {}
        d['author'] = record.author()
        d['title'] = record.title()
        d['isbn'] = record.isbn()
        d['uniformtitle'] = record.uniformtitle()
        d['series'] = record.series()
        d['subjects'] = record.subjects()
        d['addedentries'] = record.addedentries()
        d['notes'] = record.notes()
        d['physicaldescription'] = record.physicaldescription()
        d['publisher'] = record.publisher()
        d['pubyear'] = record.pubyear()
        # marc21 fields
        d['fields'] = record.as_dict()
        data.append(d)
    return data


def to_json(l):
    return unicode(json.dumps(l, ensure_ascii=False))


def sort_marc_title_ascending(l):
    return sorted(l, key=lambda x: x.get('uniformtitle', x.get('title')))


def write_str_to_file(out_file, json_str):
    out_file.write(json_str)


def marc_to_json_format(marc_file):
    return to_json(sort_marc_title_ascending(get_list_from_marc(marc_file)))


def write_json_to_file(marc_file, json_file):
    write_str_to_file(json_file, marc_to_json_format(marc_file))


def marc_to_json_open(marc_file_name, json_file_name, func=write_json_to_file):
    if not path.isfile(marc_file_name):
        return False
    if path.isfile(json_file_name):
        remove(json_file_name)
    with open(marc_file_name, 'rb') as marc_file:
        with io.open(json_file_name, 'w', encoding='utf-8') as json_file:
            func(marc_file, json_file)
    return True


def main():
    fp = urllib2.urlopen('http://www.gutenberg.org/feeds/catalog.marc.bz2')
    result = get_bz2_from_file(fp, 'test.marc', download_success)
    print str(result)


if __name__ == "__main__":
    main()
