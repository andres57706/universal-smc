from functools import wraps

from searches.utils import ip_address


def fetch_request_ipaddress(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        ip = ip_address(request)
        setattr(request, 'ip_address', ip)
        return view(request, *args, **kwargs)

    return wrapper
