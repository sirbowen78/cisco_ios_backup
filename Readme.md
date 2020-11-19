**Introduction**
<p>This python script exports the running config of Cisco IOS based routers. In order to use this script, 
the Cisco IOS must have the more command, the reason to use more instead of show is because more command will only show the actual content of the configuration file whereas show will add on</p>

>Building configuration...
>
>Current configuration : 1439 bytes

|python file| description|
|-----------|------------|
|config.py| changes these the rsa key path and config file destination path|
|ciscoios.py| Cisco router connection and export config to file.|
|filehandler.py| Reads CSV file and convert to dictionary, and also check if the destination directory exists|
|logger.py| Creates a logger to log what the script is doing.|
|start.py| Integrates all the python files to run the config file export operation|


**Cisco IOS configuration requirement**
<p>The script uses the RSA private key to login, the account has a privilege 15 hence it skips the requirement of enable secret.</p>
<p>The command lines example as follow, suppose the router is 192.168.1.1</p>

>config t
>
>ip domain-name cyruslab
>
>crypto key generate rsa modulus 4096
>
>username cyruslab privilege 15
>
>ip ssh pubkey-chain
>
>username cyruslab
>
>key-string
>
>copy and paste the rsa pub key content here.
>
>exit
>
>exit
>
>exit
>line vty 0 4
>
>login local
>
>transport input ssh
>
>end

**Usage**
<p>If you are satisfied with the default configuration in config.py then run the below, otherwise  adjust the parameters based on your environment.</p>
<p>You need to create a csv file from a notepad that has two columns: ip and username, each field must be separated by comma.</p>
<p>Using MS Excel to create CSV will cause the field to have non-UTF8 characters which will cause the csv parsing to fail, hence it is recommended to create from text editor.</p>

>python start.py
