#!/usr/bin/env python
"""
docstring get_marc_test.py

"""
import unittest
from mock import Mock, MagicMock, mock_open, patch
from app import get_marc


class marcTest(unittest.TestCase):
    def test_download_success(self):
        in_file = Mock()
        out_file = "test.marc"
        in_file.getcode = MagicMock(return_value=200)
        self.assertTrue(get_marc.download_success(in_file, out_file))
        in_file.getcode = MagicMock(return_value=300)
        self.assertFalse(get_marc.download_success(in_file, out_file))

    def test_bz2_to_file_from_url(self):
        m = mock_open()
        de = Mock()
        de.decompress = Mock(return_value=3)
        in_file = MagicMock()

        def foo(size):
            if foo.count < 3:
                foo.count += 1
                return size
            return None

        foo.count = 0
        in_file.read = foo
        with patch.object(get_marc, 'BZ2Decompressor', de):
            with patch.object(get_marc, 'open', m):
                self.assertTrue(get_marc.get_bz2_from_file(in_file, 'name',
                                                           lambda x, y: True))
                self.assertFalse(get_marc.get_bz2_from_file(
                    in_file, 'name', lambda x, y: False))
        handle = m()
        self.assertEqual(handle.write.call_count, 3)


if __name__ == "__main__":
    unittest.main()
