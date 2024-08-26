from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator


class Var(BaseModel):
    model_config = ConfigDict(strict=True)

    var: tuple[str] | str | tuple[str, Any] | int | None | list[None]
