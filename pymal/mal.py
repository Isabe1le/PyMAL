from typing import (
    Optional
)
class Session:
    """This class is used to interact with the MyAnimeList API.

    The following can be passed to the :class:`Session`

    Parameters
    -----------
    
    """

    def __init__(self, client_id: str, **kwargs):
        self._client_id = client_id