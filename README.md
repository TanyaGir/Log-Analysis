# Log-Analysis

## Project Description

In this project we have to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Geting started

### You must have the following software installed

    1.Virtual Machine - Vagrant

    2.Python 3

### Run Project:

    1.Download or Clone the following [full-stack nanodegree](https://github.com/udacity/fullstack-nanodegree-vm) and place into a desired folder on your local machine.

    2.Download the data, unzip and place the file newsdata.sql into the directory containing the files above.

    3.Start and successfully log into the the Linux-based virtual machine (VM) in the folder containing the Vagrant file with the instructions below.

### Launch the Virtual Machine

    1.Start the Vagrant VM inside Vagrant sub-directory in the fullstack-nanodegree-vm repository with:
    
    $ vagrant up   
    
    2.Log in with :
    
    $ vagrant ssh
    
    3. Go to relevant directory  cd /vagrant and ls. 
   
   ### Download and create the follwing views:
   
   1.Load the data in local database using the command:
    
       psql -d news -f newsdata.sql
       
     -psql — the PostgreSQL command line program
     -d news — connect to the database named news which has been set up for you
     -f newsdata.sql — run the SQL statements in the file newsdata.sql
     
   There are the 3 tables in the database:
   
   * The authors table includes information about the authors of articles.
   * The articles table includes the articles themselves.
   * The log table includes one entry for each time a user has accessed the site.
   
   Create the following views
   
   ```
    create view logviews as
    select articles.author , count(*) as view
    from log, articles
    where articles.slug = substring (log.path , 10)
    group by articles.author;
    
   ``` 
   ```
    create view totals2 as
    select DATE_TRUNC('day',time) as day, count(*) as totals
    from log
    group by DATE_TRUNC ('day', time);
    
   ``` 
   ```
    create view errors2 as 
    select DATE_TRUNC ('day', time) as day, count(*) as errors
    from log
    where status != '200 OK'
    group by DATE_TRUNC('day',time);
    
   ```
   ```
     create view errorrate4 as 
     select errors2.day, (errors2.errors/totals2.totals :: float) as errvalue
     from errors2 , totals2
     where errors2.day = totals2.day
     order by day asc;
     
   ``` 
   ``` 
     create view lastview as
     select day, (errvalue *100) as error 
     from errorrate4;
     
   ``` 
 ### Python reporting tool
    
 Once the views have been created , inside the Virtual machine run the pyhton file
    
   ```
     $ python reportingtool.py
     
   ``` 
 The pyhton file will execute and the results will be printed on the terminal.
    
 ### Author
     Tanya Sharma
    
