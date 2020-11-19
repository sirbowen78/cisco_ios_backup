**Introduction**
<p>This python script exports the running config of Cisco IOS based routers. In order to use this script, 
the Cisco IOS must have the more command, the reason to use more instead of show is because more command will only show the actual content of the configuration file whereas show will add on</p>

>Building configuration...
>
>Current configuration : 1439 bytes

|python file| description|
|-----------|------------|
|config.py| changes the rsa key absolute path and config file destination path|
|ciscoios.py| Cisco router connection and export config to file.|
|filehandler.py| Reads CSV file and convert to dictionary, and also check if the destination directory exists|
|logger.py| Creates a logger to log what the script is doing.|
|start.py| Integrates all the python files to run the config file export operation|


**Cisco IOS configuration requirement**
<p>The script uses the RSA private key to login, the account has a privilege 15 hence it skips the requirement of enable secret.</p>
<p>The command lines example as follow:</p>

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
>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCdQfl0Sz4Imz+Y01iLxiq0w8hezKdx4zG1
Of9Aaur2DateLcvzMt/Bw6Ds00+xKrUgxVjRc5SBEDZQu7EFeZp4B6PQOpT5p4gO3M8XARun
grXWGPsNlKWNqsTA4katRPivCpxeH0xPwRQ29UqdXXztwTzColFxCJ7GbTdWsGNOKn5Syo8B
Stsa75fWyzRhBV4xynQ5TKxnaVEUefcKv9t/eJWYBycnAzZIUb9NLz0/5h9eZn+OZspYzGbQ
UhDlhXTXZFzffDAMWyv+sasFBR24CIzB9UeTY6TBoUvq7uT8Ja8ZjiNofm/0/q5cGZ5GrhMt
LgDD0kFWrxyk55mHvmF+Kqk0iIo0OvnYRipRTjFxeK8xfgu76kJNHkzEKjlvHpuF48yhNwbs
gmhmiJSQrYzoFlXO467o8NQsiqcvsbTAED/PKFvpE9IedUWHypz+6h255a0UZkKKNP4u5oS7
+NQMu1aNG63QbCwqtMfs8kYLMnxNRYyTf1fs/EiVcdUx7JZeh1+EOk+Ll5VHq/dWIIPQyJi3
algaiY0AeNfNI4bArNuA0hB+2OQIQ0M6E0yuBH4avcCsomU56bEafwd2aH5E2nMsoG45pfWQ
L+owonhFOiDyn0dyaXjbUXRM5h4Cm2fSN1HgI07JwJCBWCR8O9JxYB7ZyDqw3dhjXmn+eLSJ
bQ== User@cyruslab
>
>exit
>
>exit
>
>exit
>
>
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
