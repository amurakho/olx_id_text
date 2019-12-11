Hi!
You should be in olx_in_test path!

At first you need install the venv and use:
>> pip install -r requirements.txt

Next you should go to the olx_test:
>> cd olx_test

And you can run it with command:
>>  scrapy crawl spider -o base.csv
(the base.csv is the file with base)

Hmm. Yes i use csv format. Its not a main format for excel, but it is also used

!ATTENTION!
www.olx.co.id - is dont like when we scrape pagination. So it close it in robot.txt.
Because of this, I put a delay between requests(1 sec). But if you want - you can change it in
olx_test/olx_test/settings.py (The variabe called "DOWNLOAD_DELAY").
