from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from typing import List

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class FlashcardsTest(StageTest):

    def generate(self) -> List[TestCase]:
        return [TestCase(attach="Card:\nDefinition:\n")]

    def check(self, reply: str, attach: str) -> CheckResult:
        lines_n = 4
        first_line, third_line = attach.strip().split('\n')
        reply = reply.strip().split('\n')
        reply_lines_n = len(reply)

        if reply_lines_n != lines_n:
            return CheckResult.wrong("Your program outputs {0} line{1}, "
                                     "while {2} lines were expected".format(reply_lines_n,
                                                                            's' if reply_lines_n != 1 else '',
                                                                            lines_n))

        if reply[0].strip() != first_line:
            return CheckResult.wrong("Your first line is \"{0}\", but line \"{1}\" was expected".format(reply[0],
                                                                                                        first_line))

        if reply[2].strip() != third_line:
            return CheckResult.wrong("Your third line is \"{0}\", but line \"{1}\" was expected".format(reply[2],
                                                                                                        third_line))

        return CheckResult.correct()


if __name__ == "__main__":
    FlashcardsTest('flashcards.flashcards').run_tests()
