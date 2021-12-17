# CmdStan CSV Parsing Testing

This is exploring the potential of using [Pydantic](https://pydantic-docs.helpmanual.io/usage/models/) to
parse the header comments of CSV files. Pydantic primarily works with loading and validating JSON, so this also serves
as a look to the future.

## Overview

- `parse.py` contains a simple recursive function that walks the CSV header and returns a nested dictionary of the
  information. It makes no assumptions about what it might find in the file, meaning it doesn't look for any particular
  string or values. It stops at the first line which does not start with a `#`, which for CmdStan is the column header line.

  It's good to note that this means it *isn't* parsing draws or adaptation information.
- `cmdstanconfig.py` and the other files contain Pydantic model definitions. They're based on the information from
  the [CmdStan guide](https://mc-stan.org/docs/2_28/cmdstan-guide/command-line-interface-overview.html).

- `examples/` contains the first 50 lines for a few different output.csv files
- `main.py` builds up an object from one of the examples and prints it. It also produces `cmdstan.schema.json`.
  The CSV is given structure using the code in `parse.py`, and then turned into a fully validated python object
  by the Pydantic library. The key idea of this approach is that both parts of this are very simple: parsing doesn't
  validate anything, and the Pydantic code exactly mirrors the spec from CmdStan.

  Run this with `python main.py`

The hope is that this will be a valuable area to explore for CmdStanPy, especially if we believe this configuration information will be available in JSON in the future.


## Future hopes

- User provided arguments are actually a subset of this data. It's concievable we could use the same object to both handle the
  args for a method and the outputs of that method with a ton of code sharing there, but some things would be messy.
- The errors provided by Pydantic are pretty good, but because we separate parsing and validation there is no line number for the
  original file. I personally think this is fine, but it would be good if we could get it back
- How this gets wired up and used in CmdStanPy is still yet to be seen.
