class Player:
    _id: str
    _name: str

    def __init__(self, id: str, name: str):
        self._id = id
        self._name = name

    @property
    def uid(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.uid}, {self.name})"


if __name__ == '__main__':
    p = Player('a123', 'Casey')
    print(p)
