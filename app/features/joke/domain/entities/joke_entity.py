import copy
from datetime import datetime
from typing import Any, Callable, TYPE_CHECKING

from app.core.error.invalid_operation_exception import InvalidOperationError

if TYPE_CHECKING:
    from app.features.joke.domain.entities.joke_command_model import JokeUpdateModel


class JokeEntity(object):
    """
        Task represents your collection of tasks as an entity
    """

    def __init__(
        self,
        id_: int | None,
        text: str,
        owner_id: int,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        is_deleted: bool | None = False,
    ):
        self.id_ = id_
        self.text = text
        self.owner_id = owner_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted

    def __eq__(self, other) -> bool:
        if isinstance(other, JokeEntity):
            return self.id_ == other.id_

        return False

    def update_entity(
        self,
        entity_update_model: 'JokeUpdateModel',
        get_update_data_fn: Callable[['JokeUpdateModel'], dict[str, Any]]
    ) -> 'JokeEntity':
        update_data = get_update_data_fn(entity_update_model)
        update_entity = copy.deepcopy(self)

        for attr_name, value in update_data.items():
            update_entity.__setattr__(attr_name, value)

        return update_entity

    def mark_entity_as_deleted(self) -> 'JokeEntity':
        if self.is_deleted:
            raise InvalidOperationError('Joke is already marked as deleted')

        marked_entity = copy.deepcopy(self)
        marked_entity.is_deleted = True

        return marked_entity
