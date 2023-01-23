import unittest

import builtins
from datetime import datetime, timezone, timedelta

from d3tl.handlers.bids_and_asks.uniswap.handlers import UniSwapV2BidsAndAsksHandler, UniSwapV3BidsAndAsksHandler
from d3tl.abstract.fabric import d3Abstract
from d3tl.bridge.configurator import D3BridgeConfigurator
from trad3er.root.composite.trader import rootTrad3r

from raffaelo.providers.http.provider import HTTPProvider


class TestUniSwapV3BidsAndAsksHandler(unittest.TestCase):

    address = '0xA374094527e1673A86dE625aa59517c5dE346d32'

    scan_api_url = 'https://api.polygonscan.com/'
    scan_api_key = ''
    gas_symbol = 'MATIC'
    block_limit = 3000

    provider = HTTPProvider(uri='https://rpc.ankr.com/polygon')

    product = D3BridgeConfigurator(
        abstract=d3Abstract,
        fabric_name='bids_and_asks',
        handler_name='uniswapV3'
    ).produce_handler()
    handler = product(
        address=address,
        provider=provider,
        uri=scan_api_url,
        api_key=scan_api_key,
        block_limit=block_limit,
        gas_symbol=gas_symbol,
        trader=rootTrad3r
    )

    def testInstance(self):
        self.assertIsInstance(self.handler, UniSwapV3BidsAndAsksHandler)

    def testAddress(self):
        self.assertEqual(self.handler.contract.address, self.address)

    def testProvider(self):
        self.assertEqual(self.handler.provider, self.provider)

    def test_get_overview(self):
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(minutes=5)

        overview = self.handler.get_overview(
            start=start_time,
            end=end_time,
            is_reverse=False
        )
        builtins.print('\n', overview)
