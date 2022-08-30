import pytest

from defi.protocols.aave.contracts.LendingPool import AaveLendingPoolV2Contract

from head.consts.chains.const import Chains
from providers.abstracts.fabric import providerAbstractFabric


class TestAaveLendingPoolV2Contract:

    _address = '0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9'
    _provider = providerAbstractFabric.getFabric(fabricType='http').getProduct(chain=Chains.ETH)

    _instance = AaveLendingPoolV2Contract()\
        .setAddress(address=_address)\
        .setProvider(provider=_provider)\
        .create()

    def testInstance(self):
        assert isinstance(self._instance, AaveLendingPoolV2Contract)

    def testAddress(self):
        assert self._instance.address == self._address

    def testProvider(self):
        assert self._instance.provider == self._provider

    def test_FLASHLOAN_PREMIUM_TOTAL(self):
        assert isinstance(self._instance.FLASHLOAN_PREMIUM_TOTAL(), int)

    def test_LENDINGPOOL_REVISION(self):
        assert isinstance(self._instance.LENDINGPOOL_REVISION(), int)

    def test_MAX_NUMBER_RESERVES(self):
        assert isinstance(self._instance.MAX_NUMBER_RESERVES(), int)

    def test_MAX_STABLE_RATE_BORROW_SIZE_PERCENT(self):
        assert isinstance(self._instance.MAX_STABLE_RATE_BORROW_SIZE_PERCENT(), int)

    def test_getAddressesProvider(self):
        assert isinstance(self._instance.getAddressesProvider(), str)

    def test_getConfiguration(self):
        _asset = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # USDT
        assert isinstance(self._instance.getConfiguration(asset=_asset), tuple)

    def test_getReserveData(self):
        _asset = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # USDT
        assert isinstance(self._instance.getReserveData(asset=_asset), tuple)

    def test_getReserveNormalizedIncome(self):
        _asset = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # USDT
        assert isinstance(self._instance.getReserveNormalizedIncome(asset=_asset), int)

    def test_getReserveNormalizedVariableDebt(self):
        _asset = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # USDT
        assert isinstance(self._instance.getReserveNormalizedVariableDebt(asset=_asset), int)

    def test_getReservesList(self):
        assert isinstance(self._instance.getReservesList(), list)

    def test_getUserAccountData(self):
        _address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # USDT
        assert isinstance(self._instance.getUserAccountData(address=_address), list)

    def test_getUserConfiguration(self):
        _address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'  # USDT
        assert isinstance(self._instance.getUserConfiguration(address=_address), tuple)

    def test_paused(self):
        assert isinstance(self._instance.paused(), bool)


