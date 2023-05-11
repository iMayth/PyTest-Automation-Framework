import pytest

from src.pom.tests.Testbase import BaseTest


class TestCheckOut(BaseTest):

    def testtest(self):
        self.checkout_page.testing(self)
