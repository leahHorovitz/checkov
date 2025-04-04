import os
import unittest

from checkov.runner_filter import RunnerFilter
from checkov.terraform.runner import Runner
from checkov.terraform.checks.resource.azure.AppServiceRemoteDebuggingNotEnabled import check


class TestAppServiceRemoteDebuggingNotEnabled(unittest.TestCase):

    def test(self):
        runner = Runner()
        current_dir = os.path.dirname(os.path.realpath(__file__))

        test_files_dir = os.path.join(current_dir, "example_AppServiceRemoteDebuggingNotEnabled")
        report = runner.run(root_folder=test_files_dir,
                            runner_filter=RunnerFilter(checks=[check.id]))
        summary = report.get_summary()

        passing_resources = {
            'azurerm_app_service.pass',
            'azurerm_windows_web_app.pass',
            'azurerm_linux_web_app.pass',
            'azurerm_linux_function_app.pass',
            'azurerm_linux_function_app_slot.pass',
            'azurerm_linux_web_app_slot.pass',
            'azurerm_windows_function_app.pass',
            'azurerm_windows_function_app_slot.pass',
            'azurerm_windows_web_app_slot.pass',
            'azurerm_app_service.pass2',
            'azurerm_windows_web_app.pass2',
            'azurerm_linux_web_app.pass2',
            'azurerm_linux_function_app.pass2',
            'azurerm_linux_function_app_slot.pass2',
            'azurerm_linux_web_app_slot.pass2',
            'azurerm_windows_function_app.pass2',
            'azurerm_windows_function_app_slot.pass2',
            'azurerm_windows_web_app_slot.pass2',
        }
        failing_resources = {
            'azurerm_app_service.fail',
            'azurerm_windows_web_app.fail',
            'azurerm_linux_web_app.fail',
            'azurerm_linux_function_app.fail',
            'azurerm_linux_function_app_slot.fail',
            'azurerm_linux_web_app_slot.fail',
            'azurerm_windows_function_app.fail',
            'azurerm_windows_function_app_slot.fail',
            'azurerm_windows_web_app_slot.fail',
        }
        skipped_resources = {}

        passed_check_resources = set([c.resource for c in report.passed_checks])
        failed_check_resources = set([c.resource for c in report.failed_checks])

        self.assertEqual(summary['passed'], len(passing_resources))
        self.assertEqual(summary['failed'], len(failing_resources))
        self.assertEqual(summary['skipped'], len(skipped_resources))
        self.assertEqual(summary['parsing_errors'], 0)

        self.assertEqual(passing_resources, passed_check_resources)
        self.assertEqual(failing_resources, failed_check_resources)
