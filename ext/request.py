from typing import *
from requests import request, get; from requests.exceptions import HTTPError, InvalidURL
from errors.base_errors import InvalidData, HTTPException, ServerError

def _completion_test() -> None:

    

    """
    Function that test OpenAI functionality.

    Attributes
    ------------
    > None
    """

    for url in ['https://api.github.com/', 'https://discord.com/api']:
        try:
            response = get(url)

            response.raise_for_status()
        
        except HTTPError as h:
            raise HTTPException(response, None) # error: ignore # type: ignore

        except Exception as e:
            raise InvalidURL("Invalid URL '{}': Did you mean 'http://{}' indeed?".format(url, url))

        else:
            print('Success!')

_completion_test()