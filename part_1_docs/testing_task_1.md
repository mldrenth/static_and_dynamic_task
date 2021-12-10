### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # = used instead of == to find out if two values are equal
    if card.value = 1:
      return True
    #No colon after else
    else
      return False
   
#dif instead of def to define a function
#no comma after card1
  dif highest_card(self, card1 card2):
  # If/else block not indented correctly
  if card1.value > card2.value:
    # returning card instead of card1
    return card
  else:
    return card2
  

# method not inside of class, needs indentation
def cards_total(self, cards):
  #total variable not set to 0
  total
  for card in cards:
    total += card.value
    #return indetented too much
    #string not formated to include integer
    return "You have a total of" + total
  
```
