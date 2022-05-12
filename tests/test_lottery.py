# 0.019
from brownie import Lottery, accounts, network, config, exceptions
from web3 import Web3
import pytest

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    with pytest.raises(exceptions.VirtualMachineError):
        assert lottery.getEntranceFee() - Web3.toWei(0.019, "ether") < 0.01
