# Copyright (c) Meta Platforms, Inc. and affiliates. All Rights Reserved

# pyre-unsafe

__version__ = "0.1.0"

__all__ = ["build_sam3_image_model", "build_sam3_predictor"]


def __getattr__(name):
    # Lazy, so importing a data submodule does not load the model stack, which
    # initialises CUDA at import.
    if name in __all__:
        from . import model_builder

        return getattr(model_builder, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
