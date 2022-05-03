# usage: run-fb-pipeline.bash tool-dir

root=$1
das2fdir=$root/das2f

# We will store the factbase in a file called fb.pl
# We will augment fb.pl in each step along the way.
# Future: we might be able to rewrite this script to use a pipeline instead of intermediate files (e.g. fb.pl)


# Layer 1. Infer low-hanging fruit information.
echo '** layer 1 a **' 1>&2
${das2fdir}/layerkind ${das2fdir} 1>&2 # <<>>fb.pl
echo '** layer 1 b **' 1>&2
${das2fdir}/layername ${das2fdir} 1>&2 # <<>>fb.pl
echo '** layer 1 c **' 1>&2
${das2fdir}/layercolor ${das2fdir} 1>&2 # <<>>fb.pl
echo '** layer 1 d **' 1>&2
${das2fdir}/layerboundingbox ${das2fdir} 1>&2 # <<>>fb.pl
echo '** layer 1 e **' 1>&2

# # Layer 2. Names, port directions
echo '** layer 2 **' 1>&2
${das2fdir}/layerdirection ${das2fdir} 1>&2 # <<>>fb.pl
#${das2fdir}/layer2  1>&2 #<<>>fb.pl



# Layer 3. Rectangle Containment relationships.
echo '** layer all contains **'  1>&2
${das2fdir}/layerallcontains ${das2fdir} 1>&2 #<<>>fb.pl


# Layer 4. Rectangle contains Port.
echo '** layer 4 **' 1>&2
${das2fdir}/layer4 ${das2fdir} 1>&2 #<<>>fb.pl

# Layer 5. indirect containment
echo '** layer 5 - indirect containment **' 1>&2
${das2fdir}/layer5 ${das2fdir} 1>&2 #<<>>fb.pl

# Layer 6. direct containment
echo '** layer 6 - direct containment **' 1>&2
${das2fdir}/layer6 ${das2fdir} 1>&2 #<<>>fb.pl

## hmm, this code has a bug (probably #1)
# # Layer edge containment 1
# echo '** layer edge containment 1 **' 1>&2
# ${das2fdir}/layeredgecontainment1 ${das2fdir} 1>&2 #<<>>fb.pl

# # Layer edge containment 2
# echo '** layer edge containment 2 **' 1>&2
# ${das2fdir}/layeredgecontainment2 ${das2fdir} 1>&2 #<<>>fb.pl
# # Layer edge containment 3
# echo '** layer edge containment 3 **' 1>&2
# ${das2fdir}/layeredgecontainment3 ${das2fdir} 1>&2 #<<>>fb.pl

# echo '** layer edge containment **' 1>&2
temp=temp_${RANDOM}
temp2=temp2_${RANDOM}
${das2fdir}/edgecontainment.bash ${das2fdir} >${temp} #<<>>fb.pl
### move result into fb.pl (without overwrite problems)
cat fb.pl $temp >$temp2
mv $temp2 fb.pl
rm -f $temp


# Layer Synccode.
echo '** layer synccode **' 1>&2
${das2fdir}/layersynccode ${das2fdir} 1>&2 #<<>>fb.pl

# Layer Connections.
echo '** layer connections **' 1>&2
${das2fdir}/layerconnection ${das2fdir} 1>&2 #<<>>fb.pl




echo '** checking design rule **' 1>&2


# # Design Rule - all ports (ellipses) must have a direction
# echo '** design rule for layer 2 **'
# ./design_rule_layer2  1>&2

dr=$root/dr
mdfile=${dr}/dr-edgecontainment.md
fname=`basename -s '.md' $mdfile`
temp=temp_${RANDOM}

${das2fdir}/a-${fname} | ${das2fdir}/b-${fname} 2> $temp

#./check-errors.bash
if grep -q failure <$temp
then
    echo
    cat $temp 1>&2
    echo quitting 1>&2
    rm $temp
    exit 1
fi
rm $temp

echo '** finished checking design rule **' 1>&2

