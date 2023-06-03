
### Cost-effective architecture for web app and function
	
### Student provides a README that includes a short explanation and reasoning of the architecture selected for both the Azure web app and the Azure function in terms of cost-effectiveness

- The cost-effectiveness of the web app and the function app is a result of the affordable prices of these services. You'll see the price increase if you try operating these services on-site.

- The web application is scalable since it can handle high volumes of user data and peak usage at particular periods, i.e. close to the registration deadline.

- Because notifications are transmitted asynchronously over a Service Bus rather than synchronously, which may result in HTTP timeout problems when there are too many guests to be alerted, the function app    that handles notifications is scalable.

### Predict the monthly cost of each Azure Resource

### Student provides a README that includes a monthly cost analysis of the project detailing each resource’s cost

- Cost analysis is done on Testing/Development level environment. Such environment will not be responsive and also will not withstand much load. Hence, it is always recommended to use production level environment for deployment.

- Testing/Development level enviroment analysis:

| RESOURCE TYPE                        | RESOURCE NAME             | TIER                                        | MONTHLY COST |
|--------------------------------------|---------------------------|---------------------------------------------|--------------|
| Function App                         | udacityproject3	   | Consumption                                 | $0           |
| Azure Service Bus                    | rameez                    | Basic                                       | $0.05        |
| Azure Database for PostgreSQL server | rameezdatabase            | Basic Gen5 1                                | $34.14       |
| Storage account                      | udacityappstorage         | Standard/Hot StorageV2 (general purpose v2) | $19.00       |
| App Service                          | TECHCONF2022              | F1: Free                                    | $0           |

Total monthly cost:

0 + 0.05 + 34.14 + 19.00 + 0 = $53.64

- production level enviroment analysis:

| RESOURCE TYPE                        | RESOURCE NAME             | TIER                                        | MONTHLY COST |
|--------------------------------------|---------------------------|---------------------------------------------|--------------|
| Function App                         | udacityproject3           | Consumption                                 | $0           |
| Azure Service Bus                    | rameez                    | Standard                                    | $9.81        |
| Azure Database for PostgreSQL server | rameezdatabase            | Gen 5, 8 vCore                              | $136.55      |
| Storage account                      | udacityappstorage         | Standard/Hot StorageV2 (general purpose v2) | $19.00       |
| App Service                          | TECHCONF2022              | Basic                                       | $68.62       |
| SendGrid                             | rameez.iqbal@lineview.com | Pro                                         | $89.95       |

Total monthly cost:

0 + 9.81 + 136.55 + 19.00 + 68.62 + 89.95 = $323.93

In doing this cost study, I utilised the price calculator:

https://azure.microsoft.com/en-in/pricing/calculator/


