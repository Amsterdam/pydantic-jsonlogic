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


class Not(BaseModel):
    model_config = ConfigDict(strict=True)

    not_: tuple[bool | int] | bool | int = Field(validation_alias="!")


class NotNot(BaseModel):
    model_config = ConfigDict(strict=True)

    not_not: tuple[int | str | list[None]] = Field(validation_alias="!!")


class GreaterThan(BaseModel):
    model_config = ConfigDict(strict=True)

    greater_than: tuple[int | str, int | str] = Field(validation_alias=">")


class GreaterThanOrEqual(BaseModel):
    model_config = ConfigDict(strict=True)

    greater_than_or_equal: tuple[int | str, int | str] = Field(validation_alias=">=")


class LessThan(BaseModel):
    model_config = ConfigDict(strict=True)

    less_than: tuple[int | str, int | str] | tuple[int, int, int] = Field(
        validation_alias="<"
    )


class LessThanOrEqual(BaseModel):
    model_config = ConfigDict(strict=True)

    less_than_or_equal: tuple[int | str, int | str] | tuple[int, int, int] = Field(
        validation_alias="<="
    )


class Max(BaseModel):
    model_config = ConfigDict(strict=True)

    max: list[int]


class Min(BaseModel):
    model_config = ConfigDict(strict=True)

    min: list[int]


class Add(BaseModel):
    model_config = ConfigDict(strict=True)

    add: list[int | str] = Field(validation_alias="+")


class Subtract(BaseModel):
    model_config = ConfigDict(strict=True)

    subtract: tuple[int | str] | tuple[int | str, int | str] = Field(
        validation_alias="-"
    )


class Multiply(BaseModel):
    model_config = ConfigDict(strict=True)

    multiply: list[int | str] = Field(validation_alias="*")


class Divide(BaseModel):
    model_config = ConfigDict(strict=True)

    divide: tuple[int | str, int | str] = Field(validation_alias="/")


class Modulo(BaseModel):
    model_config = ConfigDict(strict=True)

    modulo: tuple[int, int] = Field(validation_alias="%")


class In(BaseModel):
    model_config = ConfigDict(strict=True)

    in_: tuple[str, list[str] | str] = Field(validation_alias="in")
