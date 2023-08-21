import random
from argon2 import PasswordHasher


class Player:
    """Represents a player with a name and an id

    Intended to non-mutable; a dataclass would probably be better.

    Attributes
    ----------
    uid
        The uid of the player
    name
        the name of the player
    """

    _uid: str
    _name: str
    _password_salt: bytes
    _password_hash: str | None

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
        self._password_hash = None
        self._password_salt = b''.join([random.randbytes(1) for _ in range(8)])

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name

    def add_password(self, password: str) -> None:
        """Generates and stores a password hash with the given password

        Parameters
        ----------
        password
            the password to hash

        Raises
        ------
        RuntimeError
            if a password is already set
        """
        if self._password_hash is not None:
            raise RuntimeError("Password already set")

        hasher = PasswordHasher()
        self._password_hash = hasher.hash(password, salt=self._password_salt)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.uid}, {self.name})"
