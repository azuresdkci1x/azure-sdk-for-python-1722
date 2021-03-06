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


class Recommendation(Model):
    """Represents a recommendation result generated by the recommendation engine.

    :param creation_time: Timestamp when this instance was created.
    :type creation_time: datetime
    :param recommendation_id: A GUID value that each recommendation object is
     associated with.
    :type recommendation_id: str
    :param resource_id: Full ARM resource ID string that this recommendation
     object is associated with.
    :type resource_id: str
    :param resource_scope: Name of a resource type this recommendation
     applies, e.g. Subscription, ServerFarm, Site. Possible values include:
     'ServerFarm', 'Subscription', 'WebSite'
    :type resource_scope: str or :class:`ResourceScopeType
     <azure.mgmt.web.models.ResourceScopeType>`
    :param rule_name: Unique name of the rule.
    :type rule_name: str
    :param display_name: UI friendly name of the rule (may not be unique).
    :type display_name: str
    :param message: Recommendation text.
    :type message: str
    :param level: Level indicating how critical this recommendation can
     impact. Possible values include: 'Critical', 'Warning', 'Information',
     'NonUrgentSuggestion'
    :type level: str or :class:`NotificationLevel
     <azure.mgmt.web.models.NotificationLevel>`
    :param channels: List of channels that this recommendation can apply.
     Possible values include: 'Notification', 'Api', 'Email', 'Webhook', 'All'
    :type channels: str or :class:`Channels <azure.mgmt.web.models.Channels>`
    :param tags: The list of category tags that this recommendation belongs
     to.
    :type tags: list of str
    :param action_name: Name of action recommended by this object.
    :type action_name: str
    :param start_time: The beginning time in UTC of a range that the
     recommendation refers to.
    :type start_time: datetime
    :param end_time: The end time in UTC of a range that the recommendation
     refers to.
    :type end_time: datetime
    :param next_notification_time: When to notify this recommendation next in
     UTC. Null means that this will never be notified anymore.
    :type next_notification_time: datetime
    :param notification_expiration_time: Date and time in UTC when this
     notification expires.
    :type notification_expiration_time: datetime
    :param notified_time: Last timestamp in UTC this instance was actually
     notified. Null means that this recommendation hasn't been notified yet.
    :type notified_time: datetime
    :param score: A metric value measured by the rule.
    :type score: float
    """

    _attribute_map = {
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'recommendation_id': {'key': 'recommendationId', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'resource_scope': {'key': 'resourceScope', 'type': 'str'},
        'rule_name': {'key': 'ruleName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'level': {'key': 'level', 'type': 'NotificationLevel'},
        'channels': {'key': 'channels', 'type': 'Channels'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'action_name': {'key': 'actionName', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'next_notification_time': {'key': 'nextNotificationTime', 'type': 'iso-8601'},
        'notification_expiration_time': {'key': 'notificationExpirationTime', 'type': 'iso-8601'},
        'notified_time': {'key': 'notifiedTime', 'type': 'iso-8601'},
        'score': {'key': 'score', 'type': 'float'},
    }

    def __init__(self, creation_time=None, recommendation_id=None, resource_id=None, resource_scope=None, rule_name=None, display_name=None, message=None, level=None, channels=None, tags=None, action_name=None, start_time=None, end_time=None, next_notification_time=None, notification_expiration_time=None, notified_time=None, score=None):
        self.creation_time = creation_time
        self.recommendation_id = recommendation_id
        self.resource_id = resource_id
        self.resource_scope = resource_scope
        self.rule_name = rule_name
        self.display_name = display_name
        self.message = message
        self.level = level
        self.channels = channels
        self.tags = tags
        self.action_name = action_name
        self.start_time = start_time
        self.end_time = end_time
        self.next_notification_time = next_notification_time
        self.notification_expiration_time = notification_expiration_time
        self.notified_time = notified_time
        self.score = score
