from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Dict, Generic, TypeVar

from aiogram import Bot

T = TypeVar("T")


class BaseHandlerMixin(Generic[T]):
    if TYPE_CHECKING:  # pragma: no cover
        event: T
        data: Dict[str, Any]


class BaseHandler(BaseHandlerMixin[T], ABC):
    """
    Base class for all class-based handlers
    """

    def __init__(self, event: T, **kwargs: Any) -> None:
        self.event: T = event
        self.data: Dict[str, Any] = kwargs

    @property
    def bot(self) -> Bot:
        if "bot" in self.data:
            return self.data["bot"]
        return Bot.get_current()

    @abstractmethod
    async def handle(self) -> Any:  # pragma: no cover
        pass

    def __await__(self):
        return self.handle().__await__()