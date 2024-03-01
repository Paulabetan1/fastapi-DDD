import copy
from datetime import datetime
from typing import Any, Callable, TYPE_CHECKING

from app.core.error.invalid_operation_exception import InvalidOperationError

if TYPE_CHECKING:
    from app.features.page.domain.entities.page_command_model import PageUpdateModel


class PageEntity(object):
    """
     page represents your collection of pages as an entity
    """

    def __init__(
        self,
        id_: int | None,
        url: str,
        name: str,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
        tasks: list[int] = None
    ):
        self.id_ = id_
        self.url = url
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted
        self.tasks: list[int] = [] if tasks is None else tasks

    def update_entity(
        self,
        entity_update_model: 'PageUpdateModel',
        get_update_data_fn: Callable[['PageUpdateModel'], dict[str, Any]]
    ) -> 'PageEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def mark_entity_as_deleted(self) -> 'PageEntity':
        if self.is_deleted:
            raise InvalidOperationError('page is already marked as deleted')

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PageEntity):
            return self.id_ == other.id_

        return False

    def to_popo(self) -> object:
        return self.__dict__
