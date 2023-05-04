import argparse
import sys

import semver

parser = argparse.ArgumentParser()

parser.add_argument(
    "default", help="The default version if the git version is unavailable.")
parser.add_argument("--git-version",
                    help="The current git version released.",
                    default=None)

opts = parser.parse_args()

# print(f"Inputs: {opts}")

if opts.git_version is None:
    if opts.default.startswith("v"):
        opts.default = opts.default[1:]
    print(f"{opts.default}")
    sys.exit(0)

if opts.git_version.startswith("v"):
    opts.git_version = opts.git_version[1:]

try:
    ver = semver.Version.parse(opts.git_version)
except ValueError:
    versplit = opts.git_version.split('.')
    for index, item in enumerate(versplit):
        versplit[index] = int(item)
    ver = semver.Version.parse(".".join([str(s) for s in versplit]))

# print(f"STarting: {ver}")

if ver.prerelease:
    # Handle the initial rc when there isn't a digit at the end.
    if ver.prerelease[-1].isdigit():
        out = ver.bump_prerelease()
    else:
        out = ver.prerelease + '0'
else:
    # print("Bumping patch")
    out = ver.bump_patch()

print(f"{out}")
