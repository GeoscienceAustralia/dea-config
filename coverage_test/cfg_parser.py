# This file is part of datacube-ows, part of the Open Data Cube project.
# See https://opendatacube.org for more information.
#
# Copyright (c) 2017-2021 OWS Contributors
# SPDX-License-Identifier: Apache-2.0
import os

import pytest

from datacube_ows.cfg_parser_impl import main

from ows_refactored.ows_root_cfg import ows_cfg

def test_cfg_parser_simple(runner):
    result = runner.invoke(main, [])
    assert result.exit_code == 0