from unittest import TestCase
from mock import call, patch

class TestDeploymentScript(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('fabfile.frappe.run')
    def test_deployment(self, mock_run):
        from fabfile.frappe import upgrade
        upgrade()
        self.assertEqual(mock_run.call_args, call('bench upgrade'))
