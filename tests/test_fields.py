import pytest

from pydantic_jsonlogic import Var


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
