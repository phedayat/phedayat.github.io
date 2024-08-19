input_file=$1

[[ ! -f $input_file ]] && echo "Input file not found!" && exit 1

filename_ext=$(basename $input_file)
filename="${filename_ext%.*}"
out_filename=./${filename}.md

pandoc $input_file -f typst -t markdown -s --mathjax -o $out_filename

[[ ! -f "${out_filename}" ]] && echo "Output file not created" && exit 1

# python3 fix_aligned_env.py -i $out_filename

# mv $out_filename ../content/journal