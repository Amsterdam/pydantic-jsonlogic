from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Var(BaseModel):
    model_config = ConfigDict(strict=True)

    var: tuple[str] | str | tuple[str, Any] | int | None | list[None]


class Missing(BaseModel):
    model_config = ConfigDict(strict=True)

    missing: list[str] | str


class MissingSome(BaseModel):
    model_config = ConfigDict(strict=True)

    missing_some: tuple[int, list[str]]


class Equals(BaseModel):
    model_config = ConfigDict(strict=True)

    equals: tuple[Any, Any] = Field(validation_alias="==")


class StrictEquals(BaseModel):
    model_config = ConfigDict(strict=True)

    strict_equals: tuple[Any, Any] = Field(validation_alias="===")


class NotEquals(BaseModel):
    model_config = ConfigDict(strict=True)

    not_equals: tuple[Any, Any] = Field(validation_alias="!=")


class StrictNotEquals(BaseModel):
    model_config = ConfigDict(strict=True)

    strict_not_equals: tuple[Any, Any] = Field(validation_alias="!==")
