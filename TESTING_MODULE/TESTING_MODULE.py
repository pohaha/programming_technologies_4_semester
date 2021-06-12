import os
import sys


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class TestCase:
    case_name = "none"
    expected_result = "none"
    args = []

    def __init__(self, case_name, expected_result, *args):
        self.args = []
        self.case_name = case_name
        self.expected_result = expected_result
        for argument in args:
            self.args.append(argument)


class Test:
    def __init__(self, *args):
        self.m_tested_function = args[0]
        self.m_test_name = args[1]
        self.m_cases = []

    def add_case(self, case_name, expected_result, *args):
        self.m_cases.append(TestCase(case_name, expected_result, *args))

    def _compare(self, expected_result, returned_result):
        if(type(expected_result != type(returned_result))):
            return " test \033[31m falure: \033[39m"
        try:
            iter(expected_result)
            iter(returned_result)
        except:
            if(expected_result == returned_result):
                result = " test \033[32m successfull \033[39m"
            else:
                result = " test \033[31m falure: \033[39m"
        else:
            if((len(expected_result) != 1) and (len(expected_result) == len(returned_result))):
                bool_array = (x == y for x, y in zip(
                    expected_result, returned_result))
                print(bool_array)
                """ if((x == y for x, y in zip(expected_result, returned_result)).all()):
                    result = " test \033[32m successfull \033[39m"
                else: """
                result = " test \033[31m falure: \033[39m"
        return result

    def run(self):
        print(f"running \033[96m{self.m_test_name}\033[39m tests")
        for case in self.m_cases:
            try:
                with HiddenPrints():
                    case_result = self.m_tested_function(*(case.args))
            except Exception as ex:
                case_result = "runtime failure "+str(ex)
            ##result = self._compare(case.expected_result, case_result)
            try:
                resulting_boolean = bool(
                    case_result == case.expected_result)
            except Exception as ex:
                case_result = "runtime failure "+str(ex)
                result = " test \033[31m falure: \033[39m"
            else:
                if(resulting_boolean):
                    result = " test \033[32m successfull \033[39m"
                else:
                    result = " test \033[31m falure: \033[39m"
            print("\t" + "\033[93m"+case.case_name+"\033[39m" + result)
            if(result == " test \033[31m falure: \033[39m"):
                print(f"\t\texpected: {case.expected_result}\n" +
                      f"\t\tgot: \033[31m{case_result}\033[39m")
