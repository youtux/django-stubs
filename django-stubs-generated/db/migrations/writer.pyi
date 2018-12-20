from typing import Any, Optional, Set, Tuple, Type

from django.db.migrations.migration import Migration
from django.db.migrations.operations.base import Operation

class SettingsReference(str):
    def __new__(self: Type[SettingsReference], value: str, setting_name: str) -> SettingsReference: ...
    setting_name: str = ...
    def __init__(self, value: str, setting_name: str) -> None: ...

class OperationWriter:
    operation: django.db.migrations.operations.models.CreateModel = ...
    buff: List[Any] = ...
    indentation: int = ...
    def __init__(self, operation: Operation, indentation: int = ...) -> None: ...
    def serialize(self) -> Tuple[str, Set[str]]: ...
    def indent(self) -> None: ...
    def unindent(self) -> None: ...
    def feed(self, line: str) -> None: ...
    def render(self) -> str: ...

class MigrationWriter:
    migration: Migration = ...
    needs_manual_porting: bool = ...
    def __init__(self, migration: Migration) -> None: ...
    def as_string(self) -> str: ...
    @property
    def basedir(self) -> str: ...
    @property
    def filename(self) -> str: ...
    @property
    def path(self) -> str: ...
    @classmethod
    def serialize(cls, value: Any) -> Tuple[str, Set[str]]: ...

MIGRATION_TEMPLATE: str