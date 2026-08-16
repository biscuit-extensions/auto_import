from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class AutoImport(Extension):
    """Automatically scan workspace symbols and generate missing import statements."""

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.symbol_index: dict[str, str] = {}
        self.api.logger.info("Auto Import extension initialised.")

    def register_symbol(self, symbol: str, module_path: str) -> None:
        self.symbol_index[symbol] = module_path

    def generate_import(self, symbol: str, language: str = "python") -> str | None:
        mod = self.symbol_index.get(symbol)
        if not mod:
            return None
        if language.lower() in ("python", "py"):
            return f"from {mod} import {symbol}"
        else:
            return f"import {{ {symbol} }} from '{mod}';"

    def install(self) -> None:
        self.api.logger.info("Auto Import extension installed.")
