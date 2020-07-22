# coding=utf-8

import os
import sys
import unittest
import glob

dirname = os.path.abspath(os.path.join(__file__, '../..'))

if dirname not in sys.path:
    sys.path.insert(0, dirname)


class BaseTestCase(unittest.TestCase):

    @staticmethod
    def main():
        return unittest.main()


def get_test_modules(dirname=None):
    modules = []
    if not dirname:
        dirname = os.path.dirname(__file__)
    for path, dirs, files in os.walk(dirname):
        for filename in files:
            if not filename.startswith('test_'):
                continue
            if not filename.endswith('.py'):
                continue
            modulename = filename[:-3]
            modules.append(modulename)
    return modules


def run_tests(modules):
    import importlib
    suite = unittest.TestSuite()
    for name in modules:
        module = importlib.import_module(name)
        if hasattr(module, 'TestCase'):
            suite.addTest(unittest.makeSuite(module.TestCase))

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_tests(get_test_modules())
