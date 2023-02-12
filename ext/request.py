from typing import *
from ext.errors.base_errors import InvalidData, HTTPException, ServerError

def _completion_test(data: Union[str, Dict[str, Any]]) -> None:

    return

    """
    Function that test OpenAI functionality.

    Attributes
    ------------
    data: :class:`Union[str, Dict[str,Any]]`
    """

    import openai

    openai.api_key = "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"

    try:
        completion = openai.Completion.create(engine = "text-davinci-003", prompt = data, max_tokens = 2048)

    except:
        raise HTTPException()