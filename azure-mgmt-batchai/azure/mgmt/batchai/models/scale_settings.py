# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ScaleSettings(Model):
    """At least one of manual or autoScale settings must be specified. Only one of
    manual or autoScale settings can be specified. If autoScale settings are
    specified, the system automatically scales the cluster up and down (within
    the supplied limits) based on the pending jobs on the cluster.

    :param manual: The scale for the cluster by manual settings.
    :type manual: :class:`ManualScaleSettings
     <azure.mgmt.batchai.models.ManualScaleSettings>`
    :param auto_scale: The scale for the cluster by autoscale settings.
    :type auto_scale: :class:`AutoScaleSettings
     <azure.mgmt.batchai.models.AutoScaleSettings>`
    """

    _attribute_map = {
        'manual': {'key': 'manual', 'type': 'ManualScaleSettings'},
        'auto_scale': {'key': 'autoScale', 'type': 'AutoScaleSettings'},
    }

    def __init__(self, manual=None, auto_scale=None):
        self.manual = manual
        self.auto_scale = auto_scale
