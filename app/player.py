class Player:
    _uid: str
    _name: str

    def __init__(self, uid: str, name: str):
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
