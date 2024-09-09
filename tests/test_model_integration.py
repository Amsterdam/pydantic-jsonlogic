from pydantic import BaseModel

from pydantic_jsonlogic import All, JSONLogic


class SomeModel(BaseModel):
    json_logic: JSONLogic


def test_model_integration() -> None:
    json = '{"json_logic":{"all":[{"var":"integers"},{">=":[{"var":""},1]}]}}'
    model = SomeModel.model_validate_json(json)
    assert isinstance(model.json_logic, All)
    assert model.model_dump_json(by_alias=True) == json
