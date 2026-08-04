# coding: utf-8
"""Helpers for numeric document id + UUID companion fields."""
from __future__ import annotations
from typing import Any, Optional, Tuple

def split_document_id(value: Any) -> Tuple[Optional[int], Optional[str]]:
    if value is None:
        return None, None
    if isinstance(value, str):
        return None, value
    if isinstance(value, bool):
        raise TypeError("Document id must be int or str, not bool")
    if isinstance(value, (int, float)):
        return int(value), None
    raise TypeError(f"Unsupported document id type: {type(value)!r}")

def assign_wire_id(dst: dict, wire_key: str, numeric_id: Any, uuid: Any) -> None:
    if uuid is not None:
        dst[wire_key] = uuid
    elif numeric_id is not None:
        dst[wire_key] = numeric_id
