from datetime import datetime


def horaLocal():
    result = datetime.now().hour
    return result

def diferencia():
    hourExit = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 19)
    dif = hourExit - datetime.now()
    return dif

