#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"  # 设置为hf的国内镜像网站

from huggingface_hub import snapshot_download

access_token=""

model_name = "Qwen/Qwen2.5-Coder-0.5B"

local_dir="/data/models/"
# 最后下载文件的路径再local_dir/model_name路径下面
local_dir+=model_name

ignore_file_pattern=[]

# while True 是为了防止断联
while True:
    try:
        snapshot_download(
            repo_id=model_name,
            local_dir_use_symlinks=True,  # 在local-dir指定的目录中都是一些“链接文件”
            ignore_patterns=ignore_file_pattern,  # 忽略下载哪些文件
            local_dir=local_dir,
            token=access_token,   # huggingface的token
            resume_download=True
        )
        break
    except:
        pass
