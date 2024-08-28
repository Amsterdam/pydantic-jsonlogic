from abc import ABCMeta
from typing import Any

from pydantic import BaseModel, Field


class BaseJSONLogicOperation(BaseModel, metaclass=ABCMeta): ...


class Var(BaseJSONLogicOperation):
    var: tuple[str] | str | tuple[str, Any] | int | None | list[None]


class Missing(BaseJSONLogicOperation):
    missing: list[str] | str


class MissingSome(BaseJSONLogicOperation):
    missing_some: tuple[int, list[str]]


class Equals(BaseJSONLogicOperation):
    equals: tuple[Any, Any] = Field(validation_alias="==")


class StrictEquals(BaseJSONLogicOperation):
    strict_equals: tuple[Any, Any] = Field(validation_alias="===")


class NotEquals(BaseJSONLogicOperation):
    not_equals: tuple[Any, Any] = Field(validation_alias="!=")


class StrictNotEquals(BaseJSONLogicOperation):
    strict_not_equals: tuple[Any, Any] = Field(validation_alias="!==")


class Not(BaseJSONLogicOperation):
    not_: tuple[bool | int | str] | bool | int | str | tuple[list[None]] = Field(
        validation_alias="!"
    )


class NotNot(BaseJSONLogicOperation):
    not_not: tuple[int | str | list[None]] = Field(validation_alias="!!")


class GreaterThan(BaseJSONLogicOperation):
    greater_than: tuple[int | str, int | str] = Field(validation_alias=">")


class GreaterThanOrEqual(BaseJSONLogicOperation):
    greater_than_or_equal: tuple[int | str, int | str] = Field(validation_alias=">=")


class LessThan(BaseJSONLogicOperation):
    less_than: tuple[int | str, int | str] | tuple[int, int, int] = Field(
        validation_alias="<"
    )


class LessThanOrEqual(BaseJSONLogicOperation):
    less_than_or_equal: tuple[int | str, int | str] | tuple[int, int, int] = Field(
        validation_alias="<="
    )


class Max(BaseJSONLogicOperation):
    max: list[int]


class Min(BaseJSONLogicOperation):
    min: list[int]


class Add(BaseJSONLogicOperation):
    add: list[int | str] = Field(validation_alias="+")


class Subtract(BaseJSONLogicOperation):
    subtract: tuple[int | str] | tuple[int | str, int | str] = Field(
        validation_alias="-"
    )


class Multiply(BaseJSONLogicOperation):
    multiply: list[int | str] = Field(validation_alias="*")


class Divide(BaseJSONLogicOperation):
    divide: tuple[int | str, int | str] = Field(validation_alias="/")


class Modulo(BaseJSONLogicOperation):
    modulo: tuple[int, int] = Field(validation_alias="%")


class In(BaseJSONLogicOperation):
    in_: tuple[int | str | BaseJSONLogicOperation, list[int | str] | str] = Field(
        validation_alias="in"
    )


class Cat(BaseJSONLogicOperation):
    cat: int | str | list[int | str]


class Substr(BaseJSONLogicOperation):
    substr: tuple[str, int] | tuple[str, int, int]


class Log(BaseJSONLogicOperation):
    log: int | str | bool | tuple[int | str | bool]


class Merge(BaseJSONLogicOperation):
    merge: Any


class Or(BaseJSONLogicOperation):
    or_: list[bool | int | str | list[None] | BaseJSONLogicOperation] = Field(
        validation_alias="or"
    )


class And(BaseJSONLogicOperation):
    and_: list[bool | int | str | list[None] | BaseJSONLogicOperation] = Field(
        validation_alias="and"
    )


class If(BaseJSONLogicOperation):
    if_: list[Any] = Field(validation_alias="if")
