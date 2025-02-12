# noqa: D100
from nox_poetry import session  # type: ignore


@session
def tests(session):  # noqa: D103,WPS442
    session.run_always("poetry", "install", external=True)
    session.run("pytest", "tests/unit", external=True)
