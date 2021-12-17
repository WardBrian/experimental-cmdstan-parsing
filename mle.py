from typing import Literal, Union
from pydantic import BaseModel
from pydantic.types import (
    NonNegativeInt,
    PositiveFloat,
)


class BFGSInternalConfig(BaseModel):
    init_alpha: PositiveFloat
    tol_obj: PositiveFloat
    tol_rel_obj: PositiveFloat
    tol_grad: PositiveFloat
    tol_rel_grad: PositiveFloat
    tol_param: PositiveFloat


class BFGSConfig(BaseModel):
    bfgs: BFGSInternalConfig


class LBFGSConfig(BaseModel):
    class LBFGSInternalConfig(BFGSInternalConfig):
        history_size: NonNegativeInt

    lbfgs: LBFGSInternalConfig


class MLEConfig(BaseModel):
    class MLEConfigInternal(BaseModel):
        algorithm: Union[LBFGSConfig, BFGSConfig, Literal["newton"]]
        iter: NonNegativeInt
        save_iterations: bool

    optimize: MLEConfigInternal
