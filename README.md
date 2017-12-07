# MetaBrite Sample Python Package

This repository contains the code and instructions MetaBrite uses to create
our internally-used python packages.

# License

The `LICENSE.metabrite` file included in this repository is intended for use
in our own packages and does not refer to this repository itself. The code
contained in this repository is distributed under the MIT license, which has
been included as `LICENSE`.  

# Using this package 

* Create a new git repository [at Github](https://help.github.com/articles/create-a-repo/), 
  or elsewhere.
* Clone the repository to a local directory of your choice, represented below as
  `$MY_REPO_PATH`.
* Get a copy of the files in **this** repository into your new one, but without
  all of the `.git` metadata:
    ```bash
    cd $MY_REPO_PATH
    curl -L https://github.com/cookbrite/sample-mb-python-package/tarball/master \
        | tar xz --strip-components=1 -C .
    ```
* If you are **not** creating an internal package for MetaBrite, you should delete
  `LICENSE.metabrite`.
* Run `init_package.sh` to propagate your own package's name where it needs to go.
* Remove the contents of the README and replace with your own documentation or placeholders.
* `setup.py` contains a section at the top containing more than a few fields that
  are currently hard-coded to values specific to MetaBrite.  You should probably
  change these.

# Additional Setup

* [License your package](https://help.github.com/articles/licensing-a-repository/)
* The `tox.ini` config is set up for MetaBrite's most common test scenarios,
  including building with cython.  You may not need all of it.
