# Cowork-User-Permission-Proto
A Django cowork user prototype application which handles information of users and their login, logout, and permissions. 

## Dependencies
1. Python 2.7+
2. `pip`
3. `virtualvenv`

## Instuctions
1. Run this command `sudo apt-get install python-mysqldb`

2. Set `DATABASE_URL=mysql://USERNAME:PASSWORD@HOST:PORT(By default 3306)/DATABASE_NAME` environment variable in your `.bashrc`, `.zshrc` or whichever shell you are using.

3. Install all python dependencies
    ```bash
        $ pip install -r requirements.txt
    ```

4. Run project
    ```bash
        $ cd CoworkTesting
        $ python manage.py runserver
    ```
