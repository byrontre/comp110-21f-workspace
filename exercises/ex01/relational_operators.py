"""You've Got Relational Consistency."""

__author__ = "730345086"

tae_yeon: str = input("Left-hand side: ")
tif_fany: str = input("Right-hand side: ")

lessr = tae_yeon + " < " + tif_fany + " is False"
atlst = tae_yeon + " >= " + tif_fany + " is True"
eqlto = tae_yeon + " == " + tif_fany + " is False"
nteql = tae_yeon + " != " + tif_fany + " is True"

print(lessr)
print(atlst)
print(eqlto)
print(nteql)