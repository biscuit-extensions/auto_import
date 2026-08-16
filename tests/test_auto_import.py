from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.auto_import import setup
from src.auto_import.extension import AutoImport


class TestAutoImportExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = AutoImport(app_instance.api)
        ext.register_symbol("useState", "react")
        assert ext.generate_import("useState", "javascript") == "import { useState } from 'react';"
        ext.register_symbol("Path", "pathlib")
        assert ext.generate_import("Path", "python") == "from pathlib import Path"
