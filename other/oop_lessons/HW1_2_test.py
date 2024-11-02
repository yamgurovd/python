import os

from _pytest import mark

from HW1_duble import Circle, Rectangle, Square, Romb, Triangle
import pytest
import datetime


# переделать негативные тесты with pytest.raises(ValueError)
# на каждый класс сделать по 5 тестов
# mark.parametrize + ids (посмотреть как передать id каждому параметру)
# добавить тест, который будет пропускаться
# добавить тест, который будет пропускаться если время у нас с 23:00 до 7:00 UTC


@pytest.mark.parametrize(("side_a", "side_b", "expected_result"),
                         [pytest.param(1, 2, 2, marks=pytest.mark.basic, id='Int value 1'),
                          pytest.param(0.000000001, 2, 2e-09, id='Float value'),
                          pytest.param(5, 2, 10, marks=pytest.mark.basic),
                          pytest.param(5, 3, 15, marks=pytest.mark.skip(reason='Special skip for one test'),
                                       id='Int value test for skip'),
                          pytest.param(3, 2, 11, marks=[pytest.mark.basic, pytest.mark.xfail],
                                       id='Example test for xfail')])
def test_rectangle_positive(side_a, side_b, expected_result):
    rectangle = Rectangle(side_a, side_b, "R")

    assert rectangle.get_area() == expected_result, "ФР результат != ОР результат"


@pytest.mark.skip(reason='Skip for special')
@pytest.mark.parametrize(("side_a", "side_b", "expected_result"),
                         [pytest.param(1, 2, 2, marks=pytest.mark.basic, id='Int value 1'),
                          pytest.param(0.000000001, 2, 2e-09, id='Float value'),
                          pytest.param(5, 2, 10, marks=pytest.mark.basic, id='Int value 2'),
                          pytest.param(5, 3, 15, marks=pytest.mark.skip, id='Int value test for skip'),
                          pytest.param(3, 2, 11, marks=[pytest.mark.basic, pytest.mark.xfail],
                                       id='Example test for xfail')])
def test_rectangle_positive_for_skip(side_a, side_b, expected_result):
    rectangle = Rectangle(side_a, side_b, "R")

    assert rectangle.get_area() == expected_result, "ФР результат != ОР результат"


start_time = datetime.datetime(2023, month=9, day=16, hour=23, minute=00, tzinfo=datetime.timezone.utc)
end_time = datetime.datetime(2023, month=9, day=17, hour=7, minute=00, tzinfo=datetime.timezone.utc)

offset = start_time - end_time


@pytest.mark.skipif(condition=offset, reason='Skip for special if there is condition')
@pytest.mark.parametrize(("side_a", "side_b", "expected_result"),
                         [pytest.param(1, 2, 2, marks=pytest.mark.basic, id='Int value 1'),
                          pytest.param(0.000000001, 2, 2e-09, id='Float value'),
                          pytest.param(5, 2, 10, marks=pytest.mark.basic, id='Int value 2'),
                          pytest.param(5, 3, 15, marks=pytest.mark.skip, id='Int value test for skip'),
                          pytest.param(3, 2, 11, marks=[pytest.mark.basic, pytest.mark.xfail],
                                       id='Example test for xfail')])
def test_rectangle_positive_for_skip(side_a, side_b, expected_result):
    rectangle = Rectangle(side_a, side_b, "R")

    assert rectangle.get_area() == expected_result, "ФР результат != ОР результат"


@pytest.mark.parametrize(("side_a", "side_b", "expected_result"),
                         [(1, 0, ValueError),
                          ("str", 5, TypeError),
                          (1, None, TypeError)],
                         ids=["Zero value", "String value", "Nonetype value"])
def test_rectangle_negative(side_a, side_b, expected_result):
    with pytest.raises(expected_result):
        rectangle = Rectangle(side_a, side_b, "R")


@pytest.mark.parametrize(("radius", "expected_result"),
                         [(1, 3.14),
                          (0.000000001, 3.1400000000000002e-18)],
                         ids=["Int value", "Float value"])
def test_circle_positive(radius, expected_result):
    circle = Circle(radius, "C")

    assert circle.get_area() == expected_result, "ФР результат != ОР результат"


@pytest.mark.parametrize(("radius", "expected_result"),
                         [(0, ValueError),
                          ("str", TypeError),
                          (None, TypeError)],
                         ids=["Zero value", "String value", "Nonetype value"])
def test_circle_negative(radius, expected_result):
    with pytest.raises(expected_result):
        circle = Circle(radius, "C")


@pytest.mark.parametrize(("side", "expected_result"),
                         [(1, 1),
                          (0.000000001, 1e-18)],
                         ids=["Int value", "Float value"])
def test_square_positive(side, expected_result):
    square = Square(side, "S")

    assert square.get_area() == expected_result, "ФР результат != ОР результат"


@pytest.mark.parametrize(("side", "expected_result"),
                         [(0, ValueError),
                          ("str", TypeError),
                          (None, TypeError)],
                         ids=["Zero value", "String value", "Nonetype value"])
def test_square_negative(side, expected_result):
    with pytest.raises(expected_result):
        square = Square(side, "S")


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "expected_result"),
                         [(1, 2, 3, 4, 12.0),
                          (0.000000001, 1, 2, 3, 3.0000000000000004e-09), ],
                         ids=["Int value", "Float value"])
def test_romb_positive(side_a, side_b, side_c, side_d, expected_result):
    romb = Romb(side_a, side_b, side_c, side_d, "Romb")

    assert romb.get_area() == expected_result, "ФР результат != ОР результат"


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "expected_result"),
                         [(0, 1, 2, 3, ValueError),
                          ("str", 0, 1, 2, TypeError),
                          (1, None, -7, 4, TypeError)],
                         ids=["Zero value", "String value", "Nonetype value"])
def test_romb_negative(side_a, side_b, side_c, side_d, expected_result):
    with pytest.raises(expected_result):
        romb = Romb(side_a, side_b, side_c, side_d, "Romb")


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "expected_result"),
                         [(1, 2, 3, 6),
                          (0.000000001, 1, 2, 3.000000001)],
                         ids=["Int value", "Float value"])
def test_triangle_positive(side_a, side_b, side_c, expected_result):
    triangle = Triangle(side_a, side_b, side_c, "Romb")

    assert triangle.get_area() == expected_result, "ФР результат != ОР результат"


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "expected_result"),
                         [(0, 1, 2, ValueError),
                          ("str", -5, 1, TypeError),
                          (1, None, -7, TypeError)],
                         ids=["Zero value", "String value", "Nonetype value"])
def test_triangle_negative(side_a, side_b, side_c, expected_result):
    with pytest.raises(expected_result):
        triangle = Triangle(side_a, side_b, side_c, "Romb")
