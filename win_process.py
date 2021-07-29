import settings
import tempfile
import shutil
import datetime
import random
from zipfile import ZipFile, ZipInfo
from ziplib import MODE_DIRECTORY
from cStringIO import StringIO

MSI_TEMPLATE=settings.CANARY_MSI_TEMPLATE


def make_canary_windows_process(template=MSI_TEMPLATE):
    with open(template, 'r') as f:
        input_buf = StringIO(f.read())
    output_buf = StringIO()
    return output_buf.getvalue()

if __name__ == '__main__':
    with open('testdoc.msi', 'w+') as f:
        f.write(make_canary_windows_process())