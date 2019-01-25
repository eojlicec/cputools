#!/usr/bin/python
# A dictionary of available CPU's, COU scheduler limit, and CPU speed limit
from SystemConfiguration import (
    SCDynamicStoreCreate,
    SCDynamicStoreCopyValue,
)
ds = SCDynamicStoreCreate(None, 'power', None, None)
result = SCDynamicStoreCopyValue(ds, 'State:/IOKit/Power/CPUPower')
