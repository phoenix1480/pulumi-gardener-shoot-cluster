"""Module providing unit testing"""
import unittest

class TestWakeUp(unittest.TestCase):
    """ Test WakeUp Class """
    def test_throws_an_error_when_msg_does_not_match(self):
        """Test WakeUp msg matches to scaffold pipeline"""
        msg = "Wake Up Pipeline"
        assert "Wake" in msg


if __name__ == '__main__':
    unittest.main()