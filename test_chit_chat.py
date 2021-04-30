from unittest.mock import Mock, create_autospec

import pytest

import chit_chat
import chit_chat_2
import chit_chat_3


def test_simple_chat_returns_a_joke_when_rain(monkeypatch):
    monkeypatch.setattr(
        chit_chat, "BackyardLab", create_autospec(chit_chat.BackyardLab)
    )
    monkeypatch.setattr(
        chit_chat, "DopplerRadar", create_autospec(chit_chat.DopplerRadar)
    )
    monkeypatch.setattr(
        chit_chat, "RadiationSoilTester", create_autospec(chit_chat.RadiationSoilTester)
    )
    monkeypatch.setattr(
        chit_chat,
        "FancyWeatherAlgorithm",
        create_autospec(chit_chat.FancyWeatherAlgorithm),
    )

    response = chit_chat.simple_chat()

    assert "poncho" in response


def test_simple_chat_returns_a_joke_when_mocked(monkeypatch):
    person = create_autospec(
        chit_chat.Person,
        instance=True,
        # keyword arguments passed to the __init__
        name="Charlie",
        age=42,
        hobbies=["testing code"],
    )
    person.get_chit_chat.return_value = "weather"
    person.poncho_villa_joke.return_value = "poncho"
    Person = create_autospec(chit_chat.Person, return_value=person)
    monkeypatch.setattr(chit_chat, "Person", Person)

    acquaintance = create_autospec(
        chit_chat.Acquaintance,
        instance=True,
        # arguments to the __init__
        name="Some shmo",
        age=57,
        hobbies=["amateur meterology"],
        username="shmo_town",
        password="2secret4uhaxx",
    )
    acquaintance.respond.return_value = "rain"
    Acquaintance = create_autospec(chit_chat.Acquaintance, return_value=acquaintance)
    monkeypatch.setattr(chit_chat, "Acquaintance", Acquaintance)

    monkeypatch.setattr(
        chit_chat, "BackyardLab", create_autospec(chit_chat.BackyardLab)
    )
    monkeypatch.setattr(
        chit_chat, "DopplerRadar", create_autospec(chit_chat.DopplerRadar)
    )
    monkeypatch.setattr(
        chit_chat, "RadiationSoilTester", create_autospec(chit_chat.RadiationSoilTester)
    )
    monkeypatch.setattr(
        chit_chat,
        "FancyWeatherAlgorithm",
        create_autospec(chit_chat.FancyWeatherAlgorithm),
    )

    response = chit_chat.simple_chat()

    assert "poncho" in response


def test_simple_chat_returns_anecdote_when_sunny(monkeypatch):
    monkeypatch.setattr(
        chit_chat, "BackyardLab", create_autospec(chit_chat.BackyardLab)
    )
    monkeypatch.setattr(
        chit_chat, "DopplerRadar", create_autospec(chit_chat.DopplerRadar)
    )
    monkeypatch.setattr(
        chit_chat, "RadiationSoilTester", create_autospec(chit_chat.RadiationSoilTester)
    )
    # Algo = create_autospec(chit_chat.FancyWeatherAlgorithm)
    # Algo.return_value.assess_possible_weather.return_value = "sunny"
    algo = Mock()
    algo.assess_possible_weather.return_value = "sunny"
    Algo = Mock(return_value=algo)
    monkeypatch.setattr(chit_chat, "FancyWeatherAlgorithm", Algo)

    response = chit_chat.simple_chat()

    assert "sportsball" in response


def test_simple_chat_2_returns_a_joke_when_rain():
    person = chit_chat_2.Person(name="Chris", age=38, hobbies=["unit testing"])
    acquaintance = create_autospec(
        chit_chat_2.Acquaintance,
        instance=True,
        # arguments to the __init__
        name="Some shmo",
        age=57,
        hobbies=["amateur meterology"],
        username="shmo_town",
        password="2secret4uhaxx",
    )
    acquaintance.respond.return_value = "rain"

    response = chit_chat_2.simple_chat(person, acquaintance)

    assert "poncho" in response


def test_simple_chat_2_returns_anecdote_when_sunny():
    person = chit_chat_2.Person(name="Chris", age=38, hobbies=["unit testing"])
    acquaintance = create_autospec(
        chit_chat_2.Acquaintance,
        instance=True,
        # arguments to the __init__
        name="Some shmo",
        age=57,
        hobbies=["amateur meterology"],
        username="shmo_town",
        password="2secret4uhaxx",
    )
    acquaintance.respond.return_value = "sunny"

    response = chit_chat_2.simple_chat(person, acquaintance)

    assert "sportsball" in response


def test_simple_chat_2_raises_error_for_creepos():
    person = chit_chat_2.Person(name="Chris", age=38, hobbies=["unit testing"])
    acquaintance = create_autospec(
        chit_chat_2.Acquaintance,
        instance=True,
        # arguments to the __init__
        name="Some shmo",
        age=57,
        hobbies=["amateur meterology"],
        username="shmo_town",
        password="2secret4uhaxx",
    )

    with pytest.raises(chit_chat_2.BackAwaySlowly) as err:
        chit_chat_2.simple_chat(person, acquaintance)

    assert "I need an adult" in str(err)


def test_simple_chat_3_responds():
    person = chit_chat_3.Person(name="Chris", age=38, hobbies=["unit testing"])
    person.respond = create_autospec(person.respond)
    acquaintance = create_autospec(
        chit_chat_3.Acquaintance,
        instance=True,
        # arguments to the __init__
        name="Some shmo",
        age=57,
        hobbies=["amateur meterology"],
        username="shmo_town",
        password="2secret4uhaxx",
    )
    acquaintance.respond.return_value = "whatevs"

    chit_chat_3.simple_chat(person, acquaintance)

    person.respond.assert_called_with("whatevs")
