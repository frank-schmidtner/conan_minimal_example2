# How to execute minimal example

1. Export all recipes

```
conan export ./A test/test
conan export ./B test/test
conan export ./C test/test
```

2. Create lockfile for meta package with enforcing building of all upstream packages 

```
conan lock create -pr:b ./profile -pr:h ./profile ./A/conanfile.py --user=test --channel=test --build=BB --build=CC --lockfile-out=./lockfile.lock
```

3. Create build order

```
conan lock build-order lockfile.lock --json=build_order.json
```

4. Execute build.py

```
./build.py
```