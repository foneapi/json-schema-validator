"""
Module with unit tests for launch_control.models package
"""

import unittest

from launch_control.models import (
        DashboardBundle,
        HardwareContext,
        HardwareDevice,
        SoftwareContext,
        SoftwareImage,
        SoftwarePackage,
        TestCase,
        TestResult,
        TestRun,
        )


class DashboardBundleTests(unittest.TestCase):

    def test_format(self):
        self.assertEqual(DashboardBundle.FORMAT, "Dashboard Bundle Format 1.0")

    def test_construction_1(self):
        bundle = DashboardBundle()
        self.assertEqual(bundle.format, DashboardBundle.FORMAT)
        self.assertEqual(bundle.test_runs, [])

    def test_construction_2(self):
        format = object()
        bundle = DashboardBundle(format)
        self.assertTrue(bundle.format is format)
        self.assertEqual(bundle.test_runs, [])

    def test_construction_3(self):
        format = object()
        test_runs = object()
        bundle = DashboardBundle(format, test_runs)
        self.assertTrue(bundle.format is format)
        self.assertTrue(bundle.test_runs is test_runs)

    def test_construction_4(self):
        format = object()
        test_runs = object()
        bundle = DashboardBundle(format=format, test_runs=test_runs)
        self.assertTrue(bundle.format is format)
        self.assertTrue(bundle.test_runs is test_runs)

    def test_get_json_attr_types(self):
        self.assertEqual(DashboardBundle.get_json_attr_types(),
                {'test_runs': [TestRun]})


class HardwareContextTests(unittest.TestCase):

    def test_construction_1(self):
        hw_context = HardwareContext()
        self.assertEqual(hw_context.devices, [])

    def test_construction_2(self):
        devices = object()
        hw_context = HardwareContext(devices)
        self.assertTrue(hw_context.devices is devices)

    def test_construction_3(self):
        devices = object()
        hw_context = HardwareContext(devices=devices)
        self.assertTrue(hw_context.devices is devices)

    def test_get_json_attr_types(self):
        self.assertEqual(HardwareContext.get_json_attr_types(),
                {'devices': [HardwareDevice]})


class HardwareDeviceTests(unittest.TestCase):

    def test_construction_1(self):
        device_type = object()
        description = object()
        hw_device = HardwareDevice(device_type, description)
        self.assertTrue(hw_device.device_type is device_type)
        self.assertTrue(hw_device.description is description)
        self.assertEqual(hw_device.attributes, {})

    def test_construction_2(self):
        device_type = object()
        description = object()
        attributes = object()
        hw_device = HardwareDevice(device_type, description, attributes)
        self.assertTrue(hw_device.device_type is device_type)
        self.assertTrue(hw_device.description is description)
        self.assertTrue(hw_device.attributes is attributes)

    def test_construction_3(self):
        device_type = object()
        description = object()
        attributes = object()
        hw_device = HardwareDevice(device_type=device_type,
                description=description, attributes=attributes)
        self.assertTrue(hw_device.device_type is device_type)
        self.assertTrue(hw_device.description is description)
        self.assertTrue(hw_device.attributes is attributes)

    def test_get_json_attr_types(self):
        self.assertRaises(NotImplementedError,
                HardwareDevice.get_json_attr_types)

    def test_device_types(self):
        self.assertEqual(HardwareDevice.DEVICE_CPU, "device.cpu")
        self.assertEqual(HardwareDevice.DEVICE_MEM, "device.mem")
        self.assertEqual(HardwareDevice.DEVICE_USB, "device.usb")
        self.assertEqual(HardwareDevice.DEVICE_PCI, "device.pci")
        self.assertEqual(HardwareDevice.DEVICE_BOARD, "device.board")


class SoftwareContextTests(unittest.TestCase):

    def test_construction_1(self):
        sw_context = SoftwareContext()
        self.assertEqual(sw_context.packages, [])
        self.assertTrue(sw_context.sw_image is None)

    def test_construction_2(self):
        packages = object()
        sw_context = SoftwareContext(packages)
        self.assertTrue(sw_context.packages is packages)
        self.assertTrue(sw_context.sw_image is None)

    def test_construction_3(self):
        packages = object()
        sw_image = object()
        sw_context = SoftwareContext(packages, sw_image)
        self.assertTrue(sw_context.packages is packages)
        self.assertTrue(sw_context.sw_image is sw_image)

    def test_construction_4(self):
        packages = object()
        sw_image = object()
        sw_context = SoftwareContext(packages=packages, sw_image=sw_image)
        self.assertTrue(sw_context.packages is packages)
        self.assertTrue(sw_context.sw_image is sw_image)

    def test_get_json_attr_types(self):
        self.assertEqual(SoftwareContext.get_json_attr_types(),
                {'packages': [SoftwarePackage], 'sw_image': SoftwareImage})
    

class SoftwareImageTests(unittest.TestCase):

    def test_construction_1(self):
        name = object()
        sw_image = SoftwareImage(name)
        self.assertTrue(sw_image.name is name)

    def test_construction_2(self):
        name = object()
        sw_image = SoftwareImage(name=name)
        self.assertTrue(sw_image.name is name)

    def test_get_json_attr_types(self):
        self.assertRaises(NotImplementedError,
                SoftwareImage.get_json_attr_types)


class SoftwarePackageTests(unittest.TestCase):

    def test_construction_1(self):
        name = object()
        version = object()
        sw_package = SoftwarePackage(name, version)
        self.assertTrue(sw_package.name is name)
        self.assertTrue(sw_package.version is version)

    def test_construction_2(self):
        name = object()
        version = object()
        sw_package = SoftwarePackage(name=name, version=version)
        self.assertTrue(sw_package.name is name)
        self.assertTrue(sw_package.version is version)

    def test_get_json_attr_types(self):
        self.assertRaises(NotImplementedError,
                SoftwarePackage.get_json_attr_types)


class TestCaseTests(unittest.TestCase):
    
    def test_construction_1(self):
        test_case_id = object()
        name = object()
        test_case = TestCase(test_case_id, name)
        self.assertTrue(test_case.test_case_id is test_case_id)
        self.assertTrue(test_case.name is name)

    def test_construction_2(self):
        test_case_id = object()
        name = object()
        test_case = TestCase(test_case_id=test_case_id, name=name)
        self.assertTrue(test_case.test_case_id is test_case_id)
        self.assertTrue(test_case.name is name)

    def test_get_json_attr_types(self):
        self.assertRaises(NotImplementedError,
                TestCase.get_json_attr_types)


class TestResultTests(unittest.TestCase):
    
    def test_construction_1(self):
        # result cannot be none
        test_case_id = None
        result = None
        self.assertRaises(TypeError, TestResult, test_case_id, result)

    def test_construction_2(self):
        test_case_id = None
        for result in [
                TestResult.RESULT_PASS,
                TestResult.RESULT_FAIL,
                TestResult.RESULT_SKIP,
                TestResult.RESULT_UNKNOWN]:
            test_result = TestResult(test_case_id, result)
            self.assertTrue(test_result.test_case_id is None)
            self.assertEqual(test_result.result, result)

    def test_construction_3(self):
        for test_case_id in [
                # Characters valid in the first mandatory segment
                "_",
                "-",
                "0",
                "9",
                "a",
                "z",
                "A",
                "Z",
                # Characters valid in the second optional segment
                "first._",
                "first.-",
                "first.0",
                "first.9",
                "first.a",
                "first.z",
                "first.A",
                "first.Z",
                ]:
            result = TestResult.RESULT_PASS # not relevant
            test_result = TestResult(test_case_id, result)
            self.assertEqual(test_result.test_case_id, test_case_id)

    def test_construction_4(self):
        for test_case_id in [
                "", # empty test case id is not valid, use None instead
                " ", # whitespace not allowed
                "\n",
                "\t",
                "\r",
                ".", # first segment cannot be empty
                "first.", # subsequent segments cannot be empty
                ]:
            result = TestResult.RESULT_PASS # not relevant
            self.assertRaises(ValueError, TestResult, test_case_id, result)
