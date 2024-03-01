from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic

_T = TypeVar('_T')


class BaseRepository(ABC, Generic[_T]):
    """
        Abstract generic Repository
    """

    @abstractmethod
    def create_MCM(self, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    def validate_number(self) -> Sequence[_T]:
        raise NotImplementedError()
