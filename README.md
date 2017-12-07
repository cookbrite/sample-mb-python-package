# sample-mb-python-package

Example python package layout, and instructions.

# Using this package 

* Create a new git repository
* Clone the repository to `$MY_REPO_PATH`
* Get a copy of these sample files:
    ```bash
    cd $MY_REPO_PATH
    curl -L https://github.com/cookbrite/sample-mb-python-package/tarball/master \
        | tar xz --strip-components=1 -C .
    ``` 
* Run `init_package.sh` to propagate your own package's name where it needs to go.
* Edit the description and other informational fields in `setup.py`.
