# versioner

```yaml

---
name: Test workflow
on:
  push:
    branches:
      - develop
      - main
  workflow_dispatch:

jobs:

  test-versioner:
    name: Version Test
    runs-on: ubuntu-22.04
    steps:
    - name: Version Default
      id: new_version
      uses: craig8/versioner@v1
    - name: New Version Output
      run: |
        echo "The new version is: ${{ steps.new_version.outputs.new-version }}"

```