# Timezone Conversion:


from datetime import datetime
from pytz import timezone

# Set timezone
local_tz = timezone('US/Eastern')
utc_time = datetime.now(timezone('UTC'))

# Convert to local timezone
local_time = utc_time.astimezone(local_tz)
print("Local Time:", local_time)
