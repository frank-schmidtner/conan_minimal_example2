# How to execute minimal example

1. Export all recipes

```
conan export ./meta_package test/test
conan export ./sub_package test/test
conan export ./sub_package2 test/test
conan export ./sub_sub_package test/test
```

3. Create lockfile for meta package with enforcing building of all upstream packages 

```
conan lock create -pr:b ./build_profile -pr:h ./host_profile ./meta_package/conanfile.py --user=test --channel=test --build=sub_package --build=sub_package2 --build=sub_sub_package --lockfile-out=./deps_lockfile.lock
```

4. Try to build the sub_package2 in build context with the lockfile

```
conan install sub_package2/1.0.0@test/test --build=sub_package2 --lockfile=deps_lockfile.lock --lockfile-node-id=4 --build-require
```