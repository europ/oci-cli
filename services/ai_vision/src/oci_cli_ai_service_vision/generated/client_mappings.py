# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.ai_vision import AIServiceVisionClient

MODULE_TO_TYPE_MAPPINGS["ai_vision"] = oci.ai_vision.models.ai_vision_type_mapping
if CLIENT_MAP.get("ai_vision") is None:
    CLIENT_MAP["ai_vision"] = {}
CLIENT_MAP["ai_vision"]["ai_service_vision"] = AIServiceVisionClient
