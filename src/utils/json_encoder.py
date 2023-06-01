import json
from typing import Any
from uuid import UUID
from datetime import datetime
from enum import Enum
from inspect import isclass


class Encoder(json.JSONEncoder):
    def default(self, o: Any):
        if isinstance(o, UUID):
            return str(o)
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, Enum):
            return o.value
        if isclass(o):
            return o.__name__
        if o.__class__ is not None:
            return o.__dict__
        return super().default(o)
