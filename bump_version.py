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
    print(opts.default)
    sys.exit(0)

if opts.git_version.startswith("v"):
    opts.git_version = opts.git_version[1:]

ver = semver.Version.parse(opts.git_version)
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

print(f"v{out} {out}")
