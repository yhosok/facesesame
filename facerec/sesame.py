from pysesame2 import Sesame
from time import sleep
from uuid import UUID
import settings


def unlock_sesame():
    device_id = UUID(settings.SESAME_UUID)
    sesame = Sesame(device_id, settings.SESAME_KEY)
    status = sesame.get_status()
    if status['locked']:
        task = sesame.async_unlock()
        while task.pooling() is False:
            print('Processing...')
            sleep(1)
        print('Result: %s' % task.is_successful)
