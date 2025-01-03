#!/bin/bash

python -m sample.generate --model_path ./model/motion/humanml_enc_512_50steps/model000750000.pt --num_samples 10 --num_repetitions 3 --device 0  --text_prompt "the person sits down and claps"