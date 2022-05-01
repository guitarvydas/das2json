#!/bin/bash
# usage: generate.bash <tools root directory> <.drawio file>
#                      $1                     $2

# tools root - takes the place of $PATH
# change this for your own environment
root=`realpath $1`

infile=$2

${root}/d2f/d2f.bash ${root} ${infile} >fb.pl
# from this point on, we can ignore ${infile} since it's been converted to fb.pl
${root}/das2f/run-fb-pipeline.bash ${root} #2>/dev/null
${root}/das2j/layercomponent_query.bash >out.json
echo
echo 'out.json written'
echo

