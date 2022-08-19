# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/distributed.core.ipynb.

# %% auto 0
__all__ = ['ParallelBackend']

# %% ../nbs/distributed.core.ipynb 4
from typing import Any

from ..core import StatsForecast

# %% ../nbs/distributed.core.ipynb 5
class ParallelBackend:
    def forecast(self, df, models, freq, **kwargs: Any) -> Any:
        model = StatsForecast(df=df, models=models, freq=freq)
        return model.forecast(**kwargs)

    def cross_validation(self, df, models, freq, **kwargs: Any) -> Any:
        model = StatsForecast(df=df, models=models, freq=freq)
        return model.cross_validation(**kwargs)