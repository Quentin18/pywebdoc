from click.testing import CliRunner
from pywebdoc.cli import cli

runner = CliRunner()


def test_py():
    result = runner.invoke(cli, ['py', '--lang=fr'])
    assert result.exit_code == 0


def test_std():
    result = runner.invoke(cli, ['std', 'time'])
    assert result.exit_code == 0


def test_home():
    result = runner.invoke(cli, ['home', 'click'])
    assert result.exit_code == 0


def test_pypi():
    result = runner.invoke(cli, ['pypi', 'mailsendersu'])
    assert result.exit_code == 0
    result = runner.invoke(cli, ['pypi', 'mailsendersu', '--version=1.0.0'])
    assert result.exit_code == 0


def test_rtd():
    result = runner.invoke(cli, ['rtd', 'affapy'])
    assert result.exit_code == 0


def test_list_std():
    result = runner.invoke(cli, ['list-std', '--version=3', '--lang=fr'])
    assert result.exit_code == 0
