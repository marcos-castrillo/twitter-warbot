tweeting_interval = 3600 # seconds
sleeping_interval = 600 # seconds
live = True # console or tweet
preload_data = True
sleeping_hours = [3, 4, 5, 6, 7]

prob_item = 70
prob_battle = 25
prob_accident = 3
prob_suicide = 1
prob_revive =  1
simulation_probab = [prob_item, prob_battle, prob_accident, prob_suicide, prob_revive] # = 100

probab_tie = 3
probab_friend_tie = 5

probab_rarity_1 = 70
probab_rarity_2 = 20
probab_rarity_3 = 10
item_probab = [probab_rarity_1, probab_rarity_2, probab_rarity_3] # = 100

hour_thresholds = [25, 50, 100]
simulation_probab_0 = [prob_item - 5, prob_battle + 3, prob_accident + 1, prob_suicide + 1, prob_revive] # = 100
simulation_probab_1 = [prob_item - 8, prob_battle + 5, prob_accident + 1, prob_suicide + 1, prob_revive + 1] # = 100
simulation_probab_2 = [prob_item - 15, prob_battle + 7, prob_accident + 3, prob_suicide + 3, prob_revive + 2] # = 100
item_probab_0 = [probab_rarity_1 - 5, probab_rarity_2 + 3, probab_rarity_3 + 2] # = 100
item_probab_1 = [probab_rarity_1 - 8, probab_rarity_2 + 5, probab_rarity_3 + 3] # = 100
item_probab_2 = [probab_rarity_1 - 15, probab_rarity_2 + 10, probab_rarity_3 + 5] # = 100
