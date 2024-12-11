#!/bin/bash
sed -E '/^[ \t]*<\/mxCell>$/d' $1 | sed -E '/^[ \t]*$/d'

