import logging
from pytest import LogCaptureFixture
from logger import emit_warning


def test_emit_warning_logs_warning(caplog: LogCaptureFixture):
    # capture logs at WARNING level for the 'navi' logger
    with caplog.at_level(logging.WARNING, logger="navi"):
        emit_warning()

    print("caplog record tuples:", caplog.record_tuples)
    print("caplog text:", caplog.text)

    assert ("navi", logging.WARNING, "⚠️⚠️⚠️ OH-OH Warning ⚠️⚠️⚠️") in caplog.record_tuples
    assert "⚠️⚠️⚠️ OH-OH Warning ⚠️⚠️⚠️" in caplog.text
