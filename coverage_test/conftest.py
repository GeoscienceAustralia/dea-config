# isort: skip_file
# This file is part of datacube-ows, part of the Open Data Cube project.
# See https://opendatacube.org for more information.
#
# Copyright (c) 2017-2021 OWS Contributors
# SPDX-License-Identifier: Apache-2.0

import os

pytest_plugins = ["helpers_namespace"]
import pytest
from click.testing import CliRunner
from pytest_localserver.http import WSGIServer

from datacube_ows import ogc
from datacube_ows.ogc import app


@pytest.fixture
def runner():
    return CliRunner()

