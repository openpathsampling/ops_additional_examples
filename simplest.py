from __future__ import print_function
from jupyter_client.manager import KernelManager

km = KernelManager()
km.start_kernel()
kc = km.client()
kc.start_channels()

cmds = ["import no_mpl", "import has_mpl"]
for cmd in cmds:
    print(cmd)
    kc.execute(cmd)

