from typing import Union
from pydantic import BaseModel


from sampler import SamplerConfig
from mle import MLEConfig
from variational import VariationalConfig


class DataConfig(BaseModel):
    file: str


class RandomConfig(BaseModel):
    seed: int


class OutputConfig(BaseModel):
    file: str
    diagnostic_file: str
    refresh: int
    sig_figs: int
    profile_file: str


class Config(BaseModel):
    filename: str
    stan_version_major: int
    stan_version_minor: int
    stan_version_patch: int
    model: str
    start_datetime: str  # not working as `datetime`
    # alt. make all of these subclasses of this, instantiate those directly
    # like how LBFGSInternalConfig is implemented in mle.py
    method: Union[SamplerConfig, MLEConfig, VariationalConfig]
    id: int
    # this means a value can accept 'None', but still requires a value
    # data: Optional[DataConfig] = ...
    data: DataConfig
    init: Union[float, str]
    random: RandomConfig
    output: OutputConfig
    num_threads: int
    stanc_version: str
    stancflags: str

    # could define a compose_command on all these, especially if
    # we allowed None from the user.

    # this would mean one object does both the user command line
    # and the reading in of CSV
    # https://github.com/samuelcolvin/pydantic/issues/717 would be great
