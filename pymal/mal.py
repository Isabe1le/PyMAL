from typing import (
    Optional
)
class Session:
    """This class is used to interact with the MyAnimeList API.

    The following can be passed to the :class:`Session`

    Parameters
    -----------
    test_option: Optional[:class:`int`]
        Description of the test option. ``None`` - ``1234``

        .. somethinghere:: 1.2.3
            Something else goes here ``abcd``.
    
    non_optional_bool: :class:`bool`
        A test message here. :func:`.function_name`
        :attr:`.test_attr`
    """

    def __init__(self, **kwargs):
        self.temp = "Hello World"
    
    def function_name(self, var: str) -> None:
        """A testing function that will be removed later.

        Parameters
        -----------
        var: :class:`str`
            The response that comes after ``Hello``
        """
        print(f"Hello {var}")