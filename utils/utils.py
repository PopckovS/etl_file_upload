import logging
import owncloud
from django.conf import settings
from owncloud import HTTPResponseError
logger = logging.getLogger(__name__)


def owncloud_document_download(path: str = None) -> str:
    """
    Скачивает файл с OwnCloud.
    :param path: str путь куда сохранить файл.
    :return: str путь куда сохранен файл.
    """
    logger.info('Скачиваем файл с OwnCloud...')
    try:
        # соединение с облаком
        _cloud = owncloud.Client.from_public_link(
            public_link=settings.OWN_CLOUD_DOMAIN
        )

        # подтверждаем свои права
        _cloud.login(
            user_id=settings.OWN_CLOUD_LOGIN,
            password=settings.OWN_CLOUD_PASSWORD
        )

        # скачиваем файл
        _cloud.get_file(
            local_file=path,
            remote_path=settings.SOURCE_FILE
        )
        logger.info('Файл успешно скачен с OwnCloud...ок')

    except HTTPResponseError as e:
        logger.error('Скачивание файла "{file}" с OwnCloud не удалось'.format(
            file=settings.SOURCE_FILE))
        logging.exception(e)

    return path
