This repo contains a number of different scripts and apps for different projects

# WebScraping Projects
This directory contains a collection of python scripts for learning about web scraping and using public APIs

1. static_scrape_bsoup.py - this is a script that shows how to use the beautiful soup library to scrape a static website (the UCD Chem Eng homepage)
2. dynamic_web_scrape_selenium.py - this is a script that shows how to use the selenium library to scrape a dynamic website (a food bloggers website)
3. dynamic_web_scrape_blocked_by_cloudflare.py - this is a script that shows how selenium can fail if a website protects itself using tools like cloud flare (atp website)
4. stackexchangeAPI.py - this is a script that shows how to use publically available APIs (the stack overflow website)

# API Development Projects
1. drink_sql_project - this is a project that demonstrates how to create, query and add rows to a SQL lite database using python APIs from a front end flask app
   * web_app.py - this is a flask webapp that enables a user to call the python APIs built in the backend_app.py, it also has a templates folder with its html files
   * backend_app.py - this is a where we create the methods to add, delete, query drinks
2. email_project - this is a project that demonstrates how to let a user send an email using a python API from a front end flask app
   * web_app.py - this is a flask webapp that enables a user to call the python APIs built in the backend_app.py
   * backend_app.py - this is a where we create the methods to send the email
3. spark_submit_project - this is a project that demonstrates how to let a user start a spark job on the edge node using a python API from a front end flask app
   * web_app.py - this is a flask webapp that enables a user to call the python APIs built in the backend_app.py
   * backend_app.py - this is a where we create the methods to start the spark job
