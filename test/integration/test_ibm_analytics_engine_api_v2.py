# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test the iaesdk service API operations
"""

import pytest
import unittest
import os
import json
import time
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from iaesdk import IbmAnalyticsEngineApiV2

# Read config file
configFile = 'ibmanalyticsengine-service.env'
configLoaded = None

if os.path.exists(configFile):
    os.environ['IBM_CREDENTIALS_FILE'] = configFile
    configLoaded = True
else:
    print('External configuration was not found, skipping tests...')

class TestIbmAnalyticsEngineApiV2(unittest.TestCase):
    def setUp(self):
        if not configLoaded:
            self.skipTest("External configuration not available, skipping...")

        self.iaesdk_service = IbmAnalyticsEngineApiV2.new_instance()
        self.instance_guid = os.getenv('IBM_ANALYTICS_ENGINE_INSTANCE_GUID')
        assert self.iaesdk_service is not None
        time.sleep(10)

    def tearDown(self):
        # Delete the resources
        print("Clean up complete.")

    def test_get_analytics_engine_by_id(self):
        status_code = self.iaesdk_service.get_analytics_engine_by_id(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_get_analytics_engine_state_by_id(self):
        status_code = self.iaesdk_service.get_analytics_engine_state_by_id(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_create_customization_request(self):
        # Construct a dict representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model =  {
            'source_type': 'http',
            'script_path': 'testString',
            'source_props': 'unknown type: object'
        }
        # Construct a dict representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model =  {
            'name': 'testString',
            'type': 'bootstrap',
            'script': analytics_engine_custom_action_script_model,
            'script_params': ['testString']
        }

        # Set up parameter values
        target = 'all'
        custom_actions = [analytics_engine_custom_action_model]

        # Invoke method
        status_code = self.iaesdk_service.create_customization_request(
            self.instance_guid,
            target,
            custom_actions,
        ).get_status_code()

        assert status_code == 200

    def test_get_all_customization_requests(self):
        status_code = self.iaesdk_service.get_all_customization_requests(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_get_customization_request_by_id(self):
        result = self.iaesdk_service.get_all_customization_requests(self.instance_guid).get_result()
        request_id = result[0]["id"]
        status_code = self.iaesdk_service.get_customization_request_by_id(self.instance_guid, request_id).get_status_code()
        assert status_code == 200

    def test_resize_cluster(self):
        compute_nodes_count = 1
        status_code = self.iaesdk_service.resize_cluster(self.instance_guid, compute_nodes_count).get_status_code()
        assert status_code == 200

    def test_reset_cluster_password(self):
        status_code = self.iaesdk_service.reset_cluster_password(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_configure_logging(self):

        # Construct a dict representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model =  {
            'node_type': 'management',
            'components': ['ambari-server']
        }
        # Construct a dict representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model =  {
            'type': 'logdna',
            'credential': 'testString',
            'api_host': 'testString',
            'log_host': 'testString',
            'owner': 'testString'
        }

        # Set up parameter values
        log_specs = [analytics_engine_logging_node_spec_model]
        log_server = analytics_engine_logging_server_model

        status_code = self.iaesdk_service.configure_logging(
            self.instance_guid,
            log_specs,
            log_server,
        ).get_status_code()

        assert status_code == 202

    def test_get_logging_config(self):
        status_code = self.iaesdk_service.get_logging_config(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_delete_logging_config(self):
        status_code = self.iaesdk_service.delete_logging_config(self.instance_guid).get_status_code()
        assert status_code == 202

    def test_update_private_endpoint_whitelist_all_params(self):

        # Set up parameter values
        ip_ranges = ['testString']
        action = 'add'

        # Invoke method
        response = self.iaesdk_service.update_private_endpoint_whitelist(
            self.instance_guid,
            ip_ranges,
            action,
            headers={}
        ).get_status_code()

        assert status_code == 200
