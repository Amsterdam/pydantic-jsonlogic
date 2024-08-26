import pytest

from pydantic_jsonlogic import Missing, Var


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
