class Player:
    """Represents a player with a name and an id

    Attributes
    ----------
    uid
        The uid of the player
    name
        the name of the player
    """

    _uid: str
    _name: str

    def __init__(self, uid: str, name: str):
        """
        Parameters
        ----------
        uid
            The uid of the player
        name : str
            The name of the player
        """
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.uid}, {self.name})"
