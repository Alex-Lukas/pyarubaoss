# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.

"""

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubaoss.auth import *
from pyarubaoss.vlans import *
from test_machine import *


# TODO Remarked out failing tests


class TestGetVLANs(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self, admin, password):
        pass
    def TearDown(self):
        pass

    def test_get_dev_vlans(self):
        """
        test case for get_vlans

        """
        auth = AOSSAuth(switch, username, password)
        dev_vlans = get_vlans(auth)
        self.assertIs(type(dev_vlans), list)
        auth.logout()

class TestGetVLAN(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_get_dev_vlan(self):
        """
        test case for get_vlans

        """
        auth = AOSSAuth(switch, username, password)
        dev_vlan = get_vlan(auth, 1)
        self.assertIs(type(dev_vlan), dict)
        auth.logout()



class TestCreateVLAN(TestCase):
    """
    Test Case for pyarubaaoss vlans create vlans function
    """
    def setUp(self):
        auth = AOSSAuth(switch, username, password)
        delete_vlan(auth, 30)
        auth.logout()

    def tearDown(self):
        auth = AOSSAuth(switch, username, password)
        delete_vlan(auth, 30)
        auth.logout()

    def test_create_dev_vlan(self):
        """
        test case for get_vlans

        """
        auth = AOSSAuth(switch, username, password)
        new_vlan = create_vlan(auth, 30, "Test2")
        self.assertEqual(new_vlan, 201)
        auth.logout()


class TestModifyVLAN(TestCase):
    """
    Test Case for pyarubaaoss vlans create vlans function
    """
    def setUp(self):
        auth = AOSSAuth(switch, username, password)
        create_vlan(auth, 30, "Test2")
        auth.logout()

    def tearDown(self):
        auth = AOSSAuth(switch, username, password)
        delete_vlan(auth, 30)
        auth.logout()

    def test_modify_dev_vlan(self):
        """
        test case for modify_vlans

        """
        auth = AOSSAuth(switch, username, password)
        modified = modify_vlan(auth, 30, "Test3")
        self.assertEqual(modified, 200)
        auth.logout()


class TestGetVLANPorts(TestCase):
    """
    Test Case for pyarubaaoss vlans create vlans function
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_vlan_ports(self):
        """
        test case for get_vlan_ports

        """
        #if skiptest is True:
         #   raise SkipTest
        auth = AOSSAuth(switch, username, password)
        vlan_ports = get_vlan_ports(auth)
        self.assertIs(type(vlan_ports), dict)
        auth.logout()