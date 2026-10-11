**READ.MD**

====================================================================**MSFABRIC**================================================================================================================

=>A unified SaaS Product

*It unifies all the services required to perform any kind of operation in the world of data such as analytics, EDA(Exploratory Data Analysis), visualization and charts, Pipelines, Orchestration, Monitoring, streaming, Data Science, Machine-Learning models*



**=>Components:**

Data factory: Azure Data Factory

Data Engineering: PySpark or Spark Capabilities within Azure(Azure synapse spark)

Data Warehouse: Synapse Data warehouse

Data Science:

Real-Time Intelligence: Real stream analytics

Databases

Industry Solutions

PowerBI



**=>what will be the storage account we will be using here?**

OneLake or Fabric DataLake



As a azure dev. to create a DataLake(in Azure) we have to create different storage accounts, but in Fabric you just need to create one DataLake referred as OneLake



**Microsoft Purview** (similar to Azure Purview) which is data governance tool that take cares of data, resources, lineage, data transformations.



**Tenant:** top level of hierarchy that holds everything such as subscription users

**capacity:** A pool or bundle of resources such as computation, RAM, memory, storage that can be assigned to a resource. The size of the capacity determines the amount of computation power available.

**workspace** or container(similar to resource groups): A folder that carry all your resources or Microsoft fabric items.



\*\*SKUs(Stock Keeping Units)\*\*e.g.: F2, F4, F8, F16, F32, F64, F128, F256, F512, F1024, F2048, TRIAL(64))

@30:00 process for create azure account



This is my **business account:** akashraj@BRC12375.onmicrosoft.com **password:** @Aakash277

login to azure and then create a Microsoft entra id user and create a new user, that new user principal email will be used to create new fabric capacity or account for 60 days free trial

**password:** Bobby@12375

so we created fabric with F64 capacity/SKU via azure and in that particular F64 capacity you can have multiple workspaces or containers or resource groups



**Monitor Tab:** If you run your resources or pipelines, you can monitor everything you create: the pipelines, the failures

**Rel-Time Tab:** where you'll be creating your stream analytics and working with Data streaming

**Deployment Pipelines:** we currently used Azure DevOps but this one creates or simplifies or automates the whole process of CI/CD in different environments: Test, QA, Stage, Prod



**Manage access:**

Admin, Member, Contributor, Viewer



e.g.=> let's say you are using Databricks and you want to connect and read the data on Databricks from fabric. In that scenario I can allow the account associated with Databricks ws and you can create the role accordingly.



access to all the objects as per assigned roles of the particular workspace



**Contributor/Viewer**

build some SemanticModels, build powerbi reports

run some sql queries or do some analysis connect your Data warehouses DBs using SQL endpoints



**Settings>AdminPortal>CapacitySettngs>trial**

click on settings actions



Note: Fabric items not moved to a fabric capacity or a PowerBI Premium capacity within 7 days after your trial ends maybe permanently completed.





**ONELAKE or Fabric DataLake:** OneDrive for Data

=>whenever you create fabric capacity or tenant you automatically get OneLake storage account.

=>It is built on top of ADLS(Azure DataLake Storage) Gen 2(It is DataLake solution), aws(s3 buckets), google(Google cloud storage)

Fabric also eliminates the problem of:

=>why OneLake? **One DataLake**, logical DataLake: no need to maintain multiple storage accounts for different purpose

=>It can handle structured, semi-structured and Unstructured Data

**=>one copy of data:** Let's say multiple divisions such as Marketing, Finance, HR, Accounts and so on of a organization are trying to access some sales data so they will extract or create multiple copies of data, so there will be only **one copy of data** from onesource(OneLake per tenant)

**=>Data Redundancy - LRS, GRS, GZRS**
whenever we create storage account in azure, we have to pick one of the above data redundancy options, because that's how it stores the data in multiple copies and that's how the data is secured in azure datalake



It handles or stores all the structured(tabular) data in the Delta-Parquet file format automatically.



**Try It Yourself=> OneLake File explorer** for windows: similar as storage explorer for azure





**parquet file format:** columnar file format(used for big data processing because we fetch the data column by column instead of row by row)e.g. .csv, .json, .org, .avro



when the particular parquet file is wrapped in delta log(transaction log: that stores or carries all the transaction) it can be referred as **delta-parquet file format**.
=>delta log guarantees **ACID** transaction, indexing



ACID: Time Travel or Data Versions.



Data Serving in Fabric



Data Warehouse>> Data Lake

**Fabric Data WAREHOUSE vs Data WAREHOUSE:
?** A traditional data **WareHouse** is a datahub or central repo. of data(Historical or present)

=>Structured Data>ETL>Data Warehouses>BI or Reports

=>dimensional data model containing fact and dimension that we create in data warehouse.

=>Current **storage solutions** where we create dimensional data model in Data Engineering

=>GoogleBigQuery(Google), RedShift(AWS), Synapse(Azure), Snowflake(independent of cloud).

**=> How to create Fabric Data WAREHOUSE(Lake Centric Data Warehouse)**

**GoTo Workspace > New item > Click on Warehouse**

**warehouseUI:**

**Warehouse explorer**

**manage** schemas, security

**Queries:**

My queries, Shared queries

**create a sql query in my queries:**

**>>select 1 as columnn\_name**







**Data LAKEHOUSE:(Data Warehouse + DataLake)**

*storing the data in delta format, we can actually built the data warehouse on top of it*



=> *Data is actually stored in DataLake and can also be used to build the reports because of delta parquet file format and it supports all the functionalities require to eliminate the use of traditional data warehouse*



**Lakehouse VS Warehouse:** *Choose a **warehouse** when you need an enterprise-scale solution best suited for structured and semi-structured data while <b>lakehouse</b> can be used when you need a large repo. of highly unstructured data from heterogeneous sources such as APIs, low-cost object storage and want to use SPARK as your primary dev. tool. Acting as a lightweight data warehouse, you always may opt to use SQL endpoint \& T-SQL tools to deliver reporting and data intelligence scenarios.*



**=> How to create Fabric Data Lakehouse(Lake Centric Data Warehouse)**

**GoTo Workspace > New item > Click on Lakehouse**

**LakehouseUI:**

**Lakehouse explorer**

**Tables:**

**Files:**



**Storage URL**

ADLS has a container named raw and inside you have a folder or data named sales



**azure storage account:** abfss://raw@datalakeakash.dfs.core.windows.net/sales

**abfss:** protocol similar to https

**raw:** container

**sales:** Folder or file

**ABFS Path**

abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files

**abfss:** protocol similar to https

**akashKumarprows:** workspace or container

**akashlakehouse.Lakehouse/Files:** Lakehouse\_name.Lakehouse/Files







**KQL(Kusto-Query Language) Database:** We have used it in azure logs as **traces | search ""** querying for streaming data.











Multiple ways of doing **Data Ingestion in FABRIC:**

**Ingesting the data from multiple sources to OneLake**

**ETL(Extract-Transform-Load):**

**1)Pipeline** (similar to **Copy Activity** in azure which is a main activity used to perform in ADF to migrate the data from one source to another source )

**2)DataFlows**

**=>Gen1:** exactly same as ADF or synapse

**=>Gen2:** code free and even simpler than Gen1 as it uses the same UI as PowerQuery Editor

**3)Notebooks:** write the code in python, sql, Skala and R to do ETL

**4)EventStream:** where a source can be IOT hub and then you can perform ETL



**Shortcuts:**  *are the Objs that refers or points to a particular location which eliminates data movement.*

***e.g.=>*** *the creating of shortcut on Desktop for a game.exe file stored somewhere in your drives in your PC*











**Mirroring:** *It will create or replicate a mirror copy of your source data automatically and here you no need to apply complex ETL logic or no need to manage ETL Pipelines*

1. *DB Mirroring*

*2. Metadata Mirroring: It can help synchronizing metadata such as catalog names, schemas and tables*

*3. Open Mirroring*





# =========================FABRIC DATA FACTORY===============================





============================================================**Fabric Data factory:** Similar to Azure Data factory=============================================================================

Low/No code tool where you can use ETL/ELT and you can build pipelines.



**=> How to work with Fabric Data Factory**

**GoTo Workspace > New item > Click on Pipeline**

**Orchestrated:** in a sequence



click on pipeline activity>Copy data
A canvas will appear



**Activities under Fabric Data Factory:**

**Move \& transform**
*Copy data, Dataflow, Delete data*



**Metadata and validation**

**Lookup:** *Activity to read the data*



**Control flow**

*Notebook, Get metadata, , Script, Stored procedure and so on*



**Orchestrate:** *Run Pipeline within Pipeline*



**Transform:**





**if you hover on any activity you will see 4 nodes**

On skip, On success, On fail, On completion

**Orchestrated:** in a squence

**Copy data1** --------*On fail*------>**Lookup**------------*On success*------>**Copy data2**

\*\*=>\*\*Lookup will only run if Copy data1 fails to run and Copy data2 will only run if Lookup activity succeeds to run

\*\*=>\*\*Let's say if Copy data1 succeeds to run Lookup will be skipped and Copy data2 will also be skipped after it

\*\*=>\*\*Let's say if Copy data1 fails to run Lookup will run and if it fails Copy data2 will be skipped.





**SCENARIO 1: get single data file from API(github repo) and inject to lakehouse**



while clicking on any activity there will be a ***General,*** ***Source***<i>, **Destination, Mapping \& Settings.**</i>

&#x20;           **General
Name:** *Name of the activity*

**Description:**

**Activity state:** *Activated/Deactivated*

**Timeout:** *timeout range 0.00:10:00-7.00:00:00, Default: 0.12:00:00*

**Retry:**



&#x20;           **Source
Connection:** click on more to choose from a list of connectors to ingest the data ***similar to Get data feature***

**e.g.** for web api use Http or REST accordingly

Http

Connection settings:

Url: *Base\_Url(https://raw.githubusercontent.com/)if in Github the data is there click on raw and then copy the base url.*

Connection name: *Connection\_name(default selected to Base\_url)*

*Click connect*



*Connection will be showing now in source connection*

**Relative URL:** *Relative\_Url()*

**File format:** *DelimitedText(for csv)*

***Note:*** *Make sure to check Test connection and Preview data*





&#x20;           **Destination**

**Connection:** *add the lakehouse created earlier*

**Rootfolder:** *Tables/**Files***

**Filepath: Files > Create Directory within Files (say RawData) > File\_name**

**File format:**



*click on outside the activity anywhere in the canvas, **validate** it to see if there are any errors, <b>save</b> the activity and <b>run</b> the pipeline.*

*you will see the file will be pushed from source to destination i.e lakehouse and inside the lakehouse under the files section there will be a folder created RawData and inside that there will be your file*



**SCENARIO 2: get multiple data file from API(*github repo*) and inject to lakehouse(<i>Using Dynamic or parameterized pipeline</i>)**

&#x20;           **Parameters**

**Click on the canvas anywhere and set a new parameter:**

**Name:** rel\_url
**Type:** *String*

**Default value:** *Any one of the rel\_url*



while clicking on any activity there will be a ***General,*** ***Source***<i>, **Destination, Mapping \& Settings.**</i>

&#x20;           **General
Name:** *Name of the activity*   

**Description:** *Description of the activity*

**Activity state:** *Activated/Deactivated*

**Timeout:** *timeout range 0.00:10:00-7.00:00:00, Default: 0.12:00:00*

**Retry:**



&#x20;           **Source
Connection:** click on more to choose from a list of connectors to ingest the data ***similar to Get data feature***

**e.g.** for web api use Http or REST accordingly

Http

Connection settings:

Url: *Base\_Url(https://raw.githubusercontent.com/)if in Github the data is there click on raw and then copy the base url.*

Connection name: *Connection\_name(default selected to Base\_url)*

*Click connect*



*Connection will be showing now in source connection*

**Relative URL:** *Add dynamic content(a pipeline expression builder page will open)*

*Click on the rel\_url under Parameters section, a expression will be automatically put in the query tab. Click OK*

**File format:** *DelimitedText(for csv)*

***Note:*** *Make sure to check Test connection and Preview data*



&#x20;           **Destination**

**Connection:** *add the lakehouse created earlier*

**Rootfolder:** *Tables/**Files***

**Filepath: Files > Create Directory within Files (say RawData) > File\_name**

**File format:**



Until now we are hard coding the parameter, now we gonna use the parameter using *FOR EACH* loop, as we don't need to add the url manually again and again.

first we need to create a json file and upload json file in the lakehouse, create another sub folder(say Script) under Files

Now go back to pipeline:

add Lookup activity just before Copy data activity. Click on it:

&#x20;           **General**

**Name:**   *Name of the activity*



&#x20;           **Settings**

**Connection:** *add the lakehouse created earlier*

**Rootfolder:** *Tables/**Files***

**Filepath:** *Browse . json file in Script. click OK*

**Reursively:** *Check all the folders*

**File format**\*: JSON\*

**Note:** *Uncheck the First row only as that will return only first row of the file.*

*Disable Copy data to see the O/P of Lookup activity.*





*click on outside the activity anywhere in the canvas, **validate** it to see if there are any errors, <b>save</b> the activity and <b>run</b> the pipeline and check the O/P*



create and connect ForEach activity in middle of Lookup \& Copy data. Click on ForEach activity

**Lookup** --------*On Success*------>**ForEach**------------*On success*------>**Copy data**

&#x20;

&#x20;              **General**

**Name:** For All Files



&#x20;              **Settings**

**Sequential:** *check the box only if you wanna ingest files in a sequential manner*

**Items:** *Add dynamic content(a pipeline expression builder page will open). Click on the FileNames(Lookup activity O/P) under Activity outputs section, a expression will be automatically put in the query tab.*

*@activity('Lookup\_Activity\_O/P\_Name').output.value*

*We used .value as in the json file we have two keys wiz. count and value. so only value array.*

*Click OK.*

\*Now move the Copy data inside the ForEach activity Canvas.

now need to make some changes on the Copy data activity\*

&#x20;           **Source**

**Connection:**

**Relative URL:**  *Add dynamic content(a pipeline expression builder page will open).*

*@item().p\_rel\_url*

*Click OK*

&#x20;           **Destination**

**Connection:**

**File path:**    *Add dynamic content(a pipeline expression builder page will open).*

*since we want to create indepedent folder for each file inside the Files folder, RawData is just to add prefix for folderName:*

*RawData@{item().p\_sink\_folder}*

*Click OK*



**File name**: A*dd dynamic content(a pipeline expression builder page will open).*

*@item().p\_sink\_file*







*you will see the files will be pushed from source to destination i.e lakehouse and inside the lakehouse under the files section there will be an independent folder created for each file.*





**SCENARIO 3: After completion of scenario 2 only, get single data file from ADLS Gen 2 inject to lakehouse as well. Concept of Parent and child pipelines**

**Since Azure subscription was expired follow scenariao 1 and upload returns file from GitHub to lakehouse.**



**creating and ADLS and injecting source thing:**

Go to Azure:

go to storage account > +create

**Subscription**: need subscription to use

**Resource group:** Fabric



**Instance details**

**Storage account name: fabricdatalakeakash**

**Region:**

**Primary service:**

**Redundancy: LRS(as it is cheaper)**



*Note: Right now it is not a Datalake, it is just a blob storage, in order to create a datalake, just click next and click on enable hierarchical namespace, as in this we can create folders within folders, but in blob storage we can't do the same. Now Click Review+Create.after few seconds of validation and click create.*

*Your Datalake will be deployed under that particular resource group.*

*Once Your deployment is complete.*

*Click Go to resource*

*Go to containers under Data storage > create a container > Name it(say raw) > click create*

*go inside created container raw > upload a file (say csv)*



***Ques: How can fabric read the data from a secured azure storage account***

*Ans: With RBAC(Role based access control) we need to add/assign the email account and allow it to be read from fabric*



*Go to the recently created resource group > click on storage account > click on Access Control(IAM) > Click Add role*

***Role***

*click on Storage Blob Data Contributor and click next*

**Members**

**Assign access to:** User, group or service principal(only if fabric was created in same azure entra id or just copy the fabric account email)

**Members:** Add member and select the fabric email

**Review + assign: Click on it** *(Added Role assignment)*











while clicking on any Copy activity there will be a ***General,*** ***Source***<i>, **Destination, Mapping \& Settings.**</i>

&#x20;           **General
Name:** *Name of the activity(Copy ADLS Data)*

**Description:**

**Activity state:** *Activated/Deactivated*

**Timeout:** *timeout range 0.00:10:00-7.00:00:00, Default: 0.12:00:00*

**Retry:**



&#x20;           **Source
Connection:** click on more to choose from a list of connectors to ingest the data ***similar to Get data feature***

**say ADLS Gen2**

Connection settings:

**Url:** *Base\_Url(fetch this from Azure storage account > Settings > Endpoints > copy the Data Lake Storage and paste it here)*

**Connection name:** *Connection\_name(say adls\_conn)*

***Authentication kind:*** *Organizational account*

*Click connect*

*Connection will be showing now in source connection*

**FiLe path:** *browse source as we created raw container and uploaded the file in adls and click OK*

**File format:** *DelimitedText(for csv)*

***Note:*** *Make sure to check Test connection and Preview data*





&#x20;           **Destination**

**Connection:** *add the lakehouse created earlier*

**Rootfolder:** *Tables/**Files***

**Filepath: Files > Create Directory within Files (say RawDataADLS) > File\_name**

**File format: csv**



*click on outside the activity anywhere in the canvas, **validate** it to see if there are any errors, <b>save</b> the activity and <b>run</b> the pipeline\_2.*

*you will see the file will be pushed from source to destination i.e lakehouse and inside the lakehouse under the files section there will be a folder created RawDataADLS and inside that there will be your file.*





**SCENARIO 4: Dataflow Gen2 and transformation(Performing ETL as it is similar to power query editor)**



**once inside the canvas:**

Go to Get Data:

and select lakehouse and gather the product categories and subcategories file and create one by one and once create it will load.

click on the table link in the content column after loading. that will extract the table and actual data.





Note:

merge the file do the transformation

write the data to detination(let's say lakehouse) by adding data destination

add connection, click next

select the workspace/container and name the table as that's gonna create a table for us in destination in table(s) folder.

make sure to look at the **column mapping** as columns with **ANY** data type will not push to destination. publish/save the flow







create anpther pipeline say tutorial\_3, inside it create Dataflow







while clicking on any Dataflow there will be a ***General \& Settings.***

&#x20;           **General
Name:** *Name of the activity(DataflowJoin)*

**Description:**

**Activity state:** *Activated/Deactivated*

**Timeout:** *timeout range 0.00:10:00-7.00:00:00, Default: 0.12:00:00*

**Retry:**



&#x20;           **Settings
Workspace:** add the workspace



**Dataflow:** add the created dataflow Gen2





validate it, save it and run the tutorial\_3 pipeline. you can see the transformed table in your tables folder





**Create the parent\_pipeline**



**add 3 Invoke Pipeline(s) inside it**



&#x20;**General
Name:** *Name of the activity(say tutorial\_1, tutorial\_2, tutorial\_3)*

**Description:**

**Activity state:** *Activated/Deactivated*



&#x20;           **Settings**

**Type: Fabric
Connection:** *Fabric data Pipelines(sign in and connect)*



**Workspace:** add the workspace

**Pipeline:** select all the child pipelines created in separate invoke pipeline activities



**make sure to check the Wait on completion box**

validate it, save it and run the **parent\_pipeline.**



**What this will do?**



**tutorial\_1(child pipeline) :** *pull data dynamically from GitHub to lakehouse*

**tutorial\_2(child pipeline) :** *pull data from ADLS to lakehouse (although we have created another static git pipeline from returns file)*

**tutorial\_3(child pipeline) :** *transformation using dataflow gen2*





once the data gets loaded into lakehouse from child pipelines tutorial\_1 and tutorial\_2. from there we have transformed the data using dataflow gen2 using tutorial\_3 pipeline.



here we have created an ELT pipeline cause we have extracted and loaded in tutorial\_1 and tutorial\_2 and then on the top of both we have done the transformation. because since data is so heavy we can't do the transformation before loading





#### **Notifications(logic apps in case of ADF):**

###### what if i want to get the notification or email for any kind of pipeline failure

add a **Office 365 Outlook**

connect to the activity with the pipeline *on failure* or *on skip. and add the outlook account by signing in.*





#### **Triggers(logic apps in case of ADF):**

###### trigger or schedule the pipeline automatically

Add trigger in pipeline

a set alert popup will appear





**types of triggers in ADF:**

schedule triggers

tumbling window triggers

storage events triggers





# =========================FABRIC DATA ENGINEERING=================================





In here we are more inclined towards lakehouse, spark notebooks, pyspark transformations





*performance tuning*

*optimization using commands V-Orderby, merse statement*





In your workspace create a notebookfrom new item



write code and run the session gonna start in few second and the output will displayed. the connect option at above will turn to standard session and the green dot shows that the connection or s=the session is live.



* **Standard session**

New standard session

New high concurrency session: if you want to process large amount of data



Attach the lakehouse or warehouse from OneLake catalog



there will be two lakehouse, one will be without schema and one with schema



get the one without schema



**note: Stop current session** whenever we change the lakehouse connection, we need to restart the connection



*set the file as markup file to use HTML elements*





**Data Wrangler:** *transform your code from pandas to pysparks*

**Note:** *either you can **manually change** the language via <b>dropdown</b> or use*  %%html, %%sql to switch



**=> Reading data from files folder**

click on the three dots on the file from files folder and load data through Spark and run the loaded code



df = spark.read.format("csv").option("header","true").load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files/RawData")

\# df now is a Spark DataFrame containing CSV data from "Files/RawData/AdventureWorks\_Returns.csv". Also you can use ABFS path

display(df)



**How to load files in to tables folder from Files folder?**

Either you can use spark or you can go to your Lakehouse and click on the file to use *Load to Tables* feature. It will not just load the table but convert the file into delta parquet format.







**=> Reading data from Tables folder**

click on the three dots on the file from Tables folder and load data through Spark and run the loaded code



df = spark.sql("SELECT \* FROM akashlakehouse.returnstable LIMIT 1000")

display(df)





**Shortcuts:**  *are the Objs that refers or points to a particular location which eliminates data movement. the location that a shortcut points to is known as the target path of the shortcut while the location where the shortcuts appear is known as the shortcut path.*



**Note:**  keep in mind that there should be only one level of hierarchy in Tables folder unlike Files folder





&#x20;

**creating Shortcuts (Query the data)**





**use sql to query this you need to specify the lakehouse before the shortcut\_name**



go to lakehouse right click on files folder and create new shortcut for RawDataADLS(AzureDataLake storage). a shortcut wizard will open. click on ADLS gen2 in this case. after creating the shortcut, a shotcut will be appear at the bottomin the files folder with adls in azure.



**Note:** *let's say you have 8 PB( 8000 TB ) data sitting in azure, you won't transfer the files in lakehouse as that will cost soo much pricing and so much computation and cost, so we can create a shortcut that will point to the particular location in azure where your data is sitting.*





**Internal Shortcut**



**Medallion Architecture:** *Bronze, Silver, Gold Layer*

*first lakehouse*\*(Bronze Layer)\*\* where you will just dump the data\*

*Second/Silver lakehouse*\*(Silver Layer)\*\*\* where you will have processed or transformed data

Third\*/\*Gold *lakehouse*\***(Gold Layer)**





*create a new lakehouse named lakehousesilver(just for naming convention) and create a shortcut by clicking on Files folder. Click on Internal sources(say Microsoft OneLake).*

*Click on your lakehouse(Bronze or first one). go to Files and connect to any folder. Click next and create. An internal shortcut is created in silver layer connecting to your bronze layer.*





***Scenario 5: read all the folder and csv files from bronze lakehouse do all the transformation and push it to silverlakehouse.***



**What is the advantage of attaching the lakehouse?**

If we attach the lakehouse, we don't need to add the full url(say abfss path), because it treats it as a local lakehouse, so we can just use the file semantics("path", "Files/....)

&#x20;



***Q. Reading files from local lakehouse(which is attached say silverlakehouse)***



**# \*\*Reading Shortcut\*\***



*df = spark.read.format("csv").option("header","true").load("Files/RawDataAdventureWorks\_Customers/AdventureWorks\_Customers.csv")*

*display(df)*



**POINTS TO REMEMBER:**

* **spark.read:** batched data
* **spark.readstream:** stream data
* **option("header","true"):** promote first row as headers
* df now is a Spark DataFrame containing CSV data from "Files/RawDataAdventureWorks\_Customers/AdventureWorks\_Customers.csv".
* ***df1.printSchema():*** will display schema structure of loaded file
* ***display(df):*** to print the dataframe







***Q. Reading files from External lakehouse(say bronzelakehouse)***



**# \*\*Reading bronze Lakehouse Data\*\***

**\*\*Reading Customers Data and Applying Transformations. WRITE the data at the end.\*\***

*df1 = spark.read.format("csv")\\*

&#x20;           *.option("header", True)\\*

&#x20;           *.option("inferSchema", True)\\*

&#x20;           *.load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files/RawDataAdventureWorks\_Customers")*



*df1.printSchema()*

*display(df1)*



**POINTS TO REMEMBER:**

* ***.option("inferSchema", True):*** will predict the best possible schema for the loaded data
* ***printSchema():*** It reads all the data as string column by default in csv if you don't use *.option("inferSchema", True)*
* use backslash(/) to go to next line



* ***spark.read* =** spark reader API







**\*\*add new column named FullName that will contain the values combining prefix, firstname and lastname\*\***



*df1 = df1.withColumn("fullname", concat(col('prefix'), lit(" "), col('FirstName'), lit(" "), col('LastName')))*

*display(df1)*



**POINTS TO REMEMBER:**

* **Import packages:** In order to use any function we need to import libraries.

*from pyspark.sql.functions import \**

*from pyspark.sql.types import \**

* We have to create a new dataframe as we can't make changes in the existing dataframe, the naming will be same but we need to refer it to make changes. we need to re-write it with same name.
* ***withColumn*:** to create a new column or transform a column. If we are using the existing column name it will apply transformation else it will create a new column.
* ***lit(" ")***<i>: to use a constant such as space</i>









**\*\*create a new column domain \& extract the domain from email address\*\***



*df1 = df1.withColumn("domain", split("EmailAddress", "@")\[1])*

*display(df1)*





**POINTS TO REMEMBER:**

***split("EmailAddress", "@")\[1]:*** split the *EmailAddress* values with delimeter @. let's say akashraj1179@gmail.com where akashraj1179 and gmail.com will be considered as values in a array where \[0] is akashraj1179 and \[1] is gmail.com. domain is not an existing column so the transformation will be applied in a newly created column named domain.







**\*\*write the data\*\***





*df1.write.format("delta")\\*

&#x20;           *.mode("append")\\*

&#x20;           *.option("path", "Files/customers")\\*

&#x20;           *.saveAsTable("customers")*



*df1.write.format("delta")\\*

&#x20;           *.mode("append")\\*

&#x20;           *.saveAsTable("customers2)*



Note:

* *here we specified the path, so customers file in table will be of **external** type, while if we comment the 3rd line in above query, the customers2 file in table will be of <b>managed</b> type as* we haven't specified the path, and it will contain the data unlike in external type data will be sitting in Files folder.
* if in tables folder you can see the delta log file for the particular table that means it is a managed table but if you are not able to see delta log file for table sitting in table folder that means it is an external table as your delta files will be sitting in files folder





*df1.write.format("delta")\\*

&#x20;           *.mode("append")\\*

&#x20;           *.option("path", "Tables/customers3")\\*

&#x20;           *.saveAsTable("customers3")*





**POINTS TO REMEMBER:**

* ***spark.write* =** spark writer API
* as we applying these transformations we better save the file as delta parquet format
* **Types of modes:**

Append

Overwrite

Error

Ignore







**\*\*Reading Sales Data and Applying Transformations such as UNION. WRITE the data at the end.\*\***



*dff1 = spark.read.format("csv")\\*

&#x20;           *.option("header", True)\\*

&#x20;           *.option("inferSchema", True)\\*

&#x20;           *.load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files/RawDataAdventureWorks\_Sales\_2016")*

*dff2 = spark.read.format("csv")\\*

&#x20;           *.option("header", True)\\*

&#x20;           *.option("inferSchema", True)\\*

&#x20;           *.load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files/RawDataAdventureWorks\_Sales\_2017")*



*df2 = dff1.union(dff2)*

*display(df2)*





*df2.write.format("delta")\\*

&#x20;           *.mode("append")\\*

&#x20;           *.option("path", "Files/sales")\\*

&#x20;           *.saveAsTable("sales")*









**\*\*Reading Cat \& Subcat Data and Applying Transformations such as UNION. WRITE the data at the end.\*\***

**Note:** we already merged the category and subcategory table earlier in one of the chapter



*df3 = spark.read.format("delta")\\*

&#x20;       *.load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Tables/Merge")*

*display(df3)*







*df3.write.format("delta")\\*

&#x20;           *.mode("append")\\*

&#x20;           *.option("path", "Files/subcat")\\*

&#x20;           *.saveAsTable("subcat")*





**\*\*Reading Calendar Data and Applying Transformations. WRITE the data at the end.\*\***





*df4 = spark.read.format("csv")\\*

&#x20;           *.option("header", True)\\*

&#x20;           *.option("inferSchema", True)\\*

&#x20;           *.load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files/RawDataAdventureWorks\_Calendar")*







*display(df4)*



*df4.write.format("delta")\\*

&#x20;           *.mode("append")\\*

&#x20;           *.option("path", "Files/calendar")\\*

&#x20;           *.saveAsTable("calendar")*







**\*\*Reading Products Data and Applying Transformations. WRITE the data at the end.\*\***





*df5 = spark.read.format("csv")\\*

&#x20;           *.option("header", True)\\*

&#x20;           *.option("inferSchema", True)\\*

&#x20;           *.load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files/RawDataAdventureWorks\_Products")*



*display(df5)*





*df5 = df5.withColumn("ProductSKU", split("ProductSKU", "-")\[0])*

*display(df5)*





*df5.write.format("delta")\\*

&#x20;           *.mode("append")\\*

&#x20;           *.option("path", "Files/products")\\*

&#x20;           *.saveAsTable("products")*



**POINTS TO REMEMBER:**

***split("ProductSKU", "-")\[0]:*** split the *ProductSKU* values with delimeter *-*. let's say *CA-1098* where *CA* and *1098* will be considered as values in a array where \[0] is *CA* and \[1] is *1098*. *ProductSKU* is an existing column so the transformation will be applied in *the same* existing column







**\*\*Reading Returns Data and Applying Transformations. WRITE the data at the end.\*\***



*df6 = spark.read.format("csv")\\*

&#x20;           *.option("header", True)\\*

&#x20;           *.option("inferSchema", True)\\*

&#x20;           *.load("abfss://akashKumarprows@onelake.dfs.fabric.microsoft.com/akashlakehouse.Lakehouse/Files/RawData")*



*display(df6)*



*df6.write.format("csv")\\*

&#x20;       *.mode("append")\\*

&#x20;       *.option("path", "Files/returns")\\*

&#x20;       *.saveAsTable("returns")*



Note: If it's a managed table,by default it will always be stored in delta parquet format, while in external table you can choose to store in the format you want either csv or delta format







***Maintenance***



Click on 3 dot on any of the table present in tables folder in silver lakehouse> go to maintenance >



***optimize command***<i>(auto enabled now)</i>

coalesce

promote better query performance



***vaccum commmand***

when we delete some data in delta lake





**Microsoft Spark Utilities(MSSparkUtils)**

It is a built-in package to help us perform common tasks to work with file systems, to get environment variables, to chain notebooks together \& to work with secrets.



**How to import:**



*from notebookutils import mssparkutils*



**How to read the content of directory**

*mssparkutils.fs.ls("Files")*





**How to create a new directory**

*mssparkutils.fs.mkdirs("Files/mkdir")*





**How to copy files from one folder to another**

*mssparkutils.fs.cp("Files/calendar", "Files/mkdir", True)*





# =========================FABRIC DATA WAREHOUSE===================================



creating a gold layer in the data warehousing section. create the tables in the gold layer







**Hierarchy of a schema**

at the top we have data warehouse, under that we have schemas that act as a layer and here we gonna create a **gold layer** schema as our next course of action









**for query data we use 3-name convention:** *entity.schema.table*

e.g. *lakehouse\_name.schema\_name.table\_name, warehouse\_name.schema\_name.table\_name*







**Right click on schema or click on 3 dot menu on schema and create a new schema, the create schema query will load**



*CREATE SCHEMA SCHEMA\_NAME*

*GO*



**The above query will create objects such as Tables, Views, Functions, Stored Procedures after running.**



**Right click on table or click on 3 dot menu on table and create a new table, the create table query will load**



*CREATE TABLE akashwarehouseakash.gold.firsttable*

*(*

*id int NOT NULL*

*name varchar(100)*

*salary int*

*)*

*GO(this is optional)*



**Insert record in the created table**



*insert into akashwarehouseakash.gold.firsttable values(1, 'xyz', 100)*



**Retrieve the data**



*select \* from akashwarehouseakash.gold.firsttable*







**Cross Data Warehouse Queries**



* You can query data between two Warehouses.
* You can query data in a warehouse from another lakehouse as well just the pre-requisite is we can only query those tables which are managed tables.







**Querying data from lakehouse:**



*select \* from lakehouse\_name.schema\_name.table\_name*









**query the list of schemas and tables**

*SELECT TABLE\_SCHEMA, TABLE\_NAME*

*FROM akashlakehousesilver.INFORMATION\_SCHEMA.TABLES;*



**Create table with two different ways:**

create command

CTAS: CREATE TABLES AS SELECT





**Note:** since every table in lakehouse is external table, we need to create managed tables by clicking on every folder in Files and load to tables and load new table. here we will create managed table for each subfolder. add name and select filetypes as say parquet or csv

csv file gonna have issue because of first row not coming as headers so we need to create the table manually.



**create sales table(backup or duplicate or copy data) using CTAS in gold layer schema from lakehouse**

*create table akashwarehouseakash.gold.sales as select \* from akashlakehousesilver.dbo.sales\_man*



**drop the table**

*drop table akashwarehouseakash.gold.sales*





**create fact and dim tables(backup or duplicate or copy data) using CTAS in gold layer schema from lakehouse**



*create table akashwarehouseakash.gold.fact\_sales as select \* from akashlakehousesilver.dbo.sales\_man*

*create table akashwarehouseakash.gold.dim\_customers as select \* from akashlakehousesilver.dbo.customers2*

*create table akashwarehouseakash.gold.dim\_products as select \* from akashlakehousesilver.dbo.products\_man*

*create table akashwarehouseakash.gold.dim\_calendar as select \* from akashlakehousesilver.dbo.calendar\_man*







**Dimensional Data Modelling**

* STAR SCHEMA: there is no hierarchy between dimension i.e. no dimension in directly connected to any other dimension. It's easier to manage and most widely used.
* SNOWFLAKE SCHEMA:  There will be hierarchy between dimensions.



**Types of dimensions as in slowly changing dimension(SCD)**

1. TYPE-1(UPSERT)
UPSERT: UPDATE(if existing record) + INSERT(if new record)
2. TYPE-2: HISTORY, We create slowly changing dimension to track history using Eff\_StartDate, Eff\_ExpDate and InUSE(Flag columns wether the record is in use or not)
3. TYPE-3: Prev Value





We create slowly changing dimension to track history





**VIEWS:** are aggregated queries or stored queries used by managers or DAs

Note: while create/alter view no need to specify db\_name/warehouse\_name except select







**VISUAL QUERY EDITOR**

analyze data in sql without using sql.

using power query editor n the top of sql



* so we can insert table into canvas and transform data in a power query editor.
* we can view sql query for those transformation.
* we can store those transformation sql script as a view
* Use visualize results for visualization like power BI





as we need to create tables in warehouse

1. using ETL, picking the data from one place and pushing the data to data warehouse
2. using T-SQL







**How to create a managed table?**
just ignore the location .option("path) part







# =========================FABRIC DATA SCIENCE=====================================



















creating an ml model from workspace > new item







click on start with a template where data science queries will load for a template.

FYI, It takes a lot of time to build a model, train a model, test the model, get a score for that model







TYPES of model:

**BINARY CLASSIFICATION:** dealing with TRUE/FALSE or 0/1 condition



deciding the result on the basis of information. X as Category column Y as Decision column







**MULTI-CLASS CLASSIFICATION:** clustering

predict which category data will fall into(three or more categories





**REGRESSION:** predict a numeric value





**FORECASTING:** predict future values from past data





**DATA WRANGLER**

it will be enabled only when you start the session by running queries in ML model notebooks



Data transformation buddy, generate the Pyspark code for us similar to visual query editor









# =========================FABRIC DATA GOVERNANCE============================





&#x20;







fabric has capability to track the lineage of whole workspace

**Lineage View:** go to lineage view beside the list view at top left area in your workspace







whenever we create a Lakehouse we get a default semantic model alongside it.





**Endorsement:** It is a fabric \& PBI feature that makes it easier for users in an organization to find high quality trust worthy content and data.

where we can generate or create more trust among the developers.



**types of badges:**



**Promoted:** item creators think the item is ready for sharing and reuse



**Certified:** one level up than promoted. an authorized reviewer has certified that the item meets the organizations quality standards



**master data:** source of truth. we have to trust this. can only be applied to items that contain data such as Lakehouses and semantic models. only fabric administrator can label data items as master data









**Domains:**

let's say we have 10 workspaces, 4 of them will be finance domain, 4 of them will be HR and 2 will be marketing



created domains to group the workspace to manage the workspace easily. It is just adding the layer of hierarchy to workspaces











FABRIC Deployment PIPELINES(easy compared to AZURE devops CI/CD)



Dev--Testing/QA/QualityAssurance--UAT





no need:

to build release pipelines in CI/CD

to care of YAML Scripts





**Semantic model**

**model view**

**advantage:**

**all the tables, dax, relationships formula**

fyi, you can disable/enable the settings to put table into semantic model





**DIRECTLAKE in FABRIC(new mode):** combination of both mode(first it directly connects with your deltalake not lakehouse and only bring on demand data and latest version of data from metadata in the delatalog. The limitation is while u apply RLS it will go through lakehouse which was skipped during import means whenever we use RLS to data lakehouse, it doesnot use directlake but directquery. 



primarily there were two modes:

**Direct Query(returns the real time)** and **import mode(Data loaded in powerBI memory)**





Note:

Whenever we talk about Lakehouse, we mean delta files









================================================================================FABRIC DATA PIELINES=======================================================================================























even though we set parquet in destination but the files stored in raw folder in Files folder are of csv type, because

in file path: raw/@item(), where item value is bookings.csv, rooms.csv, hotels.csv where we are specifying that we want csv data. so we need to change the array



Parameters:

default value: 



\[{"file": "bookings", "key": \["booking\_id"]},

{"file": "rooms", "key": \["room\_id"]},

{"file": "hotels", "key": \["hotel\_id"]}]



**ERROR CODE:** 



**MappingColumnNameNotFoundInSourceFile**

don't enable mapping, because copy data activity will try to map the schema with the files everytime which isn't true and when we ingest the data with multiple files usually we don't perform mapping at all except some scenarios such as dynamic schema mapping





steps to resolve:

reset the mapping and delete every mapped column.





**2015**





**HttpRequestFailedWithClientError**

check the url of the file in the source of the activity



**UserErrorInvalidValueInPayload**



check the default value of parameters

where keys should be added as a list with. so in order to call multiple column as UPSERT, you have to pass a list of columns, we have to convert the primary key as list



**ADLSGen2ForbiddenError**

It takes some 10-15 minutes to create the storage account. so wait for some time to again test the connection





**DelimitedTextBadDataDetected**


in lookup activity, in settings file format might be not the correct one.



============================================================END of FABRIC==================================================================================================================



**=========================================================AI TUTORIAL FOR DATA DOMAIN:======================================================================================================**

AI AGENTs vs AGENTIC AIs:



**AI AGENTs:** 



AGENTIC AIs \& **FRAMEWORKS(kind of a module or SDK or package)**







**AI**  

* **LLM (Large Language Models)**              
* **Prompt Engineering**
* **RAG**







**LLM**               

* **No DL needed**
* **API Call**
* **How LLM Generates: LLM Architecture or Transformers**







**API Call**

* **OpenAI**
* **Claude** 
* **Gemini**







**#LLMs(Large Language Models)**



LLM is language model trained on large corpus of data where language model is kind of an application that predicts the next word/token.





P(next\_word/context)



before LLM(around 2022), we used statistical techniques







**biagrams:** lets say: cat will sit on \_\_\_\_\_\_\_\_ => cat will, sit on, \_\_\_\_\_\_\_\_\_

**RNN(2nd iteration):** neural network: only ML engineers were able to work with this, as it was complex to debug, understand, to create NN, it required a separate and specific domain for this

**LLM era(3rd iteration)** => work with **transformer** architeture(backbone of LLM) => chatgpt(openAI), Gemini(google), anthropic

all these companies created the LLMs for us consumers to use. The NN is still there as we still need fine tuning. but it has replaced the traditional RNN.





**Transformers**













go to vs code open the project, create the virtual environment in python

pip venv .venv



or 



pip install uv

Note: uv is modern python package manager which is very fast built on top of rust





if there is a path issue as window can't find location

&#x20;instead uv --vesion use python -m uv --version

&#x20;instead uv init use python -m uv init

&#x20;instead uv sync use python -m uv sync//sync all of the dependencies and it will create a virtual environment for user



via .python-version file you can use any version of python just edit the version and make sure the version is installed in your system.





whatever dependencies you will add in .tom file it will add those libraries.it will sync whole project with this toml file .toml file is the brain of the project









create env file as we are working with APIs, whenever we want to use API Keys, we should never hardcode those API keys and we should never store those API keys in python file or text file. 

always use .env file



creating an open ai api key



sk-proj-y\_-THR4cxdaZVR2S1b9X1X46N40jpqKZ87Ghx6g\_tDZrj6b1o3SNq7e590nZ86Ps04Xx\_IiD9tT3BlbkFJaFJ3xaZlsGcbXV6r41uXzhdqjuNvYXzOoOsdMIU18W4ecD3SvG5SH8wJKnmYEQ8l9CQVPs97YA



================================================================================LANGCHAIN===================================================================================================





AI AGENTs vs AGENTIC AIs:



**AI AGENTs:**



AGENTIC AIs \& **FRAMEWORKS(kind of a module or SDK or package)**































