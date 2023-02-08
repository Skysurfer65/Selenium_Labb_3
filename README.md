# Lab 3 Selenium MVT22

## WHAT
This was an assignment in **SELENIUM** testing.<br/>
We had three test cases that was given to us, all with exploring:<br/>
https://ecutbildning.se/<br/>
The test cases, in Swedish, where:

## Test case 1:
Navigera till den utbildning ni går mgenom menyn och verifiera att utbildningen finns i Malmö och att 
utbildningens längd är 1,5 år.**(This is a wrong assumption as it is 2 years)**
## Test case 2:
Navigera till studieorten Malmö genom sökfältet och verifiera att skolans address är: Östra 
Kanalgatan 5, samt att Mjukvarutestrare finns som utbildning på studieorten.
## Test case 3:
Gå till första nyhetsartikeln (under rubriken aktuellt) på sidan och verifiera att länken leder till en 
nyhetsida med samma rubrik som nyheten du tryckt på.

## HOW TO
No installation is necessary. Run from your chosen Python environment.
The Python environment has to have Selenium installed:<br/>
pip install selenium<br/>
The webdriver is installed from "webdriver_manager" so no need to worry about correct version of your local webdriver.

## TESTS
Tests are written in Python with the Selenium module and asserted with unittest.<br/>
I have used Seleniums own example of **page object design**.<br/>
This might be confusing at start but makes code so much shorter and accessible.<br/>
It's designed to be run from your CLI root folder, just type:<br/>
python -m unittest main -v<br/>

## AUTHOR
Richard Fehling, student at EC Utbildning, MVT22<br/>
richard.fehling@learnet.se