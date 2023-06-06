import ape
import pytest

@pytest.mark.parametrize("network", [ape.networks[network] for network in ape.networks])
def test_revert(project, accounts, network):
    with network.local.use_provider("test"):
        c = project.Example.deploy(sender=accounts[0])
        with ape.reverts():
            c.increment(sender=accounts[0])

@pytest.mark.parametrize("network", [ape.networks[network] for network in ape.networks])
def test_revert_sol(project, accounts, network):
    print(network)
    with network.local.use_provider("test"):
        c = project.HasError.deploy(sender=accounts[0])
        with ape.reverts():
            c.withdraw(sender=accounts[1])
