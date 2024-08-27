import pytest

from pydantic_jsonlogic import (
    Add,
    Equals,
    GreaterThan,
    GreaterThanOrEqual,
    LessThan,
    LessThanOrEqual,
    Max,
    Min,
    Missing,
    MissingSome,
    Not,
    NotEquals,
    NotNot,
    StrictEquals,
    StrictNotEquals,
    Subtract,
    Var,
)


@pytest.mark.parametrize(
    "json",
    [
        '{"var":["a"]}',
        '{"var":"a"}',
        '{"var":["a", 1]}',
        '{"var":1}',
        '{"var":null}',
        '{"var":[]}',
    ],
)
def test_var(json: str) -> None:
    Var.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"missing":[]}',
        '{"missing":["a"]}',
        '{"missing":"a"}',
        '{"missing":["a","b"]}',
    ],
)
def test_missing(json: str) -> None:
    Missing.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"missing_some":[1, ["a", "b"]]}',
        '{"missing_some":[2, ["a", "b", "c"]]}',
    ],
)
def test_missing_some(json: str) -> None:
    MissingSome.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"==":[1,1]}',
        '{"==":[1,"1"]}',
        '{"==":[1,2]}',
    ],
)
def test_equals(json: str) -> None:
    Equals.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"===":[1,1]}',
        '{"===":[1,"1"]}',
        '{"===":[1,2]}',
    ],
)
def test_strict_equals(json: str) -> None:
    StrictEquals.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"!=":[1,2]}',
        '{"!=":[1,1]}',
        '{"!=":[1,"1"]}',
    ],
)
def test_not_equals(json: str) -> None:
    NotEquals.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"!==":[1,2]}',
        '{"!==":[1,1]}',
        '{"!==":[1,"1"]}',
    ],
)
def test_strict_not_equals(json: str) -> None:
    StrictNotEquals.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"!":[false]}',
        '{"!":false}',
        '{"!":[true]}',
        '{"!":true}',
        '{"!":0}',
        '{"!":1}',
    ],
)
def test_not(json: str) -> None:
    Not.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"!!" : [ [] ]}',
        '{"!!" : [ 0 ]}',
        '{"!!" : [ "" ]}',
        '{"!!" : [ "0" ]}',
    ],
)
def test_not_not(json: str) -> None:
    NotNot.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{">":[2,1]}',
        '{">":[1,1]}',
        '{">":[1,2]}',
        '{">":["2",1]}',
    ],
)
def test_greater_than(json: str) -> None:
    GreaterThan.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{">=":[2,1]}',
        '{">=":[1,1]}',
        '{">=":[1,2]}',
        '{">=":["2",1]}',
    ],
)
def test_greater_than_or_equals(json: str) -> None:
    GreaterThanOrEqual.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"<":[2,1]}',
        '{"<":[1,1]}',
        '{"<":[1,2]}',
        '{"<":["1",2]}',
        '{"<":[1,2,3]}',
    ],
)
def test_less_than(json: str) -> None:
    LessThan.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"<=":[2,1]}',
        '{"<=":[1,1]}',
        '{"<=":[1,2]}',
        '{"<=":["1",2]}',
        '{"<=":[1,4,3]}',
    ],
)
def test_less_than_or_equal(json: str) -> None:
    LessThanOrEqual.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"max":[1,2,3]}',
        '{"max":[1]}',
    ],
)
def test_max(json: str) -> None:
    Max.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"min":[1,2,3]}',
        '{"min":[1]}',
    ],
)
def test_min(json: str) -> None:
    Min.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"+":[1]}',
        '{"+":[1,2]}',
        '{"+":[2,2,2]}',
        '{"+":["1",1]}',
    ],
)
def test_add(json: str) -> None:
    Add.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"-":[2,3]}',
        '{"-":[3]}',
        '{"-":["1",1]}',
    ],
)
def test_subtract(json: str) -> None:
    Subtract.model_validate_json(json)
