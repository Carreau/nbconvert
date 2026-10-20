# Class base Preprocessors

from .base import Preprocessor
from .clearmetadata import ClearMetadataPreprocessor
from .clearoutput import ClearOutputPreprocessor
from .coalescestreams import CoalesceStreamsPreprocessor
from .convertfigures import ConvertFiguresPreprocessor
from .csshtmlheader import CSSHTMLHeaderPreprocessor
from .extractattachments import ExtractAttachmentsPreprocessor
from .extractoutput import ExtractOutputPreprocessor
from .highlightmagics import HighlightMagicsPreprocessor
from .latex import LatexPreprocessor
from .regexremove import RegexRemovePreprocessor
from .svg2pdf import SVG2PDFPreprocessor
from .tagremove import TagRemovePreprocessor

__all__ = [
    "CSSHTMLHeaderPreprocessor",
    "CellExecutionError",
    "ClearMetadataPreprocessor",
    "ClearOutputPreprocessor",
    "CoalesceStreamsPreprocessor",
    "ConvertFiguresPreprocessor",
    "ExecutePreprocessor",
    "ExtractAttachmentsPreprocessor",
    "ExtractOutputPreprocessor",
    "HighlightMagicsPreprocessor",
    "LatexPreprocessor",
    "Preprocessor",
    "RegexRemovePreprocessor",
    "SVG2PDFPreprocessor",
    "TagRemovePreprocessor",
]


def __getattr__(name):
    """Lazily provide the nbclient-based names, so importing this package does not load nbclient."""
    if name == "ExecutePreprocessor":
        from .execute import ExecutePreprocessor  # noqa: PLC0415

        return ExecutePreprocessor
    if name == "CellExecutionError":
        # Backwards compatibility for imported name
        from nbclient.exceptions import CellExecutionError  # noqa: PLC0415

        return CellExecutionError
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)
