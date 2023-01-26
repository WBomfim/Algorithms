import pytest
from challenges.challenge_encrypt_message import encrypt_message


KEY_INDEX_INVALID = [
    ("verification", -2, "noitacifirev"), ("verification", 15, "noitacifirev"),
]

KEY_ODD_NUMBER = [
    ("verification", 3, "rev_noitacifi"), ("verification", 5, "firev_noitaci"),
]

KEY_EVEN_NUMBER = [
    ("verification", 4, "noitacif_irev"), ("verification", 6, "noitac_ifirev"),
]

KEY_INVALID_TYPE = [
    (123, 4), ("verification", "4"), (None, 4), ("verification", None)
]


def test_encrypt_message():
    for message, key, encrypt in KEY_INDEX_INVALID:
        assert encrypt_message(message, key) == encrypt

    for message, key, encrypt in KEY_ODD_NUMBER:
        assert encrypt_message(message, key) == encrypt

    for message, key, encrypt in KEY_EVEN_NUMBER:
        assert encrypt_message(message, key) == encrypt

    for message, key in KEY_INVALID_TYPE:
        with pytest.raises(TypeError):
            encrypt_message(message, key)
