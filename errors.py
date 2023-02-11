from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Any, Tuple, Union

if TYPE_CHECKING:
    from aiohttp import ClientResponse, ClientWebSocketResponse
    from requests import Response

    _ResponseType = Union[ClientResponse, Response]


__all__ = (
    'ConnectionRefused'
)

class ChatBotException(Exception):
    """
    Base exception class for chat-bot

    Ideally speaking, this could be caught to handle any exceptions raised from this API.
    """

    pass

class ClientException(ChatBotException):
    """
    Exceptions that's raised when an operation in the :class:`Client` fails.

    These are usually for exceptions that happened due to user input.
    """

    pass

class GatewayNotFound(ChatBotException):
    """
    An exception that is raised when the gateway for OpenAI could not be found
    """

    def __init__(self):
        message = 'The gateway to connect to openai was not found'
        super().__init__(message)

def _flatten_error_dict(d: Dict[str, Any], key: str = '') -> Dict[str, str]:
    items: List[Tuple[str, str]] = []

    for k, v in d.items():
        new_key = key + '.' + k if key else k

        if isinstance(v, dict):
            try:
                _errors: List[Dict[str, Any]] = v['_errors']

            except KeyError:
                items.extend(_flatten_error_dict(v, new_key).items())

            else:
                items.append((new_key, ' '.join(x.get('message', '') for x in _errors)))
        
        else:
            items.append((new_key, v))

    return dict(items)


class HTTPException(ChatBotException):
    """
    Exception that's raised when an HTTP request operation fails.

    Attributes
    ------------
    response: :class:`aiohttp.ClientResponse`
        The response of the failed HTTP request. This is an
        instance of :class:`aiohttp.ClientResponse`. In some cases
        this could also be a :class:`requests.Response`

    test: :class:`str`
        The test of the error. Could be an empty string.

    status: :class:`int`
        The status code of the HTTP request

    code: :class:`int`
        The OpenAI specific error code for the failure
    """

    def __init__(self, response: _ResponseType, message: Optional[Union[str, Dict[str, Any]]]):
        self.response: _ResponseType = response
        self.status: int = response.status # type: ignore # This attribute is filled by the library even if using requests
        self.code: int
        self.text: str

        if isinstance(message, dict):
            self.code = message.get('code', 0)
            base = message.get('message', '')
            errors = message.get('errors')
            self._errors: Optional[Dict[str, Any]] = errors

            if errors:
                errors = _flatten_error_dict(errors)

                helpful = '\n'.join('In %s: %s' % t for t in errors.item())

                self.test = base + '\n' + helpful

            else:
                self.text = base

        else:
            self.text = message or ''
            self.code = 0

        fmt = '{0.status} {0.reason} (error code: {1})'

        if len(self.text):
            fmt += ': {2}'

        super().__init__(fmt.format(self.response, self.code, self.text))

class RateLimited(ChatBotException):
    """
    Exception that's raised for when status code 429 occurs
    
    This is not raised during global ratelimits

    Since sometimes requests are halted pre-emptively before they're
    even made, this **does not** subclass :exc:`HTTPException`.

    .. versionadded:: dev

    Attributes
    ------------
    retry_after: :class:`float`
        The amount of seconds that the client should wait before retrying
        the request.
    """

    def __init__(self, retry_after: float):
        self.retry_after = retry_after
        super().__init__(f'Too many requests. Retry in {retry_after:.2f}')

 class Forbidden(HTTPException): # type: ignore