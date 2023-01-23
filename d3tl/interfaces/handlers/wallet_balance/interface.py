from abc import abstractmethod, ABC
from typing import Any, Optional, Dict, final, overload

from trad3er.typings.trader.typing import Trad3r
from trad3er.interfaces.trader.interface import iTrad3r


class iWalletBalanceHandler(ABC):

    def __init__(self, trader: Trad3r, *args, **kwargs) -> None:
        self._trader = trader

        self.builder.build(
            key='trader', value=self.trader
        )

    @abstractmethod
    def get_overview(self, *args, **kwargs):
        raise NotImplementedError(
            f"{self.__class__.__name__} doesn't have an {self.get_overview.__name__}() implementation")

    @property
    def trader(self):
        return self._trader

    class Builder:

        def __init__(self) -> None:
            self._options: dict = dict()

        @overload
        def build(self, params: Dict[str, Any]) -> "iWalletBalanceHandler.Builder":
            ...

        @overload
        def build(self, key: str, value: Any) -> "iWalletBalanceHandler.Builder":
            ...

        @final
        def build(
                self,
                key: Optional[str] = None,
                value: Optional[str] = None,
                params: Optional[Dict[str, Any]] = None
        ) -> "iWalletBalanceHandler.Builder":

            def validate(k: str, v: Any) -> None:
                if k == 'trader':
                    if not isinstance(v, iTrad3r):
                        raise TypeError('Invalid Trader type')

            if isinstance(params, dict):
                for k, v in params.items():
                    validate(k=k, v=v)
                    self._options[k] = v
            elif isinstance(key, str):
                validate(k=key, v=value)
                self._options[key] = value
            return self

    @property
    def builder(self):
        return self.Builder()
