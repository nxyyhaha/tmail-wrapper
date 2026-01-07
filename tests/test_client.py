import unittest
from unittest.mock import patch, Mock

from tmail_api.client import TMail


class TestTMailClient(unittest.TestCase):
    def setUp(self):
        self.client = TMail('https://api.example.com/api', 'key123')

    @patch('tmail_api.client.requests.get')
    def test_domains(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'ok': True})
        self.assertEqual(self.client.domains(), {'ok': True})

    @patch('tmail_api.client.requests.get')
    def test_create(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'email': 'a@b.com'})
        self.assertEqual(self.client.create(), {'email': 'a@b.com'})

    @patch('tmail_api.client.requests.get')
    def test_messages(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: [])
        self.assertEqual(self.client.messages('a@b.com'), [])

    @patch('tmail_api.client.requests.delete')
    def test_delete(self, mock_delete):
        mock_delete.return_value = Mock(status_code=200, json=lambda: {'deleted': 1})
        self.assertEqual(self.client.delete_message(123), {'deleted': 1})

    def test_clean_message(self):
        sample = {
            'id': 1,
            'subject': 'Hello',
            'sender_name': 'Me',
            'sender_email': 'me@example.com',
            'date': 'Now',
            'datediff': 'just now',
            'content': '<div>Hello <b>World</b>!<br>\nSent with <a href="https://proton.me">Proton Mail</a></div>',
            'attachments': []
        }
        cleaned = self.client.clean_message(sample)
        self.assertEqual(cleaned['id'], 1)
        self.assertIn('Hello World', cleaned['content'])


if __name__ == '__main__':
    unittest.main()
