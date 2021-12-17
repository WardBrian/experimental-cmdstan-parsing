from typing import Literal, Union
from pydantic import BaseModel
from pydantic.types import NonNegativeInt, PositiveFloat, PositiveInt, confloat


class NUTSConfig(BaseModel):
    class NUTSConfigInternal(BaseModel):
        max_depth: int

    nuts: NUTSConfigInternal


class StaticConfig(BaseModel):
    class StaticConfigInternal(BaseModel):
        int_time: PositiveFloat

    static: StaticConfigInternal


class SamplerHMCConfig(BaseModel):
    class SamplerHMCConfigInternal(BaseModel):
        engine: Union[NUTSConfig, StaticConfig]
        metric: Literal["unit", "diag_e", "dense_e"]
        metric_file: str
        stepsize: PositiveFloat
        stepsize_jitter: confloat(ge=0, le=1)

    hmc: SamplerHMCConfigInternal


class SamplerAdaptConfig(BaseModel):
    engaged: bool
    gamma: PositiveFloat
    delta: confloat(gt=0, lt=1)
    kappa: PositiveFloat
    t0: PositiveFloat
    init_buffer: int
    term_buffer: int
    window: int


class SamplerConfig(BaseModel):
    class SamplerConfigInternal(BaseModel):
        num_samples: NonNegativeInt
        num_warmup: NonNegativeInt
        save_warmup: bool
        thin: PositiveInt
        adapt: SamplerAdaptConfig
        algorithm: Union[SamplerHMCConfig, Literal["fixed_param"]]
        num_chains: PositiveInt

    sample: SamplerConfigInternal
