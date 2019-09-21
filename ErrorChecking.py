import inspect


class ErrorChecking:
    def __init__(self):
        self.message = []  # argument, function name, class name

    def check(self, variable, varType, message):
        previous_frame = inspect.currentframe().f_back
        caller_function_header = inspect.getframeinfo(
            previous_frame).code_context[0].strip()
        print(caller_function_header)
        caller_function_args = caller_function_header[caller_function_header.find(
            '(') + 1:-1].split(',')
        self.variable_name = caller_function_args[0]

        # frame is a named tuple of
        # filename, line_number, function_name, lines, index
        self.caller_function_name = inspect.getframeinfo(
            previous_frame).function

        self.maybe_caller_class_info = None
        if previous_frame.f_locals.get('self'):
            self.maybe_caller_class_info = ' inside the {} class'.format(
                previous_frame.f_locals['self'].__class__.__name__)

        message.replace(" ", "")
        # self.message = message.split(",")
        errorMessage = {
            "int": lambda: self.notAInt(variable),
            "string": lambda: self.notAString(variable),
            "list": lambda: self.notAList(variable),
            "bool": lambda: self.notABool(variable),
            "float": lambda: self.notAFloat(variable),
            "floatOrInt": lambda: self.notAFloatOrInt(variable)
        }
        errorMessage[varType]()

    def notAInt(self, variable):
        if not isinstance(variable, int):
            print(self.error_message("int"))

    def notAString(self, variable):
        if not isinstance(variable, str):
            print(self.error_message("string"))

    def notAList(self, variable):
        if not isinstance(variable, list):
            print(self.error_message("list"))

    def notABool(self, variable):
        if not isinstance(variable, bool):
            print(self.error_message("list"))

    def notAFloat(self, variable):
        if not isinstance(variable, float):
            print(self.error_message("float"))

    def notAFloatOrInt(self, variable):
        if not isinstance(variable, float) and not isinstance(variable, int):
            print(self.error_message("float or int"))

    def error_message(self, reqType):
        return 'The {var} argument of the {func} function{maybe_class_info} is not a {req_type}!'.format(
               var=self.variable_name, func=self.caller_function_name, maybe_class_info=self.maybe_caller_class_info, req_type=reqType)
