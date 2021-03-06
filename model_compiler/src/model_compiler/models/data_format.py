# Copyright 2019 ZTE corporation. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import enum
from enum import Enum
from typing import Optional

from ..protos.generated.model_config_pb2 import ModelInput


class DataFormat(Enum):
    CHANNELS_FIRST = enum.auto()
    CHANNELS_LAST = enum.auto()


def as_model_config_data_format(data_format: Optional[DataFormat]):
    if data_format is None:
        result = ModelInput.FORMAT_NONE  # pylint: disable=no-member
    elif data_format == DataFormat.CHANNELS_FIRST:
        result = ModelInput.FORMAT_NCHW  # pylint: disable=no-member
    else:
        result = ModelInput.FORMAT_NHWC  # pylint: disable=no-member

    return result


def str_to_data_format(input_str: Optional[str]) -> Optional[DataFormat]:
    if input_str == 'channels_first':
        return DataFormat.CHANNELS_FIRST
    if input_str == 'channels_last':
        return DataFormat.CHANNELS_LAST
    return None
