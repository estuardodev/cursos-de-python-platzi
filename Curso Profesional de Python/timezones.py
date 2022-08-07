from datetime import datetime
import pytz

guatemala_timezone = pytz.timezone("America/Guatemala")
guatemala_date = datetime.now(guatemala_timezone)
print("Guatemala: ", guatemala_date.strftime("%d/%m/%Y, %H:%M:%S"))

argentina_timezone = pytz.timezone("America/Argentina/Buenos_Aires")
argentina_date = datetime.now(argentina_timezone)
print("Buenos Aires: ", argentina_date.strftime("%d/%m/%Y, %H:%M:%S"))