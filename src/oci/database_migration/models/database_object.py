# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseObject(object):
    """
    Note: Deprecated. Use the new resource model APIs instead.
    Database objects to exclude from migration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param owner:
            The value to assign to the owner property of this DatabaseObject.
        :type owner: str

        :param object_name:
            The value to assign to the object_name property of this DatabaseObject.
        :type object_name: str

        """
        self.swagger_types = {
            'owner': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'owner': 'owner',
            'object_name': 'objectName'
        }

        self._owner = None
        self._object_name = None

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this DatabaseObject.
        Owner of the object (regular expression is allowed)


        :return: The owner of this DatabaseObject.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DatabaseObject.
        Owner of the object (regular expression is allowed)


        :param owner: The owner of this DatabaseObject.
        :type: str
        """
        self._owner = owner

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this DatabaseObject.
        Name of the object (regular expression is allowed)


        :return: The object_name of this DatabaseObject.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this DatabaseObject.
        Name of the object (regular expression is allowed)


        :param object_name: The object_name of this DatabaseObject.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
