def lcs(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    result = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            result = x[i - 1] + result
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
            
  import codewars_test as test
from solution import lcs


@test.describe("Tests")
def test_group():
    @test.it("Fixed tests")
    def test_case():
        test.assert_equals(lcs("", ""), "")
        test.assert_equals(lcs("abc", ""), "")
        test.assert_equals(lcs("", "abc"), "")
        test.assert_equals(lcs("a", "b"), "")
        test.assert_equals(lcs("a", "a"), "a")
        test.assert_equals(lcs("abc", "a"), "a")
        test.assert_equals(lcs("abc", "ac"), "ac")
        test.assert_equals(lcs("abcdef", "abc"), "abc")
        test.assert_equals(lcs("abcdef", "acf"), "acf")
        test.assert_equals(lcs("anothertest", "notatest"), "nottest")
        test.assert_equals(lcs("132535365", "123456789"), "12356")
        test.assert_equals(lcs("nothardlythefinaltest", "zzzfinallyzzz"), "final")
        test.assert_equals(lcs("abcdefghijklmnopq", "apcdefghijklmnobq"), "acdefghijklmnoq")
