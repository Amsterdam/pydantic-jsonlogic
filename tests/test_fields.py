import pytest

from pydantic_jsonlogic import (
    Add,
    And,
    Cat,
    Divide,
    Equals,
    GreaterThan,
    GreaterThanOrEqual,
    If,
    In,
    LessThan,
    LessThanOrEqual,
    Log,
    Max,
    Merge,
    Min,
    Missing,
    MissingSome,
    Modulo,
    Multiply,
    Not,
    NotEquals,
    NotNot,
    Or,
    StrictEquals,
    StrictNotEquals,
    Substr,
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
        '{"===":[0,"0"]}',
        '{"===":[0,{"+":"0"}]}',
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
        '{"!" : [ [] ]}',
        '{"!" : [ 0 ]}',
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
        '{"!!" : [ [] ]}',
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


@pytest.mark.parametrize(
    "json",
    [
        '{"*":[1]}',
        '{"*":[3,2]}',
        '{"*":[2,2,2]}',
        '{"*":["1",1]}',
    ],
)
def test_multiply(json: str) -> None:
    Multiply.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"/":[4,2]}',
        '{"/":["1",1]}',
    ],
)
def test_divide(json: str) -> None:
    Divide.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"%":[1,2]}',
    ],
)
def test_modulo(json: str) -> None:
    Modulo.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"in":["Bart",["Bart","Homer","Lisa","Marge","Maggie"]]}',
        '{"in":["i","team"]}',
    ],
)
def test_in(json: str) -> None:
    In.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"cat":"ice"}',
        '{"cat":["ice"]}',
        '{"cat":["ice","cream"]}',
        '{"cat":[1,2]}',
        '{"cat":["Robocop",2]}',
        '{"cat":["we all scream for ","ice","cream"]}',
    ],
)
def test_cat(json: str) -> None:
    Cat.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"substr":["jsonlogic", 4]}',
        '{"substr":["jsonlogic", -5]}',
        '{"substr":["jsonlogic", 0, 1]}',
        '{"substr":["jsonlogic", -1, 1]}',
        '{"substr":["jsonlogic", 4, 5]}',
        '{"substr":["jsonlogic", -5, 5]}',
        '{"substr":["jsonlogic", -5, -2]}',
        '{"substr":["jsonlogic", 1, -5]}',
    ],
)
def test_substr(json: str) -> None:
    Substr.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"log": "hello"}',
        '{"log":["hello"]}',
        '{"log":1}',
        '{"log":false}',
        '{"log":[1]}',
        '{"log":[true]}',
    ],
)
def test_log(json: str) -> None:
    Log.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"merge":[]}',
        '{"merge":[[1]]}',
        '{"merge":[[1],[]]}',
        '{"merge":[[1], [2]]}',
        '{"merge":[[1], [2], [3]]}',
        '{"merge":[[1, 2], [3]]}',
        '{"merge":[[1], [2, 3]]}',
        '{"merge":1}',
        '{"merge":[1,2]}',
        '{"merge":[1,[2]]}',
    ],
)
def test_merge(json: str) -> None:
    Merge.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"or":[true,true]}',
        '{"or":[false,true]}',
        '{"or":[true,false]}',
        '{"or":[false,false]}',
        '{"or":[false,false,true]}',
        '{"or":[false,false,false]}',
        '{"or":[false]}',
        '{"or":[true]}',
        '{"or":[1,3]}',
        '{"or":[3,false]}',
        '{"or":[false,3]}',
        '{"or" : [ [], true ]}',
    ],
)
def test_or(json: str) -> None:
    Or.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"and":[true,true]}',
        '{"and":[false,true]}',
        '{"and":[true,false]}',
        '{"and":[false,false]}',
        '{"and":[true,true,true]}',
        '{"and":[true,true,false]}',
        '{"and":[false]}',
        '{"and":[true]}',
        '{"and":[1,3]}',
        '{"and":[3,false]}',
        '{"and":[false,3]}',
        '{"and" : [ [], true ]}',
        '{"and" : [ 0, true ]}',
    ],
)
def test_and(json: str) -> None:
    And.model_validate_json(json)


@pytest.mark.parametrize(
    "json",
    [
        '{"if":[]}',
        '{"if":[true]}',
        '{"if":[false]}',
        '{"if":["apple"]}',
        '{"if":[true, "apple"]}',
        '{"if":[false, "apple"]}',
        '{"if":[true, "apple", "banana"]}',
        '{"if":[false, "apple", "banana"]}',
        '{"if":[ [], "apple", "banana"]}',
        '{"if":[ [1], "apple", "banana"]}',
        '{"if":[ [1,2,3,4], "apple", "banana"]}',
        '{"if":[ "", "apple", "banana"]}',
        '{"if":[ "zucchini", "apple", "banana"]}',
        '{"if":[ "0", "apple", "banana"]}',
        '{"if":[ 0, "apple", "banana"]}',
        '{"if":[ 1, "apple", "banana"]}',
        '{"if":[ 3.1416, "apple", "banana"]}',
        '{"if":[ -1, "apple", "banana"]}',
        '{"if":[true, "apple", true, "banana"]}',
        '{"if":[true, "apple", false, "banana"]}',
        '{"if":[false, "apple", true, "banana"]}',
        '{"if":[false, "apple", false, "banana"]}',
        '{"if":[true, "apple", true, "banana", "carrot"]}',
        '{"if":[true, "apple", false, "banana", "carrot"]}',
        '{"if":[false, "apple", true, "banana", "carrot"]}',
        '{"if":[false, "apple", false, "banana", "carrot"]}',
        '{"if":[false, "apple", false, "banana", false, "carrot"]}',
        '{"if":[false, "apple", false, "banana", false, "carrot", "date"]}',
        '{"if":[false, "apple", false, "banana", true, "carrot", "date"]}',
        '{"if":[false, "apple", true, "banana", false, "carrot", "date"]}',
        '{"if":[false, "apple", true, "banana", true, "carrot", "date"]}',
        '{"if":[true, "apple", false, "banana", false, "carrot", "date"]}',
        '{"if":[true, "apple", false, "banana", true, "carrot", "date"]}',
        '{"if":[true, "apple", true, "banana", false, "carrot", "date"]}',
        '{"if":[true, "apple", true, "banana", true, "carrot", "date"]}',
        '{"if":[ {"+":"0"}, "apple", "banana"]}',
        '{"if":[ {"+":"1"}, "apple", "banana"]}',
    ],
)
def test_if(json: str) -> None:
    If.model_validate_json(json)
