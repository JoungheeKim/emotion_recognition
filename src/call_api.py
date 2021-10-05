# coding=utf-8
# Copyright 2020 The JoungheeKim All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hydra
import os
from typing import Any, List, Optional
from src.utils import reset_logging, init, load_data, save_data
import logging
from speech_to_text import get_api_class


@hydra.main(config_path=os.path.join("..", "configs"), config_name="api")
def main(cfg):

    ## Resent Logging
    reset_logging()

    ## Pring configureation
    logging.info(cfg)

    ## load data
    df = load_data(cfg.base)

    ## make api
    api = get_api_class(cfg.api)

    ## run stt
    df = api.run_stt(df)

    ## save data
    save_data(df, cfg.base)


if __name__ == "__main__":
    init()
    main()

