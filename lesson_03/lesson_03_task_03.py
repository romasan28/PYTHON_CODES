from address import address
from mailing import mailing

to_address = address(194328, "Saint-Petersburg", "Koroleva", 12, 345)
from_address = address(193235, "Moskow", "Aviatotrov", 7, 219)

mail1 = mailing(to_address, from_address, 1500, "sk12345_ma7219")

print(mail1)
