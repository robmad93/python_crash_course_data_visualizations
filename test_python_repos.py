import unittest
import requests


class TestPythonRepos(unittest.TestCase):

    def setUp(self):
        """Make an API call and store the response."""
        self.url = (
            "https://api.github.com/search/repositories?q=language:python&sort=stars"
        )
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        self.response = requests.get(self.url, headers=self.headers)
        self.response_dict = self.response.json()

    def test_status_code(self):
        """Test that the API call was successful."""
        self.assertEqual(self.response.status_code, 200)

    def test_total_repositories(self):
        """ "Test that the total no. of repositories is greater than a given amount."""
        self.assertGreater(self.response_dict["total_count"], 50000)

    def test_number_of_items(self):
        """Test that the no. of items returned is as expected."""
        self.assertEqual(
            len(self.response_dict["items"]), 30
        )  # Default number of items per page


if __name__ == "__main__":
    unittest.main()
