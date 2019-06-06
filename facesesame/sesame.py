from pysesame2 import Sesame, SesameError
from time import sleep
from uuid import UUID
import settings
import logger
import traceback

logger = logger.getLogger()


def unlock_sesame():
    device_id = UUID(settings.SESAME_UUID)
    sesame = Sesame(device_id, settings.SESAME_KEY)
    status = sesame.get_status()
    if status['locked']:
        try:
            task = sesame.async_unlock()
            logger.info('sasame is locked. will unlock')
            try_count = 0
            while task.pooling() is False:
                if (try_count > 10):
                    logger.error('Failed to unlock sesame')
                    break
                logger.debug('Processing...')
                sleep(1)
                try_count += 1
            logger.info('Result: %s' % task.is_successful)
        except SesameError:
            logger.error(traceback.print_exc())
