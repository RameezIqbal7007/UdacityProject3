PREFIX="jckuriproject3"
RESOURCEGROUP="${PREFIX}resourcegroup"
LOCATION="westus"
STORAGEACCOUNT="${PREFIX}store"
FUNCTIONAPP="${PREFIX}functionapp"

echo "PREFIX: $PREFIX"
echo "RESOURCEGROUP: $RESOURCEGROUP"
echo "LOCATION: $LOCATION"
echo "STORAGEACCOUNT: $STORAGEACCOUNT"
echo "FUNCTIONAPP: $FUNCTIONAPP"

echo "CREATING STORAGE ACCOUNT..."
az storage account create --name $STORAGEACCOUNT --resource-group $RESOURCEGROUP --location $LOCATION

echo "CREATING FUNCTION APP..."
az functionapp create --resource-group $RESOURCEGROUP --name $FUNCTIONAPP --storage-account $STORAGEACCOUNT --os-type Linux --consumption-plan-location $LOCATION --runtime python

