"""
Created on Tue Sep 19 2023
@author: lillygrella
"""
import unittest
import pandas as pd
from main import readin, get_summ_stats


class TestMain(unittest.TestCase):
    """
    evoke unit testing to confirm readin and sumstats work correctly
    """

    def test_readin(self):
        """
        test that the readin function correctly populates df as a pd.dataframe datatype
        """
        spy = readin()
        self.assertIsNotNone(spy)
        self.assertIsInstance(spy, pd.DataFrame)

    def test_sumstats(self):
        """
        confirms summary stats are being calculated correctly
        """
        spy = readin()
        series = get_summ_stats(spy)
        self.assertIsNotNone(series)

        assert spy["Close"].mean().round(2) == series.iloc[1].round(2)
        assert spy["Close"].count().round(2) == series.iloc[0].round(2)
        assert spy["Close"].median().round(2) == series.iloc[5].round(2)
        assert spy["Close"].std().round(2) == series.iloc[2].round(2)


# Run the tests
if __name__ == "__main__":
    unittest.main()
