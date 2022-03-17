from abc import abstractmethod
from typing import Generic, Protocol, TypeVar

from torch.utils.data import Dataset

T = TypeVar("T")
"T is a invariant type."

K = TypeVar("K", contravariant=True)
"K is a contravariant type."

V = TypeVar("V", covariant=True)
"V is a covariant type."


class Indexable(Protocol[K, V]):
    "Indexable type implements both `__len__` and `__getitem__`"

    @abstractmethod
    def __len__(self) -> int:
        "self.__len__() <==> len(self)"
        ...

    @abstractmethod
    def __getitem__(self, key: K) -> V:
        "self.__getitem__(key) <==> self[key]"

        ...


class DatasetWrapper(Dataset, Generic[T]):
    def __init__(self, seq: Indexable[int, T]) -> None:
        super().__init__()

        self._seq = seq

    def __len__(self) -> int:
        return len(self._seq)

    def __getitem__(self, key: int) -> T:
        return self._seq[key]

    @classmethod
    def wrap(cls, seq: Indexable[int, T]) -> Dataset[T]:
        return cls(seq)
