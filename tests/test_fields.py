import pytest

from pydantic_jsonlogic import (
    Add,
    All,
    And,
    Cat,
    Divide,
    Equals,
    Filter,
    GreaterThan,
    GreaterThanOrEqual,
    If,
    In,
    Length,
    LessThan,
    LessThanOrEqual,
    Log,
    Map,
    Max,
    Merge,
    Min,
    Missing,
    MissingSome,
    Modulo,
    Multiply,
    None_,
    Not,
    NotEquals,
    NotNot,
    Or,
    Reduce,
    Some,
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
        '{"var":["a",1]}',
        '{"var":1}',
        '{"var":null}',
        '{"var":[]}',
        '{"var":1.45}',
    ],
)
def test_var(json: str) -> None:
    model = Var.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"missing":[]}',
        '{"missing":["a"]}',
        '{"missing":"a"}',
        '{"missing":["a","b"]}',
        '{"missing":{"merge":["vin",{"if":[{"var":"financing"},["apr"],[]]}]}}',
    ],
)
def test_missing(json: str) -> None:
    model = Missing.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"missing_some":[1,["a","b"]]}',
        '{"missing_some":[2,["a","b","c"]]}',
    ],
)
def test_missing_some(json: str) -> None:
    model = MissingSome.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"==":[1,1]}',
        '{"==":[1,"1"]}',
        '{"==":[1,2]}',
    ],
)
def test_equals(json: str) -> None:
    model = Equals.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


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
    model = StrictEquals.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"!=":[1,2]}',
        '{"!=":[1,1]}',
        '{"!=":[1,"1"]}',
    ],
)
def test_not_equals(json: str) -> None:
    model = NotEquals.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"!==":[1,2]}',
        '{"!==":[1,1]}',
        '{"!==":[1,"1"]}',
    ],
)
def test_strict_not_equals(json: str) -> None:
    model = StrictNotEquals.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"!":[false]}',
        '{"!":false}',
        '{"!":[true]}',
        '{"!":true}',
        '{"!":0}',
        '{"!":1}',
        '{"!":[[]]}',
        '{"!":[0]}',
        '{"!":[""]}',
        '{"!":["0"]}',
        '{"!":[0.01]}',
        '{"!":0.01}',
    ],
)
def test_not(json: str) -> None:
    model = Not.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"!!":[[]]}',
        '{"!!":[0]}',
        '{"!!":[false]}',
        '{"!!":[""]}',
        '{"!!":["0"]}',
        '{"!!":[[]]}',
        '{"!!":[""]}',
        '{"!!":["0"]}',
        '{"!!":[0.01]}',
        '{"!!":0.01}',
        '{"!!":false}',
        '{"!!":"a"}',
    ],
)
def test_not_not(json: str) -> None:
    model = NotNot.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{">":[2,1]}',
        '{">":[1,1]}',
        '{">":[1,2]}',
        '{">":["2",1]}',
        '{">":[1.3,2]}',
        '{">":[1,2.3]}',
        '{">":[1.3,2.3]}',
    ],
)
def test_greater_than(json: str) -> None:
    model = GreaterThan.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{">=":[2,1]}',
        '{">=":[1,1]}',
        '{">=":[1,2]}',
        '{">=":["2",1]}',
        '{">=":[1.3,2]}',
        '{">=":[1,2.3]}',
        '{">=":[1.3,2.3]}',
    ],
)
def test_greater_than_or_equals(json: str) -> None:
    model = GreaterThanOrEqual.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"<":[2,1]}',
        '{"<":[1,1]}',
        '{"<":[1,2]}',
        '{"<":["1",2]}',
        '{"<":[1,2,3]}',
        '{"<":[1.3,2]}',
        '{"<":[1,2.3]}',
        '{"<":[1.3,2.3]}',
    ],
)
def test_less_than(json: str) -> None:
    model = LessThan.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"<=":[2,1]}',
        '{"<=":[1,1]}',
        '{"<=":[1,2]}',
        '{"<=":["1",2]}',
        '{"<=":[1,4,3]}',
        '{"<=":[1.3,2]}',
        '{"<=":[1,2.3]}',
        '{"<=":[1.3,2.3]}',
    ],
)
def test_less_than_or_equal(json: str) -> None:
    model = LessThanOrEqual.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"max":[1,2,3]}',
        '{"max":[1]}',
        '{"max":[1.34,2.568]}',
        '{"max":[1,2.568,5,2.54]}',
    ],
)
def test_max(json: str) -> None:
    model = Max.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"min":[1,2,3]}',
        '{"min":[1]}',
        '{"min":[1.34,2.568]}',
        '{"min":[1,2.568,5,2.54]}',
    ],
)
def test_min(json: str) -> None:
    model = Min.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"+":[1]}',
        '{"+":[1.1]}',
        '{"+":[1,2]}',
        '{"+":[1.1,2]}',
        '{"+":[1,2.1]}',
        '{"+":[1.1,2.1]}',
        '{"+":[2,2,2]}',
        '{"+":[2.1,2.2,2.3]}',
        '{"+":["1",1]}',
        '{"+":["1.1",1.1]}',
        '{"+":["1.1",1.1,5]}',
    ],
)
def test_add(json: str) -> None:
    model = Add.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"-":[2,3]}',
        '{"-":[1.1,2]}',
        '{"-":[1,2.1]}',
        '{"-":[1.1,2.1]}',
        '{"-":[3]}',
        '{"-":[3.33333]}',
        '{"-":["1",1]}',
        '{"-":["1",1.1]}',
        '{"-":["1.1",1.1]}',
    ],
)
def test_subtract(json: str) -> None:
    model = Subtract.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"*":[1]}',
        '{"*":[1.123]}',
        '{"*":[3,2]}',
        '{"*":[3.123,2]}',
        '{"*":[3,2.22224]}',
        '{"*":[3.122343,2.222]}',
        '{"*":[2,2,2]}',
        '{"*":["1",1]}',
        '{"*":[2.1,2,"2"]}',
    ],
)
def test_multiply(json: str) -> None:
    model = Multiply.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"/":[4,2]}',
        '{"/":[4.1,2]}',
        '{"/":[4,2.4]}',
        '{"/":[4.1,2.4]}',
        '{"/":["1",1]}',
        '{"/":["1.1",1]}',
        '{"/":["1",1.1]}',
        '{"/":["1.1",1.2]}',
    ],
)
def test_divide(json: str) -> None:
    model = Divide.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"%":[1,2]}',
        '{"%":[1.1,2]}',
        '{"%":[1,2.3]}',
        '{"%":[1.1,2.3]}',
        '{"%":["11",2]}',
        '{"%":[11,"2"]}',
        '{"%":["11","2"]}',
        '{"%":["1.1",2]}',
        '{"%":["1",2.3]}',
        '{"%":[1.1,"2"]}',
        '{"%":[1,"2.3"]}',
        '{"%":["1.1","2.3"]}',
    ],
)
def test_modulo(json: str) -> None:
    model = Modulo.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"in":["Bart",["Bart","Homer","Lisa","Marge","Maggie"]]}',
        '{"in":["i","team"]}',
        '{"in":[1,[2,3]]}',
        '{"in":[1,[1,2,3,"a","b"]]}',
        '{"in":[{"var":"filling"},["apple","cherry"]]}',
    ],
)
def test_in(json: str) -> None:
    model = In.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"cat":"ice"}',
        '{"cat":5}',
        '{"cat":5.79}',
        '{"cat":false}',
        '{"cat":true}',
        '{"cat":["ice"]}',
        '{"cat":["ice","cream"]}',
        '{"cat":[1,2]}',
        '{"cat":["Robocop",2]}',
        '{"cat":["we all scream for ","ice","cream"]}',
        '{"cat":["I love",false]}',
        '{"cat":["I love",5]}',
        '{"cat":["I love",5.97]}',
    ],
)
def test_cat(json: str) -> None:
    model = Cat.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"substr":["jsonlogic",4]}',
        '{"substr":["jsonlogic",-5]}',
        '{"substr":["jsonlogic",0,1]}',
        '{"substr":["jsonlogic",-1,1]}',
        '{"substr":["jsonlogic",4,5]}',
        '{"substr":["jsonlogic",-5,5]}',
        '{"substr":["jsonlogic",-5,-2]}',
        '{"substr":["jsonlogic",1,-5]}',
    ],
)
def test_substr(json: str) -> None:
    model = Substr.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"log":"hello"}',
        '{"log":["hello"]}',
        '{"log":1}',
        '{"log":false}',
        '{"log":1.1}',
        '{"log":[1]}',
        '{"log":[1.1]}',
        '{"log":[1.1,5]}',
        '{"log":[true]}',
    ],
)
def test_log(json: str) -> None:
    model = Log.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"merge":[]}',
        '{"merge":[[1]]}',
        '{"merge":[[1],[]]}',
        '{"merge":[[1],[2]]}',
        '{"merge":[[1],[2],[3]]}',
        '{"merge":[[1,2],[3]]}',
        '{"merge":[[1],[2,3]]}',
        '{"merge":1}',
        '{"merge":[1,2]}',
        '{"merge":[1,[2]]}',
    ],
)
def test_merge(json: str) -> None:
    model = Merge.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


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
        '{"or":[[],true]}',
        '{"or":[0,true]}',
        '{"or":["",true]}',
        '{"or":["0",true]}',
        '{"or":[0.12,true]}',
        '{"or":[false,0.12]}',
        '{"or":[-0.14,0.12]}',
        '{"or":[{">":[3,1]},true]}',
        '{"or":[{">":[3,1]},false]}',
        '{"or":[{">":[3,1]},{"!":true}]}',
        '{"or":[{">":[3,1]},{"<":[1,3]}]}',
        '{"or":[{"<":[{"var":"temp"},110]},{"==":[{"var":"pie.filling"},"apple"]}]}',
    ],
)
def test_or(json: str) -> None:
    model = Or.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


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
        '{"and":[[],true]}',
        '{"and":[0,true]}',
        '{"and":["",true]}',
        '{"and":["0",true]}',
        '{"and":[0.12,true]}',
        '{"and":[false,0.12]}',
        '{"and":[0.12,-5.16]}',
        '{"and":[{">":[3,1]},true]}',
        '{"and":[{">":[3,1]},false]}',
        '{"and":[{">":[3,1]},{"!":true}]}',
        '{"and":[{">":[3,1]},{"<":[1,3]}]}',
        '{"and":[{"<":[{"var":"temp"},110]},{"==":[{"var":"pie.filling"},"apple"]}]}',
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
        '{"if":[true,"apple"]}',
        '{"if":[false,"apple"]}',
        '{"if":[true,"apple","banana"]}',
        '{"if":[false,"apple","banana"]}',
        '{"if":[[],"apple","banana"]}',
        '{"if":[[1],"apple","banana"]}',
        '{"if":[[1,2,3,4],"apple","banana"]}',
        '{"if":["","apple","banana"]}',
        '{"if":["zucchini","apple","banana"]}',
        '{"if":["0","apple","banana"]}',
        '{"if":[0,"apple","banana"]}',
        '{"if":[1,"apple","banana"]}',
        '{"if":[3.1416,"apple","banana"]}',
        '{"if":[-1,"apple","banana"]}',
        '{"if":[true,"apple",true,"banana"]}',
        '{"if":[true,"apple",false,"banana"]}',
        '{"if":[false,"apple",true,"banana"]}',
        '{"if":[false,"apple",false,"banana"]}',
        '{"if":[true,"apple",true,"banana","carrot"]}',
        '{"if":[true,"apple",false,"banana","carrot"]}',
        '{"if":[false,"apple",true,"banana","carrot"]}',
        '{"if":[false,"apple",false,"banana","carrot"]}',
        '{"if":[false,"apple",false,"banana",false,"carrot"]}',
        '{"if":[false,"apple",false,"banana",false,"carrot","date"]}',
        '{"if":[false,"apple",false,"banana",true,"carrot","date"]}',
        '{"if":[false,"apple",true,"banana",false,"carrot","date"]}',
        '{"if":[false,"apple",true,"banana",true,"carrot","date"]}',
        '{"if":[true,"apple",false,"banana",false,"carrot","date"]}',
        '{"if":[true,"apple",false,"banana",true,"carrot","date"]}',
        '{"if":[true,"apple",true,"banana",false,"carrot","date"]}',
        '{"if":[true,"apple",true,"banana",true,"carrot","date"]}',
        '{"if":[{"+":"0"},"apple","banana"]}',
        '{"if":[{"+":"1"},"apple","banana"]}',
        '{"if":[{">":[2,1]},"apple","banana"]}',
        '{"if":[{">":[1,2]},"apple","banana"]}',
        '{"if":[true,{"cat":["ap","ple"]},{"cat":["ba","na","na"]}]}',
        '{"if":[false,{"cat":["ap","ple"]},{"cat":["ba","na","na"]}]}',
        '{"if":[{"missing":"a"},"missedit","foundit"]}',
        '{"if":[{"var":"x"},[{"var":"y"}],99]}',
        '{"if":[{"==":[{"%":[{"var":"i"},15]},0]},"fizzbuzz",{"==":[{"%":[{"var":"i"},3]},0]},"fizz",{"==":[{"%":[{"var":"i"},5]},0]},"buzz",{"var":"i"}]}',
    ],
)
def test_if(json: str) -> None:
    model = If.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"filter":[{"var":"integers"},true]}',
        '{"filter":[{"var":"integers"},false]}',
        '{"filter":[{"var":"integers"},{">=":[{"var":""},2]}]}',
        '{"filter":[{"var":"integers"},{"%":[{"var":""},2]}]}',
    ],
)
def test_filter(json: str) -> None:
    model = Filter.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"map":[{"var":"integers"},{"*":[{"var":""},2]}]}',
        '{"map":[{"var":"desserts"},{"var":"qty"}]}',
        '{"map":[{"var":"list"},{"if":[{"==":[{"%":[{"var":""},15]},0]},"fizzbuzz",{"==":[{"%":[{"var":""},3]},0]},"fizz",{"==":[{"%":[{"var":""},5]},0]},"buzz",{"var":""}]}]}',
    ],
)
def test_map(json: str) -> None:
    model = Map.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"reduce":[{"var":"integers"},{"+":[{"var":"current"},{"var":"accumulator"}]},0]}',
        '{"reduce":[{"var":"integers"},{"+":[{"var":"current"},{"var":"accumulator"}]},{"var":"start_with"}]}',
        '{"reduce":[{"var":"integers"},{"*":[{"var":"current"},{"var":"accumulator"}]},1]}',
    ],
)
def test_reduce(json: str) -> None:
    model = Reduce.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"all":[{"var":"integers"},{">=":[{"var":""},1]}]}',
        '{"all":[{"var":"integers"},{"==":[{"var":""},1]}]}',
        '{"all":[{"var":"integers"},{"<":[{"var":""},1]}]}',
        '{"all":[{"var":"items"},{">=":[{"var":"qty"},1]}]}',
        '{"all":[{"var":"items"},{">":[{"var":"qty"},1]}]}',
        '{"all":[{"var":"items"},{"<":[{"var":"qty"},1]}]}',
        '{"all":[{"var":"items"},{">=":[{"var":"qty"},1]}]}',
        '{"all":[[0,1,3],true]}',
    ],
)
def test_all(json: str) -> None:
    model = All.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"none":[{"var":"integers"},{">=":[{"var":""},1]}]}',
        '{"none":[{"var":"integers"},{"==":[{"var":""},1]}]}',
        '{"none":[{"var":"integers"},{"<":[{"var":""},1]}]}',
        '{"none":[{"var":"items"},{">=":[{"var":"qty"},1]}]}',
        '{"none":[{"var":"items"},{">":[{"var":"qty"},1]}]}',
        '{"none":[{"var":"items"},{"<":[{"var":"qty"},1]}]}',
        '{"none":[{"var":"items"},{">=":[{"var":"qty"},1]}]}',
        '{"none":[[0,1,3],true]}',
    ],
)
def test_none(json: str) -> None:
    model = None_.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"some":[{"var":"integers"},{">=":[{"var":""},1]}]}',
        '{"some":[{"var":"integers"},{"==":[{"var":""},1]}]}',
        '{"some":[{"var":"integers"},{"<":[{"var":""},1]}]}',
        '{"some":[{"var":"items"},{">=":[{"var":"qty"},1]}]}',
        '{"some":[{"var":"items"},{">":[{"var":"qty"},1]}]}',
        '{"some":[{"var":"items"},{"<":[{"var":"qty"},1]}]}',
        '{"some":[{"var":"items"},{">=":[{"var":"qty"},1]}]}',
        '{"some":[[0,1,3],true]}',
    ],
)
def test_some(json: str) -> None:
    model = Some.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)


@pytest.mark.parametrize(
    "json",
    [
        '{"length":"somevalue"}',
        '{"length":["somevalue"]}',
        '{"length":[{"var":"text"}]}',
    ],
)
def test_length(json: str) -> None:
    model = Length.model_validate_json(json)
    assert json == model.model_dump_json(by_alias=True)
