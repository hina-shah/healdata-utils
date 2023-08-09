import pytest 
from pathlib import Path

@pytest.fixture(scope="module")
def heal_dd_from_redcap_dd_export_json():
    return Path("data/output/heal_dd_from_redcap_dd_export.json").read_text()

@pytest.fixture(scope="module")
def heal_dd_from_redcap_dd_export_csv():
    return Path("data/output/heal_dd_from_redcap_dd_export.csv").read_text()


@pytest.fixture(scope="module")
def heal_dd_from_spss_sav_json():
    return Path("data/output/heal_dd_from_spss_sav.json").read_text()

@pytest.fixture(scope="module")
def heal_dd_from_spss_sav_csv():
    return Path("data/output/heal_dd_from_spss_sav.csv").read_text()
    