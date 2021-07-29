import settings
from cStringIO import StringIO

MSI_TEMPLATE=settings.CANARY_MSI_TEMPLATE

def make_canary_windows_process(template=MSI_TEMPLATE):
    with open(template, 'r') as f:
        output_buf = StringIO(f.read())
    return output_buf.getvalue()

if __name__ == '__main__':
    with open('testdoc.msi', 'w+') as f:
        f.write(make_canary_windows_process())
