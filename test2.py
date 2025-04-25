def triangle_field(a:int, h:int) -> float:
    print(0.5 * a * h)

def test_triangle_field(capsys):
    # given
    a = 5
    h = 10
    # when
    triangle_field(a, h)
    out, error = capsys.readouterr()

    # then
    assert out == '25.0\n', f"Expected 25 but got {out}"
