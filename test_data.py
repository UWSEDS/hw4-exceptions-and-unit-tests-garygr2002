''' Unit tests for prime.py '''

import ntpath
import os
import platform
import unittest

from data import get_data
from data import remove_data


# The test directory, and a test URL that is known to exist
test_directory = "data/"
test_url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'


# create_file_name_from_url(): Create a file name from the test URL, including its path in the local file system.
def create_file_name_from_url():
    return '{}{}'.format(test_directory, ntpath.basename(test_url))


# create_test_file(): Create a dummy test file that simulates an existing download.
def create_test_file():
    f = open(create_file_name_from_url(), "w+")
    f.write("This is file has been written as part of a 'data.py' unit test.\r\n")
    f.close()
    return


# Borrowed from 'http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python'
def get_creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


# remove_test_file(): Removes a test file.  This may either be a legitimately downloaded file, or a dummy file.
def remove_test_file():
    file_name = create_file_name_from_url()
    if os.path.exists(file_name):
        os.remove(file_name)
    return


class TestData(unittest.TestCase):

    # Test for existing file get
    def testExistingFileGet(self):
        create_test_file()
        file_name = create_file_name_from_url()
        creation_date_before = get_creation_date(file_name)
        get_data(test_url)
        creation_date_after = get_creation_date(file_name)
        remove_test_file()
        self.assertTrue(creation_date_after == creation_date_before)

    # Test for missing file get
    def testMissingFileGet(self):
        remove_test_file()
        get_data(test_url)
        okay = os.path.isfile(create_file_name_from_url())
        remove_test_file()
        self.assertTrue(okay)

    # Test for missing URL get
    def testMissingUrlGet(self):
        exception_occurred = 0
        try:
            get_data('https://data.seattle.gov/resource/4xy5-26gyblahblahblah.csv')
        except FileNotFoundError:
            exception_occurred = 1
        self.assertTrue(exception_occurred == 1)

    # Test for existing file remove
    def testExistingFileRemove(self):
        create_test_file()
        remove_data(ntpath.basename(test_url))
        file_name = create_file_name_from_url()
        okay = os.path.isfile(file_name)
        remove_test_file()
        self.assertFalse(okay)

    # Test for missing file remove
    def testMissingFileRemove(self):
        remove_test_file()
        remove_data(ntpath.basename(test_url))
        file_name = create_file_name_from_url()
        okay = os.path.isfile(file_name)
        self.assertFalse(okay)

if __name__ == '__main__':
    unittest.main()
