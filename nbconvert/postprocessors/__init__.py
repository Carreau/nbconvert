from .base import PostProcessorBase

__all__ = ["PostProcessorBase", "ServePostProcessor"]


def __getattr__(name):
    """Lazily provide ServePostProcessor, so importing this package does not load tornado."""
    if name == "ServePostProcessor":
        # protect against unavailable tornado
        try:
            from .serve import ServePostProcessor  # noqa: PLC0415
        except ImportError:
            return None
        return ServePostProcessor
    msg = f"module {__name__!r} has no attribute {name!r}"
    raise AttributeError(msg)
