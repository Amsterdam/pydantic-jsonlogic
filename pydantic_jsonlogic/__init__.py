from typing import Any, Union

from pydantic import BaseModel, Field

Number = int | float


class Var(BaseModel):
    var: tuple[str] | str | tuple[str, Any] | Number | None | list[None]


class Merge(BaseModel):
    merge: Any


class Missing(BaseModel):
    missing: list[str] | str | Merge


class MissingSome(BaseModel):
    missing_some: tuple[int, list[str]]


class Equals(BaseModel):
    equals: tuple[Any, Any] = Field(alias="==")


class StrictEquals(BaseModel):
    strict_equals: tuple[Any, Any] = Field(alias="===")


class NotEquals(BaseModel):
    not_equals: tuple[Any, Any] = Field(alias="!=")


class StrictNotEquals(BaseModel):
    strict_not_equals: tuple[Any, Any] = Field(alias="!==")


class Not(BaseModel):
    not_: tuple[bool | Number | str] | bool | Number | str | tuple[list[None]] = Field(
        alias="!"
    )


class NotNot(BaseModel):
    not_not: tuple[Number | str | list[None] | bool] | Number | str | bool = Field(
        alias="!!"
    )


class GreaterThan(BaseModel):
    greater_than: tuple[Number | str | Var, Number | str] = Field(alias=">")


class GreaterThanOrEqual(BaseModel):
    greater_than_or_equal: tuple[Number | str | Var, Number | str] = Field(alias=">=")


class LessThan(BaseModel):
    less_than: (
        tuple[Number | str | Var, Number | str] | tuple[Number, Number, Number]
    ) = Field(alias="<")


class LessThanOrEqual(BaseModel):
    less_than_or_equal: (
        tuple[Number | str, Number | str] | tuple[Number, Number, Number]
    ) = Field(alias="<=")


class Max(BaseModel):
    max: list[Number]


class Min(BaseModel):
    min: list[Number]


class Add(BaseModel):
    add: list[Number | str | Var] = Field(alias="+")


class Subtract(BaseModel):
    subtract: tuple[Number | str] | tuple[Number | str, Number | str] = Field(alias="-")


class Multiply(BaseModel):
    multiply: list[Number | str | Var] = Field(alias="*")


class Divide(BaseModel):
    divide: tuple[Number | str, Number | str] = Field(alias="/")


class Modulo(BaseModel):
    modulo: tuple[Number | str | Var, Number | str] = Field(alias="%")


class In(BaseModel):
    in_: tuple[Union[int, str, "JSONLogic"], list[int | str] | str] = Field(alias="in")


class Cat(BaseModel):
    cat: Number | str | bool | list[Number | str | bool]


class Substr(BaseModel):
    substr: tuple[str, int] | tuple[str, int, int]


class Log(BaseModel):
    log: Number | str | bool | list[Number | str | bool]


class Or(BaseModel):
    or_: list[Union[bool, Number, str, list[None], "JSONLogic"]] = Field(alias="or")


class And(BaseModel):
    and_: list[Union[bool, Number, str, list[None], "JSONLogic"]] = Field(alias="and")


class If(BaseModel):
    if_: list[Any] = Field(alias="if")


class Filter(BaseModel):
    filter: tuple[
        # An array or an operation that produces an array
        Union[list[Any], Var, Missing, MissingSome, If, Merge, "Filter", "Map"],
        # Something that produces a truthy or falsy result
        Union[bool, "JSONLogic"],
    ]


class Map(BaseModel):
    map: tuple[
        # An array or an operation that produces an array
        Union[list[Any], Var, Missing, MissingSome, If, Merge, Filter, "Map"],
        # The operation to be performed on each element of the array
        "JSONLogic",
    ]


class Reduce(BaseModel):
    reduce: tuple[
        # An array or an operation that produces an array
        list[Any] | Var | Missing | MissingSome | If | Merge | Filter | Map,
        # The operation to be performed for each element of the array
        "JSONLogic",
        # The initial accumulator value
        Any,
    ]


class All(BaseModel):
    all: tuple[
        # An array or an operation that produces an array
        list[Any] | Var | Missing | MissingSome | If | Merge | Filter | Map,
        # Something that produces a truthy or falsy result
        Union[bool, "JSONLogic"],
    ]


class None_(BaseModel):
    none: tuple[
        # An array or an operation that produces an array
        list[Any] | Var | Missing | MissingSome | If | Merge | Filter | Map,
        # Something that produces a truthy or falsy result
        Union[bool, "JSONLogic"],
    ]


class Some(BaseModel):
    some: tuple[
        # An array or an operation that produces an array
        list[Any] | Var | Missing | MissingSome | If | Merge | Filter | Map,
        # Something that produces a truthy or falsy result
        Union[bool, "JSONLogic"],
    ]


JSONLogic = (
    Add
    | All
    | And
    | Cat
    | Divide
    | Equals
    | Filter
    | GreaterThan
    | GreaterThanOrEqual
    | If
    | In
    | LessThan
    | LessThanOrEqual
    | Log
    | Map
    | Max
    | Merge
    | Min
    | Max
    | Missing
    | MissingSome
    | Modulo
    | Multiply
    | None_
    | Not
    | NotEquals
    | NotNot
    | Or
    | Reduce
    | Some
    | StrictEquals
    | StrictNotEquals
    | Substr
    | Subtract
    | Var
)
