#
# Copyright (c) 2020 Carsten Igel.
#
# This file is part of rtcg
# (see https://github.com/carstencodes/rtcg).
#
# License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
#

import unittest

import rtcg


class BasicTest(unittest.TestCase):
    def test_basic(self) -> None:
        def none():
            pass

        fn_under_test = rtcg.create_function("foo", none)
        self.assertIsNotNone(fn_under_test)

    def test_basic_correct_type(self) -> None:
        def none():
            pass

        fn_under_test = rtcg.create_function("foo", none)
        self.assertTrue(callable(fn_under_test))

    def test_void_void_method(self) -> None:
        called = False

        def test():
            nonlocal called
            called = True

        fn_under_test = rtcg.create_function("foo", test)
        fn_under_test()
        self.assertTrue(called)

    def test_void_int_method(self) -> None:
        def test():
            return 1

        fn_under_test = rtcg.create_function("foo", test, result_type=int)
        value = fn_under_test()
        self.assertEqual(value, 1)

    def test_int_int_method(self) -> None:
        def test(val: int):
            return val + 1

        fn_under_test = rtcg.create_function(
            "foo", test, rtcg.Argument("val", int), result_type=int
        )
        value = fn_under_test(1)
        self.assertEqual(value, 2)


if __name__ == "__main__":
    unittest.main()
