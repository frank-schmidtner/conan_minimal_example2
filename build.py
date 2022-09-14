#!/usr/bin/python3

import json
import os

build_order = json.loads(open("build_order.json").read())
lockfile="lockfile.lock"
lockfile_out="full_lockfile.lock"

for level in build_order:
    for entry in level:
        ref = entry[0]
        name = ref.split("/")[0]
        context = entry[2]
        lock_id = entry[3]
        cmd = f"conan install {ref} --build={name} --lockfile={lockfile} --lockfile-node-id={lock_id} --lockfile-out={lockfile_out}"
        if context == "build":
            cmd += " --build-require"
        print(f"Executing cmd:\n{cmd}")
        if os.system(cmd) != 0:
            print("Failed")
            exit(-1)
        
        os.system(f"conan lock update {lockfile} {lockfile_out}")