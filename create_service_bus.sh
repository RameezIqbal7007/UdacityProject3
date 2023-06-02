PREFIX="jckuriproject3"
RESOURCEGROUP="${PREFIX}resourcegroup"
LOCATION="westus"
SERVICEBUS="${PREFIX}servicebus"
QUEUE="notificationqueue"

echo "PREFIX: $PREFIX"
echo "RESOURCEGROUP: $RESOURCEGROUP"
echo "LOCATION: $LOCATION"
echo "SERVICEBUS: $SERVICEBUS"
echo "QUEUE: $QUEUE"

echo "CREATING SERVICE BUS..."
az servicebus namespace create --resource-group $RESOURCEGROUP --name $SERVICEBUS --location $LOCATION --sku Basic

echo "CREATING QUEUE..."
az servicebus queue create --resource-group $RESOURCEGROUP --namespace-name $SERVICEBUS --name $QUEUE --enable-partitioning true

echo "GETTING CONNECTION STRING..."
CONNECTIONSTRING=$(az servicebus namespace authorization-rule keys list --resource-group $RESOURCEGROUP --namespace-name $SERVICEBUS --name RootManageSharedAccessKey --query primaryConnectionString --output tsv)

echo "CONNECTION STRING:"
echo $CONNECTIONSTRING

