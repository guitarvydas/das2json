#!/bin/bash
cat \
    0D/python/gensym.py \
    0D/python/datum.py \
    0D/python/message.py \
    0D/python/dynrouting.py \
    0D/python/container.py \
    0D/python/registry.py \
    0D/python/process.py \
    0D/python/0d.py \
    0D/python/std/std.py \
    0D/python/std/lib.py \
    0D/python/std/fakepipe.py \
    0D/python/std/transpiler.py \
    0D/python/std/stock.py \
    0D/python/std/run.py \
    > py0d.py

