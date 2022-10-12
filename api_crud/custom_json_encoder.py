"""This is the CustomJSONEncoder."""
import json
from typing import Any


class CustomJSONEncoder(json.JSONEncoder):
    """ This class is in charge of serializing the images"""
    def default(self, o: Any) -> Any:  # pylint: disable=E0202
        """
        This method encodes the parameter it receives
        if it is an instance of bytes
        :param o:
        """
        if isinstance(o, bytes):
            return str(o, 'utf-8')
        return json.JSONEncoder.default(self, o)
