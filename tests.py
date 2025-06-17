from fs_lib import test, run
import requests

# @test("Web app output", score=10)
# def test_web_app_output():
#     """
#     The web app should return "Hello World" on route "/"
#     """
#     assert requests.get("http://localhost:5000/").text == "Hello World"

@test("Output 2", score=10)
def test_output_2():
    """
    The program output should be "Hello Fox"
    """
    assert run("python3", "app/main.py") == "Hello Fox"

@test("Output", score=10)
def test_output():
    """
    The program output should be "Hello World"
    """
    assert run("python3", "app/main.py") == "Hello World"