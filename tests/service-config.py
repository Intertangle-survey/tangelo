import nose
import requests

import fixture


@nose.with_setup(fixture.start_tangelo, fixture.stop_tangelo)
def test_service_config():
    result = requests.get(fixture.url("configured")).content

    assert result == "abracadabra"


@nose.with_setup(fixture.start_tangelo, fixture.stop_tangelo)
def test_config_protected():
    result = requests.get(fixture.url("configured.yaml"))

    assert result.status_code == 403


@nose.with_setup(fixture.start_tangelo, fixture.stop_tangelo)
def test_source_protected():
    result = requests.get(fixture.url("configured.py"))

    assert result.status_code == 403
