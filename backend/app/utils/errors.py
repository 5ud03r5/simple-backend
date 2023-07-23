class NotFoundError(Exception):
    status_code = 404
    report_error = False
    expose = True
