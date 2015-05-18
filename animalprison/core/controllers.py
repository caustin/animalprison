import json
from functools import partial
from animalprison.extensions import redis_store
from animalprison import serializers


def get_services() -> list:
    """

    :return:
    """
    return [
        json.loads(service.decode(encoding='utf-8')) for service in
        redis_store.lrange('services', 0, -1)
    ]


def find_service(key: str, value: str) -> dict:
    """

    :param key:
    :param value:
    :return:
    """
    for service in get_services():
        if service.get(key) == value:
            return service


get_service_by_id = partial(find_service, 'id')
get_service_by_id.__doc__ = "Find a service by it's id."

get_service_by_name = partial(find_service, 'name')
get_service_by_name.__doc__ = "Find a service buy it's name."


def get_service(service_id: str) -> list:
    """
    :param service_id:
    :return:
    """
    if not service_id:
        return get_services()
    else:
        return get_service_by_id(service_id)


def add_service(service_data: dict) -> dict:
    """
    :param service_data:
    :return:
    """
    service = serializers.Service().load(service_data)
    print(service)
    return {}
