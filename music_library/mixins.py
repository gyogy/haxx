import json


class JsonParser():

    def to_json(self, indent=4):
        name = self.__class__.__name__
        attributes = self.__dict__

        return json.dumps({'type': name, 'dict': attributes}, default=lambda o: o.__dict__, indent=indent)

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)
