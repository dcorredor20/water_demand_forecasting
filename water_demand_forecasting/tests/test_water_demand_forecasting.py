#!/usr/bin/env python

"""Tests for `water_demand_forecasting` package."""


import unittest
from click.testing import CliRunner

from water_demand_forecasting import water_demand_forecasting
from water_demand_forecasting import cli


class TestWater_demand_forecasting(unittest.TestCase):
    """Tests for `water_demand_forecasting` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'water_demand_forecasting.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
