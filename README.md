
# Dodo Tutorial
1. [What is Dodo](#What-is-Dodo-?)
2. [Motivation](#motivation)
3. [Write a simple test](#write-a-simple-test)
4. [Execute tests](#execute-tests)
5. [License](#license)
6. [Contribute](#contribute)
7. [Contact](#contact)


## What is Dodo ?
Dodo is a test execution framework completely written using *Python* programming language. You can write test cases using Python and use assertions that you do in other test frameworks.

## Motivation
The major motivation behind development of Dodo is to understand how test frameworks are developed and how do they work. At this point Dodo is not used in production (at least I am not aware of any organization) so there may be unknown issues lurking somewhere in code.

## Write a simple test
Writing test that can be executed by Dodo is extremely simple. You just have to create a Python package that contains a Python modules containing tests. Test functions must be prefixed with ***test***. i.e ***test_database_connection***. You can find an example test in [Example test](https://github.com/vbmade2000/Dodo/tree/master/examples/testpackage) directory.

## Execute tests
Tests can be executed in the following way.
`$ dodo \<path-to-test-package\>`

After execution you can see results like given below. The result will be printed in Green colour for passed tests and Red for failed tests.

> $ dodo /tmp/testpackage/
> test_conf_file_not_present - Pass
> test_database_connection - Pass

## License
Yet to be decided.

## Contribute
You can use Github issue tracker to file a bug. Contribution to code is not accepted yet due to lack of time for review and infrastructure.

## Contact
You can contact me at [Malhar Vora](mailto:vbmade2000@gmail.com)  or [Madhura mande](mailto:mandemadhura@gmail.com) if you want to use Dodo and want to add some feature.
