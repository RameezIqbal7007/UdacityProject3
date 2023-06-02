PREFIX="jckuriproject3"
RESOURCEGROUP="${PREFIX}resourcegroup"
LOCATION="westus"
SQLSERVER="${PREFIX}sqlserver"
DATABASE="techconfdb"
CLIENTIP=$(curl ifconfig.me)

echo "PREFIX: $PREFIX"
echo "RESOURCEGROUP: $RESOURCEGROUP"
echo "LOCATION: $LOCATION"
echo "SQLSERVER: $SQLSERVER"
echo "DATABASE: $DATABASE"
echo "CLIENT IP: $CLIENTIP"

echo "CREATING RESOURCE GROUP..."
az group create --name $RESOURCEGROUP --location $LOCATION

echo "CREATING DATASE SERVER..."
az postgres server create --location $LOCATION --resource-group $RESOURCEGROUP --name $SQLSERVER --admin-user dbadmin --admin-password admin_password123 --sku-name B_Gen5_1

echo "CREATING FIREWALL RULE..."
az postgres server firewall-rule create --resource-group $RESOURCEGROUP --server $SQLSERVER --name allips --start-ip-address 0.0.0.0 --end-ip-address 255.255.255.255

echo "SHOWING DATABASE SERVER..."
az postgres server show --resource-group $RESOURCEGROUP --name $SQLSERVER

echo "CREATING DATABASE..."
az postgres db create --name $DATABASE --resource-group $RESOURCEGROUP --server $SQLSERVER
