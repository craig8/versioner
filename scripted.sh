default_version="v1.0.0"
# current_git_tag is the last tagged relese in the repository.   From there
# we need to remove the v from the begining of the tag.
results=$(git tag -l "v*" = '')
if [[ $results == '' ]]; then
    current_git_tag="${ default_version }"
else
    # uses -V which is version sort to keep it monotonically increasing.
    current_git_tag=$(git tag -l "v*" | grep --invert-match '-' | sort --reverse -V  | sed -n 1p)
fi

echo "$current_git_tag  $default_version"

if [[ "${current_git_tag}" == "${default_version}" ]] ; then
echo "They are the same"
fi

my_new_versions=$(python bump_version.py "${default_version}" --git-version "${current_git_tag}")

echo $my_new_versions
#current_git_tag=${current_git_tag#?}