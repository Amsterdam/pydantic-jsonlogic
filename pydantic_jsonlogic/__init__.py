from typing import Any

from pydantic import BaseModel, Field


class Var(BaseModel):
    var: tuple[str] | str | tuple[str, Any] | int | None | list[None]


class Missing(BaseModel):
    missing: list[str] | str


class MissingSome(BaseModel):
    missing_some: tuple[int, list[str]]


class Equals(BaseModel):
    equals: tuple[Any, Any] = Field(validation_alias="==")


class StrictEquals(BaseModel):
    strict_equals: tuple[Any, Any] = Field(validation_alias="===")


class NotEquals(BaseModel):
    not_equals: tuple[Any, Any] = Field(validation_alias="!=")


class StrictNotEquals(BaseModel):
    strict_not_equals: tuple[Any, Any] = Field(validation_alias="!==")


class Not(BaseModel):
    not_: tuple[bool | int] | bool | int = Field(validation_alias="!")


class NotNot(BaseModel):
    not_not: tuple[int | str | list[None]] = Field(validation_alias="!!")


class GreaterThan(BaseModel):
    greater_than: tuple[int | str, int | str] = Field(validation_alias=">")


class GreaterThanOrEqual(BaseModel):
    greater_than_or_equal: tuple[int | str, int | str] = Field(validation_alias=">=")


class LessThan(BaseModel):
    less_than: tuple[int | str, int | str] | tuple[int, int, int] = Field(
        validation_alias="<"
    )


class LessThanOrEqual(BaseModel):
    less_than_or_equal: tuple[int | str, int | str] | tuple[int, int, int] = Field(
        validation_alias="<="
    )


class Max(BaseModel):
    max: list[int]


class Min(BaseModel):
    min: list[int]


class Add(BaseModel):
    add: list[int | str] = Field(validation_alias="+")


class Subtract(BaseModel):
    subtract: tuple[int | str] | tuple[int | str, int | str] = Field(
        validation_alias="-"
    )


class Multiply(BaseModel):
    multiply: list[int | str] = Field(validation_alias="*")


class Divide(BaseModel):
    divide: tuple[int | str, int | str] = Field(validation_alias="/")


class Modulo(BaseModel):
    modulo: tuple[int, int] = Field(validation_alias="%")


class In(BaseModel):
    in_: tuple[str, list[str] | str] = Field(validation_alias="in")


class Cat(BaseModel):
    cat: int | str | list[int | str]


class Substr(BaseModel):
    substr: tuple[str, int] | tuple[str, int, int]


class Log(BaseModel):
    log: int | str | bool | tuple[int | str | bool]


class Merge(BaseModel):
    merge: Any


class Or(BaseModel):
    or_: list[bool | int] = Field(validation_alias="or")


class And(BaseModel):
    and_: list[bool | int] = Field(validation_alias="and")


class If(BaseModel):
    if_: list[Any] = Field(validation_alias="if")
