from typing import Dict, Union
from pydantic import BaseModel
from pydantic.types import PositiveFloat, PositiveInt


class VariationalAdaptConfig(BaseModel):
    engaged: bool
    iter: PositiveInt


# unfortunate inconsistency means these aren't just literal strings
class FullrankConfig(BaseModel):
    fullrank: Dict = {}


class MeanfieldConfig(BaseModel):
    meanfield: Dict = {}


class VariationalConfig(BaseModel):
    class VariationalConfigInternal(BaseModel):
        algorithm: Union[FullrankConfig, MeanfieldConfig]
        iter: PositiveInt
        grad_samples: PositiveInt
        eta: PositiveFloat
        adapt: VariationalAdaptConfig
        tol_rel_obj: PositiveFloat
        eval_elbo: PositiveInt
        output_samples: PositiveInt

    variational: VariationalConfigInternal
