
class ErrorCode:
    OK = 0
    # error codes for doctor
    UNSUPPORTED_LOGIN_TYPE              = 1001
    DOCTOR_ACCOUNT_NONEXISTS            = 1002
    DOCTOR_ACCOUNT_EXISTS               = 1003
    DOCTOR_PASSWORD_ERROR               = 1004
    DOCTOR_PASSWORD_NOTSET              = 1005
    DOCTOR_VERIFY_CODE_ERROR            = 1006
    DOCTOR_VERIFY_CODE_EXPIRED          = 1007
    REGISTER_DOCTOR_ERROR               = 1008
    CHANGE_DOCTOR_INFO_ERROR            = 1009
    UNSUPPORTED_DOCTOR_CHANGE_INFO_TYPE = 1010
    DELETE_DOCTOR_INFO_ERROR            = 1011

    # error codes for patient
    # TODO

    # other error codes
    DB_CONNECTION_ERROR         = 8001
    REQUEST_DATA_FORMAT_ERROR   = 8002
    MISSING_REQUIRED_PARAMS     = 8003
    FILE_TOO_LARGE              = 8004
    REQUEST_DATA_ERROR          = 8005

    error_descriptions = {
        OK                            : "OK",
        # error descriptions for doctor
        DOCTOR_ACCOUNT_NONEXISTS            : "doctor account nonexists",
        DOCTOR_ACCOUNT_EXISTS               : "doctor account exists",
        DOCTOR_PASSWORD_ERROR               : "doctor password error",
        DOCTOR_PASSWORD_NOTSET              : "doctor password notset",
        DOCTOR_VERIFY_CODE_ERROR            : "doctor verify code error",
        DOCTOR_VERIFY_CODE_EXPIRED          : "doctor verify code expired",
        REGISTER_DOCTOR_ERROR               : "register doctor error",
        CHANGE_DOCTOR_INFO_ERROR            : "change doctor info error",
        UNSUPPORTED_DOCTOR_CHANGE_INFO_TYPE : "unsupported doctor change info type",
        DELETE_DOCTOR_INFO_ERROR            : "delete doctor info error",

        # other error codes
        DB_CONNECTION_ERROR                 : "db connection error",
        REQUEST_DATA_FORMAT_ERROR           : "request data format error",
        MISSING_REQUIRED_PARAMS             : "missing required params",
        FILE_TOO_LARGE                      : "file too large",
        REQUEST_DATA_ERROR                  : "request data error",
    }

    @staticmethod
    def get_description(code):
        return ErrorCode.error_descriptions.get(code, "Unknown error code")

# test
if __name__ == "__main__":
    print(ErrorCode.OK)  # 0
    print(ErrorCode.get_description(ErrorCode.OK))  # 成功