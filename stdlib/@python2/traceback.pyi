import sys
from _typeshed import SupportsWrite
from types import FrameType, TracebackType
from typing import IO, Any, Dict, Generator, Iterable, Iterator, List, Mapping, Optional, Set, Tuple, Type

_PT = Tuple[str, int, str, Optional[str]]

def print_tb(tb: Optional[TracebackType], limit: Optional[int] = ..., file: Optional[IO[str]] = ...) -> None: ...
def print_exception(
    etype: Optional[Type[BaseException]],
    value: Optional[BaseException],
    tb: Optional[TracebackType],
    limit: Optional[int] = ...,
    file: Optional[IO[str]] = ...,
) -> None: ...
def print_exc(limit: Optional[int] = ..., file: Optional[IO[str]] = ...) -> None: ...
def print_last(limit: Optional[int] = ..., file: Optional[IO[str]] = ...) -> None: ...
def print_stack(f: Optional[FrameType] = ..., limit: Optional[int] = ..., file: Optional[IO[str]] = ...) -> None: ...
def extract_tb(tb: Optional[TracebackType], limit: Optional[int] = ...) -> List[_PT]: ...
def extract_stack(f: Optional[FrameType] = ..., limit: Optional[int] = ...) -> List[_PT]: ...
def format_list(extracted_list: List[_PT]) -> List[str]: ...
def format_exception_only(etype: Optional[Type[BaseException]], value: Optional[BaseException]) -> List[str]: ...
def format_exception(
    etype: Optional[Type[BaseException]], value: Optional[BaseException], tb: Optional[TracebackType], limit: Optional[int] = ...
) -> List[str]: ...
def format_exc(limit: Optional[int] = ...) -> str: ...
def format_tb(tb: Optional[TracebackType], limit: Optional[int] = ...) -> List[str]: ...
def format_stack(f: Optional[FrameType] = ..., limit: Optional[int] = ...) -> List[str]: ...
def tb_lineno(tb: TracebackType) -> int: ...