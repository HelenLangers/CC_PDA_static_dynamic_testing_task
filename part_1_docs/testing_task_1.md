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
    # requires double equals for 'equal to'
    if card.value = 1:
      return True
      # needs a colon after else
    else
      return False
   
# spelling error. dif should be def.
# comma needed after 'card1'
  dif highest_card(self, card1 card2):
    if card1.value > card2.value:
      # 'card' isn't defined. Should be card1
      return card
    else:
      return card2
  

  # total needs to be a defined variable e.g. total = 0
  def cards_total(self, cards):
    total
    for card in cards:
      total += card.value
    return "You have a total of" + total
  # the return here should return an f string: return(f"You have a total of {total}")
```
