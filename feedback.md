# Feedback

## P1T1

-[x] Nice `__str__` in player - would make a good repr but understanding the restrictions of the exercise :)

-[x] Beware of implementing methods with false affordances: so for example you have a get node by index (btw, use `__getitem__` and then you can subscript this). But usually this implies random access which the list does not give you - very nice implementation though.

-[x] `del_head` - I really like the implementation here very good defensive programming practices and not afraid to raise exceptions.
    Just watch PEP8 - delete_head...

-[x] and consider if implementing pop and pop_left would be better than adding the complexity of delete...

-[x] player_node:
    IMO use from `__future__ import annotations` to avoid the restriction of having to implement types as strings and then allows you to consistently use piping

-[x] excellent test cases. very descriptive names and appropriate tests.