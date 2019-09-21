import inspect


class ErrorChecking:
    def __init__(self):
        self.checklist = {
            "int": self.notAInt,
            "string": self.notAString,
            "list": self.notAList,
            "bool": self.notABool,
            "float": self.notAFloat,
            "floatOrInt": self.notAFloatOrInt
        }

    def check(self, variable, varType):
        self.var_type = varType
        previous_frame = inspect.currentframe().f_back
        caller_function_header = inspect.getframeinfo(
            previous_frame).code_context[0].strip()
        caller_function_args = caller_function_header[caller_function_header.find(
            '(') + 1:-1].split(',')
        self.variable_name = caller_function_args[0]

        # frame is a named tuple of
        # filename, line_number, function_name, lines, index
        self.caller_function_name = inspect.getframeinfo(
            previous_frame).function

        self.maybe_caller_class_info = ''
        if previous_frame.f_locals.get('self'):
            self.maybe_caller_class_info = ' inside the {} class'.format(
                previous_frame.f_locals['self'].__class__.__name__)

        if self.var_type in self.checklist:
            self.checklist[self.var_type](variable)

    def notAInt(self, variable):
        if not isinstance(variable, int):
            print(self.error_message())

    def notAString(self, variable):
        if not isinstance(variable, str):
            print(self.error_message())

    def notAList(self, variable):
        if not isinstance(variable, list):
            print(self.error_message())

    def notABool(self, variable):
        if not isinstance(variable, bool):
            print(self.error_message())

    def notAFloat(self, variable):
        if not isinstance(variable, float):
            print(self.error_message())

    def notAFloatOrInt(self, variable):
        if not isinstance(variable, float) and not isinstance(variable, int):
            print(self.error_message())

    def error_message(self):
        return 'The {var} argument of the {func} function{maybe_class_info} is not a {req_type}!' \
        .format(
                var=self.variable_name,
                func=self.caller_function_name,
                maybe_class_info=self.maybe_caller_class_info,
                req_type=self.var_type
               )
