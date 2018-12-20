from typing import Any, Optional, Set

from django.core.management.base import BaseCommand, CommandParser
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.migrations.migration import Migration

class Command(BaseCommand):
    stderr: django.core.management.base.OutputWrapper
    stdout: django.core.management.base.OutputWrapper
    style: django.core.management.color.Style
    help: str = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    verbosity: Any = ...
    interactive: Any = ...
    def handle(self, *args: Any, **options: Any) -> None: ...
    start: Any = ...
    def migration_progress_callback(
        self, action: str, migration: Optional[Migration] = ..., fake: bool = ...
    ) -> None: ...
    def sync_apps(self, connection: DatabaseWrapper, app_labels: Set[str]) -> None: ...