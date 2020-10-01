# python-challenge

##PyBank
For this part of the homework, the data includes monthly finances over the course of a few years.
* By looping through the months, the code will find the overall number of months and total net earnings in the data
* The loop function also allows the code to calculate the monthly finance value, and subtract it by the previous month to find monthly changes
* By creating a list of the changes each month, the average change is calculated on the data set aside
    * This also allows the best increase and worst decrease amounts to be found, and which month they occurred

By running the code, it will populate all of these values in the terminal, as well as print a text file in the resources folder for PyBank

##PyPoll
The pypoll code I wrote uses the loop function similarly to the PyBank function to pull out specific data in each row.
* Looping through the rows allows it to add a row (vote) as it cycles through the data to collect total votes
* Creating a dictionary for vote percent and vote counts allowed us to pull the data will specific candidates.
    * This was how a winner was ultimately found, as a for loop searched through to vote count dictionary for who had the most votes

By running the code, it will populate all of these values in the terminal, as well as print a text file in the resources folder for PyPoll
