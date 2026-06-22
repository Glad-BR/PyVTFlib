from PyVTFLib import (
    VTF_FLAG as FLAG,
    CreateVTFOptions,
    ExtractVTFOptions,
    NormalMapOptions,
    ResizeOptions,
    FORMAT,
    PLATFORM,
    FILE_FORMAT,
    RESIZE_FILTER,
    RESIZE_METHOD,
    COMPRESSION_METHOD,
    VERSION,
    create,
    extract
)

from pathlib import Path


test = Path('tests')
example_img = test/'test.png'
example_vtf = test/'output.vtf'
example_extract = test/'extract.png'

# Super Simple VTF creation
options = CreateVTFOptions(
    input_path=example_img,
    output_path=example_vtf,
    format=FORMAT.DXT5,
    vtf_flags=[FLAG.ANISOTROPIC, FLAG.TRILINEAR]
)
create(options)

# Convert VTF to regular image
options = ExtractVTFOptions(
    input_path=example_vtf,
    output_path=example_extract,
)
extract(options)

