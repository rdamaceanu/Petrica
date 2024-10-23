from database.week_crud import create_week
from datetime import datetime, timedelta

# Create a new week
start_date = datetime.strptime('2023-10-01', '%Y-%m-%d').date()
end_date = start_date + timedelta(days=5)
weekid = create_week(start_date, end_date)