class Card:
    def __init__(self, name, value, group, rank, bonus=0, penalty=0, is_blanked=1, bonus_flag=1, penalty_flag=1, army_flag=1, flame_flag=1, leader_flag=1, beast_flag=1 , Island_flag= 0):
        self.name = name  # Card name (e.g., "Ace of Spades")
        self.value = value  # Numeric or symbolic value
        self.group = group  # Suit or category (e.g., "Spades")
        self.rank = rank  # Rank of the card
        self.bonus = bonus  # Bonus points for the card
        self.penalty = penalty  # Penalty points for the card
        self.is_blanked = is_blanked  # Internal attribute for blanked state
        self.bonus_flag = bonus_flag  # Bonus flag
        self.penalty_flag = penalty_flag  # Penalty flag
        self.army_flag = army_flag  # Army flag specific to the card
        self.flame_flag = flame_flag  # Flame flag specific to the card
        self.leader_flag = leader_flag  # Leader flag specific to the card
        self.beast_flag = beast_flag  # Beast flag specific to the card
        self.Island_flag = 0


@property
def is_blanked(self):
    return self.is_blanked

@is_blanked.setter
def is_blanked(self, value):
    # Allow resetting to 1 even if it was 2
    if value == 1 or (self.is_blanked != 2 and value in [0, 1]):
        self.is_blanked = value
    else:
        raise ValueError("Invalid state transition for is_blanked. Cannot change from 2 to 0.")

    def __repr__(self):
        return f"Card(name={self.name}, value={self.value}, group={self.group}, rank={self.rank}, bonus={self.bonus}, penalty={self.penalty}, is_blanked={self.is_blanked}, bonus_flag={self.bonus_flag}, penalty_flag={self.penalty_flag}, army_flag={self.army_flag}, flame_flag={self.flame_flag}, leader_flag={self.leader_flag}, beast_flag={self.beast_flag})"


class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        cards_info = [
            {"Name": "Rangers", "Suit": "Army", "Value": 5},
            {"Name": "Elven Archers", "Suit": "Army", "Value": 10},
            {"Name": "Dwarvish Infantry", "Suit": "Army", "Value": 15},
            {"Name": "Light Cavalry", "Suit": "Army", "Value": 17},
            {"Name": "Knights", "Suit": "Army", "Value": 20},
            {"Name": "Rune Of Protection", "Suit": "Artifact", "Value": 1},
            {"Name": "World Tree", "Suit": "Artifact", "Value": 2},
            {"Name": "Book of Changes", "Suit": "Artifact", "Value": 3},
            {"Name": "Shield of Keth", "Suit": "Artifact", "Value": 4},
            {"Name": "Gem of Order", "Suit": "Artifact", "Value": 5},
            {"Name": "War Horse", "Suit": "Beast", "Value": 6},
            {"Name": "Unicorn", "Suit": "Beast", "Value": 9},
            {"Name": "Hydra", "Suit": "Beast", "Value": 12},
            {"Name": "Dragon", "Suit": "Beast", "Value": 30},
            {"Name": "Basilisk", "Suit": "Beast", "Value": 35},
            {"Name": "Candle", "Suit": "Flame", "Value": 2},
            {"Name": "Fire Elemental", "Suit": "Flame", "Value": 4},
            {"Name": "Forge", "Suit": "Flame", "Value": 9},
            {"Name": "Lightning", "Suit": "Flame", "Value": 11},
            {"Name": "Wildfire", "Suit": "Flame", "Value": 40},
            {"Name": "Fountain of Life", "Suit": "Flood", "Value": 1},
            {"Name": "Water Elemental", "Suit": "Flood", "Value": 4},
            {"Name": "Island", "Suit": "Flood", "Value": 14},
            {"Name": "Swamp", "Suit": "Flood", "Value": 18, "Army_Flag": 1, "Flame_Flag": 1},
            {"Name": "Great Flood", "Suit": "Flood", "Value": 32},
            {"Name": "Earth Elemental", "Suit": "Land", "Value": 4},
            {"Name": "Underground Caverns", "Suit": "Land", "Value": 6},
            {"Name": "Forest", "Suit": "Land", "Value": 7},
            {"Name": "Bell Tower", "Suit": "Land", "Value": 8},
            {"Name": "Mountain", "Suit": "Land", "Value": 9},
            {"Name": "Princess", "Suit": "Leader", "Value": 2},
            {"Name": "Warlord", "Suit": "Leader", "Value": 4},
            {"Name": "Queen", "Suit": "Leader", "Value": 6},
            {"Name": "King", "Suit": "Leader", "Value": 8},
            {"Name": "Empress", "Suit": "Leader", "Value": 15},
            {"Name": "Magic Wand", "Suit": "Weapon", "Value": 1},
            {"Name": "Elven Longbow", "Suit": "Weapon", "Value": 3},
            {"Name": "Sword of Keth", "Suit": "Weapon", "Value": 7},
            {"Name": "Warship", "Suit": "Weapon", "Value": 23},
            {"Name": "War Dirigable", "Suit": "Weapon", "Value": 35},
            {"Name": "Air Elemental", "Suit": "Weather", "Value": 4},
            {"Name": "Rainstorm", "Suit": "Weather", "Value": 8},
            {"Name": "Whirlwind", "Suit": "Weather", "Value": 13},
            {"Name": "Smoke", "Suit": "Weather", "Value": 27},
            {"Name": "Blizzard", "Suit": "Weather", "Value": 30},
            {"Name": "Shapeshifter", "Suit": "Wild", "Value": 0},
            {"Name": "Mirage", "Suit": "Wild", "Value": 0},
            {"Name": "Doppelganger", "Suit": "Wild", "Value": 0},
            {"Name": "Necromancer", "Suit": "Wizard", "Value": 3},
            {"Name": "Elemental Enchantress", "Suit": "Wizard", "Value": 5},
            {"Name": "Collector", "Suit": "Wizard", "Value": 7},
            {"Name": "Beastmaster", "Suit": "Wizard", "Value": 9},
            {"Name": "Warlock Lord", "Suit": "Wizard", "Value": 25}
        ]

        for card_info in cards_info:
            card = Card(
                name=card_info["Name"],
                value=card_info["Value"],
                group=card_info["Suit"],
                rank=0,
                army_flag=card_info.get("Army_Flag", 1),
                flame_flag=card_info.get("Flame_Flag", 1),
                leader_flag=card_info.get("Leader_Flag", 1),
                beast_flag=card_info.get("Beast_Flag", 1)
            )  # Rank can be adjusted as needed
            self.cards.append(card)

    def get_card(self, name):
        """Retrieve a card by its name."""
        for card in self.cards:
            if card.name == name:
                return card
        return None

    def update_card(self, name, **kwargs):
        """Update attributes of a specific card by its name."""
        card = self.get_card(name)
        if card:
            for key, value in kwargs.items():
                if hasattr(card, key):
                    setattr(card, key, value)

    def display_deck(self):
        """Display all cards in the deck."""
        for card in self.cards:
            print(card)

    def select_hand(self, names):
        """Select a hand of cards by their names."""
        hand = [self.get_card(name) for name in names if self.get_card(name)]
        return hand
#------------------------------------------------->>>>>>>>>>>>>>>>>  rangers
    def rangers_bonus(self, hand, rangers_card):
        land_count = sum(1 for c in hand if c.group == "Land" and c.is_blanked != 0)
        rangers_card.bonus += land_count * 10
        print(f"Rangers Bonus Applied: +{land_count * 10}")


    def rangers_effect(self,hand):
      # Check for Dwarvish Infantry in hand
        Flag = 0
        # Check for Wildfire in hand
        Wildfire_count = sum(1 for c in hand if c.group == "Wildfire" and c.is_blanked != 0)
        # Check for Mountain in hand
        mountain_count = sum(1 for c in hand if c.group == "Mountain" and c.is_blanked != 0)
        # Check for Great Flood in hand
        Great_Flood_count = sum(1 for c in hand if c.group == "Great Flood" and c.is_blanked != 0)

        if Wildfire_count == 0 :
          Flag = 1
        if Great_Flood_count == 0 :
          Flag = 0
        if mountain_count == 0 :
          Flag = 1



      # Check for Dwarvish Infantry in hand
        for card in hand:
            if card.name == "Dwarvish Infantry" and Flag == 0 and card.is_blanked != 0:
                card.penalty_flag = 0
                card.is_blanked = 2
                print("Dwarvish Infantry Penalty Flag Set to 0")

        # Check for Swamp in hand
        for card in hand:
            if card.name == "Swamp" and Flag == 0 and card.is_blanked != 0:
                card.army_flag = 0
                card.is_blanked = 2
                print("Swamp Army Flag Set to 0")

        # Check for Blizzard in hand
        for card in hand:
            if card.name == "Blizzard" and Flag == 0 and card.is_blanked != 0:
                card.army_flag = 0
                card.is_blanked = 2
                print("Blizzard Army Flag Set to 0")

        print("Rangers Effect Applied: Done")


#------------------------------------------------->>>>>>>>>>>>>>>>>  Elven Archers
    def elven_archers_bonus(self, hand, elven_archers_card):
            """Apply bonus for Elven Archers if no Weather card in hand is active."""
            weather_count = sum(1 for c in hand if c.group == "Weather" and c.is_blanked != 0)
            if weather_count == 0:
                elven_archers_card.bonus += 5
                print("Elven Archers Bonus Applied: +5")


# ---------------------------------------------------------->  Dwarvish Infantry



    def dwarvish_infantry_penalty(self, hand, dwarvish_infantry_card):
        """Apply penalty for Dwarvish Infantry: -2 for each other Army card if Land is not blanked."""
        army_count = sum(1 for c in hand if c.group == "Army"  and c.is_blanked != 0)
        army_count -=1
        land_active = any(c.group == "Land" and c.is_blanked != 0 for c in hand)
        if land_active:
            dwarvish_infantry_card.penalty -= army_count * 2
            print(f"Dwarvish Infantry Penalty Applied: -{dwarvish_infantry_card.penalty}")

            print(f"Dwarvish Infantry Penalty Applied: -{army_count * 2}")

#--------------------------------------------------------->  Light Cavalry



    def light_cavalry_penalty(self, hand, light_cavalry_card):
        """Apply penalty for Light Cavalry: -2 for each Land card."""
        land_count = sum(1 for c in hand if c.group == "Land" and c.is_blanked != 0)
        light_cavalry_card.penalty -= land_count * 2
        print(f"Light Cavalry Penalty Applied: -{land_count * 2}")


# ------------------------------------------------------->

    def knights_penalty(self, hand, knights_card):
        """Apply penalty for  Knights: -8 unless with at least one Leader."""
        leader_active = any(c.group == "Leader" and c.is_blanked != 0 for c in hand)
        if not leader_active:
            knights_card.penalty -= 8
            print("Knights Penalty Applied: -8")
        print(leader_active)

# ------------------------------------------------------------->
    def rune_Of_Protection_effect(self, hand, Rune_Of_Protection_card):
        """Apply the Rune Of Protection effect: Clears penalties and blanks all cards."""
        for card in hand:
            card.is_blanked = 2
            card.penalty_flag = 0
        print("Rune Of Protection Effect Applied: Penalties cleared and cards blanked.")

# ------------------------------------------------------------->


    def world_tree_bonus(self, hand, world_tree_card):
        """Apply bonus for World Tree: +50 if every non-blanked card is a different suit."""
        active_suits = {card.group for card in hand if card.is_blanked != 0}
        if len(active_suits) == len([card for card in hand if card.is_blanked != 0]):
            world_tree_card.bonus += 50
            print("World Tree Bonus Applied: +50")


    def shield_of_keth_bonus(self, hand, shield_of_keth_card):
        """Apply bonus for Shield of Keth: +15 with any one Leader, +40 with both Leader and Sword of Keth."""
        has_leader = any(card.group == "Leader" and card.is_blanked != 0 for card in hand)
        has_sword_of_keth = any(card.name == "Sword of Keth" and card.is_blanked != 0 for card in hand)

        if has_leader and has_sword_of_keth:
            shield_of_keth_card.bonus += 40
            print("Shield of Keth Bonus Applied: +40 (Leader and Sword of Keth present)")
        elif has_leader:
            shield_of_keth_card.bonus += 15
            print("Shield of Keth Bonus Applied: +15 (Leader present)")

    def gem_of_order_bonus(self, hand, gem_of_order_card):
        """Apply bonus for Gem of Order based on runs of card values."""
        active_cards = sorted([card.value for card in hand if card.is_blanked != 0])
        longest_run = 0
        current_run = 1

        for i in range(1, len(active_cards)):
            if active_cards[i] == active_cards[i - 1] + 1:
                current_run += 1
                longest_run = max(longest_run, current_run)
            else:
                current_run = 1

        bonus_map = {3: 10, 4: 30, 5: 60, 6: 100, 7: 150}
        if longest_run >= 3:
            gem_of_order_card.bonus += bonus_map.get(longest_run, 0)
            print(f"Gem of Order Bonus Applied: +{bonus_map.get(longest_run, 0)} for {longest_run}-card run")

    def war_Horse_bonus(self, hand, war_Horse_card):
        """Apply bonus for War Horse: +14 with any Leader or Wizard."""
        has_leader_or_wizard = any(
            card.group in ["Leader", "Wizard"] and card.is_blanked != 0 for card in hand
        )

        if has_leader_or_wizard:
            war_Horse_card.bonus += 14
            print("War Horse Bonus Applied: +14 (Leader or Wizard present)")


    def unicorn_bonus(self, hand, unicorn_card):
          """Apply bonus for Unicorn: +30 with Princess, +15 with Empress, Queen, or Elemental Enchantress."""
          has_princess = any(card.name == "Princess" and card.is_blanked != 0 for card in hand)
          has_empress_queen_enchantress = any(
              card.name in ["Empress", "Queen", "Elemental Enchantress"] and card.is_blanked != 0 for card in hand
          )

          if has_princess:
              unicorn_card.bonus += 30
              print("Unicorn Bonus Applied: +30 (Princess present)")
          elif has_empress_queen_enchantress:
              unicorn_card.bonus += 15
              print("Unicorn Bonus Applied: +15 (Empress, Queen, or Elemental Enchantress present)")

    def hydra_bonus(self, hand, hydra_card):
        """Apply bonus for Hydra: +28 with Swamp."""
        has_swamp = any(card.name == "Swamp" and card.is_blanked != 0 for card in hand)

        if has_swamp:
            hydra_card.bonus += 28
            print("Hydra Bonus Applied: +28 (Swamp present)")

    def dragon_penalty(self, hand, dragon_card):
        """Apply penalty for Dragon: -40 unless with at least one Wizard."""
        has_wizard = any(card.group == "Wizard" and card.is_blanked != 0 for card in hand)

        if not has_wizard:
            dragon_card.penalty -= 40
            print("Dragon Penalty Applied: -40 (No Wizard present)")


    def basilisk_effect(self, hand, basilisk_card):
        """Apply Basilisk effect: Blanks all Leaders and Beasts if Rangers are in the hand and not blanked; otherwise, blanks all Armies, Leaders, and Beasts."""
        has_active_rangers = any(card.name == "Rangers" and card.is_blanked != 0 for card in hand)
        print(f"Has Active Rangers: {has_active_rangers}")

        for card in hand:
            if has_active_rangers:
                if card.group in ["Leader", "Beast"] and card != basilisk_card:
                    if card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                        card.is_blanked = 0
                        print(f"Basilisk Effect Applied with Rangers: Card {card.name} blanked.")
            else:
                if card.group in ["Army", "Leader", "Beast"] and card != basilisk_card:
                    if card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                        card.is_blanked = 0
                        print(f"Basilisk Effect Applied without Rangers: Card {card.name} blanked.")

    def candle_bonus(self, hand, candle_card):
        """Apply bonus for Candle: +100 with Book of Changes, Bell Tower, and any one Wizard."""
        has_book_of_changes = any(card.name == "Book of Changes" and card.is_blanked != 0 for card in hand)
        has_bell_tower = any(card.name == "Bell Tower" and card.is_blanked != 0 for card in hand)
        has_wizard = any(card.group == "Wizard" and card.is_blanked != 0 for card in hand)

        if has_book_of_changes and has_bell_tower and has_wizard:
            candle_card.bonus += 100
            print("Candle Bonus Applied: +100 (Book of Changes, Bell Tower, and Wizard present)")

    def fire_elemental_bonus(self, hand, fire_elemental_card):
        """Apply bonus for Fire Elemental: +15 for each other Flame."""
        flame_count = sum(1 for card in hand if card.group == "Flame" and card != fire_elemental_card and card.is_blanked != 0)
        fire_elemental_card.bonus += flame_count * 15
        print(f"Fire Elemental Bonus Applied: +{flame_count * 15} for {flame_count} other Flames")

    def forge_bonus(self, hand, forge_card):
        """Apply bonus for Forge: +9 for each Weapon and Artifact."""
        bonus_count = sum(1 for card in hand if card.group in ["Weapon", "Artifact"] and card.is_blanked != 0)
        forge_card.bonus += bonus_count * 9
        print(f"Forge Bonus Applied: +{bonus_count * 9} for {bonus_count} Weapons and Artifacts")

    def lightning_bonus(self, hand, lightning_card):
        """Apply bonus for Lightning: +30 with Rainstorm."""
        has_rainstorm = any(card.name == "Rainstorm" and card.is_blanked != 0 for card in hand)

        if has_rainstorm:
            lightning_card.bonus += 30
            print("Lightning Bonus Applied: +30 (Rainstorm present)")

    def water_elemental_bonus(self, hand, water_elemental_card):
        """Apply bonus for Water Elemental: +15 for each other Flood."""
        flood_count = sum(1 for card in hand if card.group == "Flood" and  card.is_blanked != 0)
        flood_count -= 1
        water_elemental_card.bonus += flood_count * 15
        print(f"Water Elemental Bonus Applied: +{flood_count * 15} for {flood_count} other Floods")

    def swamp_penalty(self, hand, swamp_card):
        """Apply penalty for Swamp: -3 for each Army and Flame, considering their respective flags."""
        if swamp_card.Island_flag == 0 :
          army_count = sum(1 for card in hand if card.group == "Army" and card.is_blanked != 0)
          flame_count = sum(1 for card in hand if card.group == "Flame" and card.is_blanked != 0)
          print(f"Army Count: {army_count}, Flame Count: {flame_count}")

          army_penalty = army_count * -3 * swamp_card.army_flag
          flame_penalty = flame_count * -3 * swamp_card.flame_flag

          total_penalty = army_penalty + flame_penalty
          swamp_card.penalty = total_penalty

          print(f"Swamp Penalty Applied: {army_penalty} for Army, {flame_penalty} for Flame, Total: {total_penalty}")

    def earth_elemental_bonus(self, hand, earth_elemental_card):
        """Apply bonus for Earth Elemental: +15 for each other Land."""
        land_count = sum(1 for card in hand if card.group == "Land" and card != earth_elemental_card and card.is_blanked != 0)
        earth_elemental_card.bonus += land_count * 15
        print(f"Earth Elemental Bonus Applied: +{land_count * 15} for {land_count} other Lands")

    def underground_caverns_bonus(self, hand, underground_caverns_card):
        """Apply bonus for Underground Caverns: +25 with Dwarvish Infantry or Dragon."""
        has_dwarvish_infantry = any(card.name == "Dwarvish Infantry" and card.is_blanked != 0 for card in hand)
        has_dragon = any(card.name == "Dragon" and card.is_blanked != 0 for card in hand)

        if has_dwarvish_infantry or has_dragon:
            underground_caverns_card.bonus += 25
            print("Underground Caverns Bonus Applied: +25 (Dwarvish Infantry or Dragon present)")

    def underground_caverns_effect(self, hand):
        """Clears the Penalty on all Weather and blanks them."""
        Flag  = 0
        for card in hand:
            if card.name == "Wildfire" and card.is_blanked != 0 :
                Flag = 1
                print("Dwarvish Infantry Penalty Flag Set to 0")

        # Check for Great Flood in hand
        for card in hand:
            if card.name == "Great Flood" and card.is_blanked != 0 :
                Flag = 1
                print("Great Flood Army Flag Set to 0")

        if Flag == 0:
          for card in hand:
              if card.group == "Weather":
                  card.penalty = 0
                  card.is_blanked = 2
                  print(f"Underground Caverns Effect: Penalty cleared and card {card.name} blanked")

    def forest_bonus(self, hand, forest_card):
        """Apply bonus for Forest: +12 for each Beast and Elven Archers."""
        count = sum(1 for card in hand if card.group == "Beast" or card.name == "Elven Archers" and card.is_blanked != 0)
        forest_card.bonus += count * 12
        print(f"Forest Bonus Applied: +{count * 12} for {count} Beasts and Elven Archers")

    def bell_tower_bonus(self, hand, bell_tower_card):
        """Apply bonus for Bell Tower: +15 with any one Wizard."""
        has_wizard = any(card.group == "Wizard" and card.is_blanked != 0 for card in hand)

        if has_wizard:
            bell_tower_card.bonus += 15
            print("Bell Tower Bonus Applied: +15 (Wizard present)")

    def mountain_bonus(self, hand, mountain_card):
        """Apply bonus for Mountain: +50 with both Smoke and Wildfire."""
        has_smoke = any(card.name == "Smoke" and card.is_blanked != 0 for card in hand)
        has_wildfire = any(card.name == "Wildfire" and card.is_blanked != 0 for card in hand)

        if has_smoke and has_wildfire:
            mountain_card.bonus += 50
            print(f"Mountain Bonus: {mountain_card.bonus}")

    def mountain_effect(self, hand):
        """Clears the Penalty on all Floods and unblanks them."""
        for card in hand:
            if card.group == "Flood":
                card.penalty_flag= 0
                card.is_blanked = 2
                print(f"Mountain Effect: Penalty cleared and card {card.name} unblanked")




    def princess_bonus(self, hand, princess_card):
        """Apply bonus for Princess: +8 for each Army, Wizard, and other Leader."""
        count = sum(1 for card in hand if card.group in ["Army", "Wizard", "Leader"] and card != princess_card and card.is_blanked != 0)
        princess_card.bonus += count * 8
        print(f"Princess Bonus Applied: +{count * 8} for {count} Armies, Wizards, and Leaders")

    def warlord_bonus(self, hand, warlord_card):
        """Apply bonus for Warlord: Equal to the base strengths of all Armies in your hand."""
        army_total = sum(card.value for card in hand if card.group == "Army" and card.is_blanked != 0)
        warlord_card.bonus += army_total
        print(f"Warlord Bonus Applied: +{army_total} (Base strengths of all Armies)")

    def queen_bonus(self, hand, queen_card):
        """Apply bonus for Queen: +5 for each Army, +20 for each Army if in the same hand with King."""
        has_king = any(card.name == "King" and card.is_blanked != 0 for card in hand)
        army_count = sum(1 for card in hand if card.group == "Army" and card.is_blanked != 0)

        if has_king:
            queen_card.bonus += army_count * 20
            print(f"Queen Bonus Applied: +{army_count * 20} (Army count with King present)")
        else:
            queen_card.bonus += army_count * 5
            print(f"Queen Bonus Applied: +{army_count * 5} (Army count without King)")

    def king_bonus(self, hand, king_card):
        """Apply bonus for King: +5 for each Army, +20 for each Army if in the same hand with Queen."""
        has_queen = any(card.name == "Queen" and card.is_blanked != 0 for card in hand)
        army_count = sum(1 for card in hand if card.group == "Army" and card.is_blanked != 0)

        if has_queen:
            king_card.bonus += army_count * 20
            print(f"King Bonus Applied: +{army_count * 20} (Army count with Queen present)")
        else:
            king_card.bonus += army_count * 5
            print(f"King Bonus Applied: +{army_count * 5} (Army count without Queen)")

    def empress_bonus(self, hand, empress_card):
        """Apply bonus for Empress: +10 for each Army."""
        army_count = sum(1 for card in hand if card.group == "Army" and card.is_blanked != 0)
        empress_card.bonus += army_count * 10
        print(f"Empress Bonus Applied: +{army_count * 10} for {army_count} Armies")


    def magic_wand_bonus(self, hand, magic_wand_card):
        """Apply bonus for Magic Wand: +25 with any one Wizard."""
        has_wizard = any(card.group == "Wizard" and card.is_blanked != 0 for card in hand)

        if has_wizard:
            magic_wand_card.bonus += 25
            print("Magic Wand Bonus Applied: +25 (Wizard present)")

    def elven_longbow_bonus(self, hand, elven_longbow_card):
        """Apply bonus for Elven Longbow: +30 with Elven Archers, Warlord, or Beastmaster."""
        has_match = any(card.name in ["Elven Archers", "Warlord", "Beastmaster"] and card.is_blanked != 0 for card in hand)

        if has_match:
            elven_longbow_card.bonus += 30
            print("Elven Longbow Bonus Applied: +30 (Elven Archers, Warlord, or Beastmaster present)")


    def underground_caverns_effect(self, hand):
        """Clears the Penalty on all Weather and blanks them."""
        for card in hand:
            if card.group == "Weather":
                card.penalty = 0
                card.is_blanked = 2
                print(f"Underground Caverns Effect: Penalty cleared and card {card.name} blanked")


    def empress_penalty(self, hand, empress_card):
        """Apply penalty for Empress: -5 for each other Leader."""
        leader_count = sum(1 for card in hand if card.group == "Leader" and card != empress_card and card.is_blanked != 0)
        empress_card.penalty -= leader_count * 5
        print(f"Empress Penalty Applied: -{leader_count * 5} for {leader_count} other Leaders")


    def sword_of_keth_bonus(self, hand, sword_of_keth_card):
        """Apply bonus for Sword of Keth: +10 with any one Leader, +40 with both Leader and Shield of Keth."""
        has_leader = any(card.group == "Leader" and card.is_blanked != 0 for card in hand)
        has_shield_of_keth = any(card.name == "Shield of Keth" and card.is_blanked != 0 for card in hand)

        if has_leader and has_shield_of_keth:
            sword_of_keth_card.bonus += 40
            print("Sword of Keth Bonus Applied: +40 (Leader and Shield of Keth present)")
        elif has_leader:
            sword_of_keth_card.bonus += 10
            print("Sword of Keth Bonus Applied: +10 (Leader present)")

    def air_elemental_bonus(self, hand, air_elemental_card):
        """Apply bonus for Air Elemental: +15 for each other Weather."""
        weather_count = sum(1 for card in hand if card.group == "Weather" and card != air_elemental_card and card.is_blanked != 0)
        air_elemental_card.bonus += weather_count * 15
        print(f"Air Elemental Bonus Applied: +{weather_count * 15} for {weather_count} other Weather cards")

    def elemental_enchantress_bonus(self, hand, elemental_enchantress_card):
        """Apply bonus for Elemental Enchantress: +5 for each Land, Weather, Flood, and Flame."""
        count = sum(1 for card in hand if card.group in ["Land", "Weather", "Flood", "Flame"] and card.is_blanked != 0)
        elemental_enchantress_card.bonus += count * 5
        print(f"Elemental Enchantress Bonus Applied: +{count * 5} for {count} cards in Land, Weather, Flood, or Flame groups")

    def collector_bonus(self, hand, collector_card):
        """Apply bonus for Collector: +10 if three different cards in same suit, +40 if four, +100 if five."""
        suit_counts = {}
        for card in hand:
            if card.is_blanked == 0:
                continue
            suit_counts[card.group] = suit_counts.get(card.group, 0) + 1

        for count in suit_counts.values():
            if count >= 5:
                collector_card.bonus += 100
                print("Collector Bonus Applied: +100 (Five different cards in same suit)")
                return
            elif count == 4:
                collector_card.bonus += 40
                print("Collector Bonus Applied: +40 (Four different cards in same suit)")
                return
            elif count == 3:
                collector_card.bonus += 10
                print("Collector Bonus Applied: +10 (Three different cards in same suit)")
                return

    def beastmaster_bonus(self, hand, beastmaster_card):
        """Apply bonus for Beastmaster: +9 for each Beast."""
        beast_count = sum(1 for card in hand if card.group == "Beast" and card.is_blanked != 0)
        beastmaster_card.bonus += beast_count * 9
        print(f"Beastmaster Bonus Applied: +{beast_count * 9} for {beast_count} Beasts")

    def beastmaster_effect(self, hand):
        """Clears the Penalty on all Beasts."""
        for card in hand:
            if card.group == "Beast":
                card.penalty = 0
                card.is_blanked = 2
                print(f"Beastmaster Effect: Penalty cleared on {card.name}")

    def warlock_lord_penalty(self, hand, warlock_lord_card):
          """Apply penalty for Warlock Lord: -10 for each Leader and other Wizard."""
          penalty_count = sum(1 for card in hand if card.group in ["Leader", "Wizard"] and card != warlock_lord_card and card.is_blanked != 0)
          warlock_lord_card.penalty -= penalty_count * 10
          print(f"Warlock Lord Penalty Applied: -{penalty_count * 10} for {penalty_count} Leaders and Wizards")


    def wildfire_effect(self, hand, wildfire_card):
        """Blanks all cards except Flames, Weather, Wizards, Weapons, Artifacts, Great Flood, Island, Mountain, Unicorn, & Dragon."""
        if wildfire_card.Island_flag == 0:
          great_flood = 0

          for card in hand:
              if card.name == "Great Flood":
                great_flood = 1
                print("Great Flood Army Flag Set to 1")

          for card in hand:
              if card.name == "Mountain":
                great_flood = 0
                print("Great Flood Army Flag Set to 0")

          if great_flood == 0:
            allowed_groups = ["Flame", "Weather", "Wizard", "Weapon", "Artifact"]
            allowed_names = ["Great Flood", "Island", "Mountain", "Unicorn", "Dragon"]

            for card in hand:
                if card.group not in allowed_groups and card.name not in allowed_names and card != wildfire_card:
                    if card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                        card.is_blanked = 0
                        print(f"Wildfire Effect: Card {card.name} blanked")

    def great_flood_effect(self, hand, great_flood_card):
        """Blanks all Armies, all Land except Mountain, all Flames except Lightning."""
        if great_flood_card.Island_flag == 0:
          mountain_count = 0
          rangers_count = 0

          for card in hand:
              if card.name == "Rangers":
                rangers_count = 1
                print("Great Flood Army Flag Set to 0")

          for card in hand:
              if card.name == "Mountain":
                mountain_count = 1
                print("Great Flood Army Flag Set to 1")

          if mountain_count == 0 and rangers_count  == 0:
            for card in hand:
                if card.group == "Army" or (card.group == "Land" and card.name != "Mountain") or (card.group == "Flame" and card.name != "Lightning"):
                    if card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                        card.is_blanked = 0
                        print(f"Great Flood Effect: Card {card.name} blanked")

          if rangers_count == 1 and mountain_count == 0 :
            for card in hand:
                if  (card.group == "Land" and card.name != "Mountain") or (card.group == "Flame" and card.name != "Lightning"):
                    if card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                        card.is_blanked = 0
                        print(f"Great Flood Effect: Card {card.name} blanked")



    def war_dirigible_effect(self, hand, war_dirigible_card):
        """Blanks War Dirigible unless with at least one Army, and if hand contains any Weather."""
        has_army = any(card.group == "Army" and card.is_blanked != 0 for card in hand)
        has_weather = any(card.group == "Weather" and card.is_blanked != 0 for card in hand)

        if not has_army or has_weather:
            if war_dirigible_card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                war_dirigible_card.is_blanked = 0
                reason = "no Army" if not has_army else "Weather present"
                print(f"War Dirigible Effect: Card {war_dirigible_card.name} blanked due to {reason}")

    def rainstorm_bonus(self, hand, rainstorm_card):
        """Apply bonus for Rainstorm: +10 for each Flood."""
        flood_count = sum(1 for card in hand if card.group == "Flood" and card.is_blanked != 0)
        rainstorm_card.bonus += flood_count * 10
        print(f"Rainstorm Bonus Applied: +{flood_count * 10} for {flood_count} Flood cards")

    def rainstorm_effect(self, hand):
        """Apply effect for Rainstorm: Blanks all Flames except Lightning."""
        for card in hand:
            if card.group == "Flame" and card.name != "Lightning":
                if card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                    card.is_blanked = 0
                    print(f"Rainstorm Penalty: Card {card.name} blanked")

    def whirlwind_bonus(self, hand, whirlwind_card):
        """Apply bonus for Whirlwind: +40 with Rainstorm and either Blizzard or Great Flood."""
        has_rainstorm = any(card.name == "Rainstorm" and card.is_blanked != 0 for card in hand)
        has_blizzard_or_great_flood = any(card.name in ["Blizzard", "Great Flood"] and card.is_blanked != 0 for card in hand)

        if has_rainstorm and has_blizzard_or_great_flood:
            whirlwind_card.bonus += 40
            print("Whirlwind Bonus Applied: +40 (Rainstorm and Blizzard/Great Flood present)")

    def smoke_effect(self, hand, smoke_card):
        """Blanks Smoke unless with at least one Flame."""
        has_flame = any(card.group == "Flame" and card.is_blanked != 0 for card in hand)

        if not has_flame:
            if smoke_card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                smoke_card.is_blanked = 0
                print(f"Smoke Effect: Card {smoke_card.name} blanked due to no Flame present")

    def blizzard_penalty(self, hand, blizzard_card):
        """Apply Blizzard penalty: -5 for each Army, Leader, Beast, and Flame."""
        penalty_count = sum(1 for card in hand if card.group in ["Army", "Leader", "Beast", "Flame"] and card.is_blanked != 0)
        blizzard_card.penalty -= penalty_count * 5
        print(f"Blizzard Penalty Applied: -{penalty_count * 5} for {penalty_count} cards in Army, Leader, Beast, and Flame groups")

    def blizzard_effect(self, hand):
        """Apply Blizzard effect: Blanks all Floods."""
        for card in hand:
            if card.group == "Flood":
                if card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                    card.is_blanked = 0
                    print(f"Blizzard Effect: Card {card.name} blanked")




# -------------------------------------------------------> the Top Cards

    def book_of_changes_effect(self, hand, book_of_changes_card):
        """Apply Book of Changes effect: User selects a card and assigns a new group."""
        selected_card_name = input("Enter the name of the card to change group: ").strip()
        selected_card = next((card for card in hand if card.name == selected_card_name), None)
        if selected_card:
            new_group = input("Enter the new group for the selected card: ").strip()
            selected_card.group = new_group
            print(f"Book of Changes Effect Applied: {selected_card.name} group changed to {new_group}")
        else:
            print("Book of Changes Effect: Selected card not found in hand.")



    def island_effect(self, hand, island_card):
        """Apply Island effect: User selects a card and applies specific calculations."""
        if island_card.is_blanked != 0:
            selected_card_name = input("Enter the name of the card to clear penalty: ").strip()
            selected_card = next((card for card in hand if card.name == selected_card_name), None)
            if selected_card:
                if selected_card.name in ["Swamp", "Great Flood", "Wildfire"]:
                    selected_card.Island_flag = 1
                    print(f"Island Effect Applied: Cleared penalty on {selected_card.name}")
                else:
                    print(f"Island Effect: {selected_card.name} is not eligible for penalty clearing.")
            else:
                print("Island Effect: Selected card not found in hand.")


    def warship_effect(self, hand, warship_card):
        """Apply Warship effect: Blanked unless with at least one Flood; Clears the word Army from Penalty section of all Floods."""
        has_flood = any(card.group == "Flood" and card.is_blanked != 0 for card in hand)

        if not has_flood:
            if warship_card.is_blanked != 2:  # Only blank if the card is not cleared of blanking
                warship_card.is_blanked = 0
                print(f"Warship Effect: Card {warship_card.name} blanked due to no Flood present")

        for card in hand:
            if card.name == "Blizzard":
                card.army_flag = 0
                print("Blizzard Army Flag Set to 0")



    def shapeshifter_effect(self, hand, shapeshifter_card):
        """Apply Shapeshifter effect: May take on the name and suit of any Artifact, Leader, Wizard, Weapon, or Beast."""
        valid_groups = ["Artifact", "Leader", "Wizard", "Weapon", "Beast"]
        available_cards = [card for card in self.cards if card.group in valid_groups and card.is_blanked != 0]

        if available_cards:
            print("Available cards to shapeshift into:")
            for card in available_cards:
                print(f"- {card.name} ({card.group})")

            selected_card_name = input("Enter the name of the card to shapeshift into: ").strip()
            selected_card = next((card for card in available_cards if card.name == selected_card_name), None)
            if selected_card:
                shapeshifter_card.name = selected_card.name
                shapeshifter_card.group = selected_card.group
                shapeshifter_card.penalty_flag = 0
                shapeshifter_card.bonus_flag = 0
                shapeshifter_card.value = 0
                print(f"Shapeshifter Effect Applied: Changed to {selected_card.name} ({selected_card.group})")
            else:
                print("Shapeshifter Effect: Selected card not found in available options.")
        else:
            print("Shapeshifter Effect: No valid cards to shapeshift into.")


    def mirage_effect(self, hand, mirage_card):
        """Apply Mirage effect: May take on the name and suit of any Army, Flame, Flood, Land, or Weather."""
        valid_groups = ["Army", "Flame", "Flood", "Land", "Weather"]
        available_cards = [card for card in self.cards if card.group in valid_groups and card.is_blanked != 0]

        if available_cards:
            print("Available cards to Mirage into:")
            for card in available_cards:
                print(f"- {card.name} ({card.group})")

            selected_card_name = input("Enter the name of the card to Mirage into: ").strip()
            selected_card = next((card for card in available_cards if card.name == selected_card_name), None)
            if selected_card:
                mirage_card.name = selected_card.name
                mirage_card.group = selected_card.group
                mirage_card.penalty_flag = 0
                mirage_card.bonus_flag = 0
                mirage_card.value = 0
                print(f"Mirage Effect Applied: Changed to {selected_card.name} ({selected_card.group})")
            else:
                print("Mirage Effect: Selected card not found in available options.")
        else:
            print("Mirage Effect: No valid cards to Mirage into.")


    def doppelganger_effect(self, hand, doppelganger_card):
        if doppelganger_card.is_blanked != 0:
            selected_card_name = input("Enter the name of the card to duplicate the name, suit, base strength with penalty with out bounes: ").strip()
            selected_card = next((card for card in hand if card.name == selected_card_name), None)
            if selected_card:
              selected_card.penalty_flag = 2
              selected_card.value*= 2
              doppelganger_card.name = selected_card.name
              doppelganger_card.group = selected_card.group
              doppelganger_card.penalty_flag =0
              doppelganger_card.bonus_flag =0
              doppelganger_card.value = 0

    def fountain_of_life_card_bonus(self, hand, fountain_of_life_card):
        """Apply Fountain of Life bonus: Add base strength of any Weapon, Flood, Flame, Land, or Weather card in hand."""
        valid_groups = ["Weapon", "Flood", "Flame", "Land", "Weather"]
        if fountain_of_life_card.is_blanked != 0:
            print("Available cards to add base strength from:")
            available_cards = [card for card in hand if card.group in valid_groups and card.is_blanked != 0]
            for card in available_cards:
                print(f"- {card.name} ({card.group}, Value: {card.value})")

            selected_card_name = input("Enter the name of the card to add base strength: ").strip()
            selected_card = next((card for card in available_cards if card.name == selected_card_name), None)
            if selected_card:
                fountain_of_life_card.value += selected_card.value
                print(f"Fountain of Life Bonus Applied: Added {selected_card.value} from {selected_card.name}")
            else:
                print("Fountain of Life Effect: Selected card not found in available options.")

    def card_effect(self, hand):
        """Apply specific card effects based on card names."""
        for card in hand:
            if card.is_blanked == 0:
                print(f"Card {card.name} is blanked, no effect applied.")
                continue

            if card.name == "Rune Of Protection":
                self.rune_Of_Protection_effect(hand, card)

            if card.name == "Rangers":
                self.rangers_effect(hand)

            if card.name == "Basilisk":
                self.basilisk_effect(hand, card)

            if card.name == "Underground Caverns":
                self.underground_caverns_effect(hand)

            if card.name == "Mountain":
                self.mountain_effect(hand)
                
            if card.name == "Beastmaster":
                self.beastmaster_effect(hand)

            if card.name == "Wildfire":
                self.wildfire_effect(hand, card)

            if card.name == "Great Flood":
                self.great_flood_effect(hand, card)

            if card.name == "War Dirigable":
                self.war_dirigible_effect(hand, card)

            if card.name == "Rainstorm":
                self.rainstorm_effect(hand)

            if card.name == "Smoke":
                self.smoke_effect(hand, card)

            if card.name == "Blizzard":
                self.blizzard_effect(hand)

            if card.name == "Warship":
                self.warship_effect(hand, card)

# ------------------------------------------------------->

    def card_Bonus_Penalty(self, hand):
        """Apply specific card effects based on card names."""
        for card in hand:
            if card.is_blanked == 0:
                print(f"Card {card.name} is blanked, no effect applied.")
                continue

            if card.name == "Rangers":
                self.rangers_bonus(hand, card)

            if card.name == "Elven Archers":
                self.elven_archers_bonus(hand, card)

            if card.name == "Dwarvish Infantry":
                self.dwarvish_infantry_penalty(hand, card)

            if card.name == "Light Cavalry":
                self.light_cavalry_penalty(hand, card)

            if card.name == "Knights":
                self.knights_penalty(hand, card)

            if card.name == "World Tree":
                self.world_tree_bonus(hand, card)

            if card.name == "Shield of Keth":
                self.shield_of_keth_bonus(hand, card)

            if card.name == "Gem of Order":
                self.gem_of_order_bonus(hand, card)

            if card.name == "War Horse":
                self.war_Horse_bonus(hand, card)

            if card.name == "Unicorn":
                self.unicorn_bonus(hand, card)

            if card.name == "Hydra":
                self.hydra_bonus(hand, card)

            if card.name == "Dragon":
                self.dragon_penalty(hand, card)

            if card.name == "Candle":
                self.candle_bonus(hand, card)

            if card.name == "Fire Elemental":
                self.fire_elemental_bonus(hand, card)

            if card.name == "Forge":
                self.forge_bonus(hand, card)

            if card.name == "Lightning":
                self.lightning_bonus(hand, card)

            if card.name == "Water Elemental":
                self.water_elemental_bonus(hand, card)

            if card.name == "Earth Elemental":
                self.earth_elemental_bonus(hand, card)

            if card.name == "Underground Caverns":
                self.underground_caverns_bonus(hand, card)

            if card.name == "Forest":
                self.forest_bonus(hand, card)

            if card.name == "Bell Tower":
                self.bell_tower_bonus(hand, card)

            if card.name == "Mountain":
                self.mountain_bonus(hand, card)

            if card.name == "Princess":
                self.princess_bonus(hand, card)

            if card.name == "Warlord":
                self.warlord_bonus(hand, card)

            if card.name == "Queen":
                self.queen_bonus(hand, card)

            if card.name == "King":
                self.king_bonus(hand, card)

            if card.name == "Empress":
                self.empress_bonus(hand, card)
                self.empress_penalty(hand, card)

            if card.name == "Magic Wand":
                self.magic_wand_bonus(hand, card)

            if card.name == "Elven Longbow":
                self.elven_longbow_bonus(hand, card)

            if card.name == "Sword of Keth":
                self.sword_of_keth_bonus(hand, card)
#-----------------------------  Done untill
            if card.name == "Air Elemental":
                self.air_elemental_bonus(hand, card)

            if card.name == "Elemental Enchantress":
                self.elemental_enchantress_bonus(hand, card)

            if card.name == "Collector":
                self.collector_bonus(hand, card)

            if card.name == "Beastmaster":
                self.beastmaster_bonus(hand, card)

            if card.name == "Warlock Lord":
                self.warlock_lord_penalty(hand, card)

            if card.name == "Rainstorm":
                self.rainstorm_bonus(hand, card)

            if card.name == "Whirlwind":
                self.whirlwind_bonus(hand, card)

            if card.name == "Blizzard":
                self.blizzard_penalty(hand, card)

            if card.name == "Swamp":
                self.swamp_penalty(hand, card)

            if card.name == "Fountain of Life":
                self.fountain_of_life_card_bonus(hand, card)


    def PreProcessing(self, hand):
        """Apply specific card effects based on card names."""
        for card in hand:
            if card.is_blanked == 0:
                print(f"Card {card.name} is blanked, no effect applied.")
                continue

            if card.name == "Book of Changes":
                self.book_of_changes_effect(hand, card)

            if card.name == "Shapeshifter":
                self.shapeshifter_effect(hand, card)

            if card.name == "Mirage":
                self.mirage_effect(hand, card)

            if card.name == "Doppelganger":
                self.doppelganger_effect(hand, card)

        for card in hand:
            if card.is_blanked == 0:
                print(f"Card {card.name} is blanked, no effect applied.")
                continue

            if card.name == "Island":
                self.island_effect(hand,card)

    def score(self, hand):
        """Calculate the score of the hand."""
        total_score = 0
        for card in hand:
            if card.is_blanked == 0:
                card_score = 0
            else:
                card_score = (card.bonus * card.bonus_flag) + (card.penalty * card.penalty_flag) + card.value
            total_score += card_score
            print(f"Card: {card.name}, Score: {card_score}")
        print(f"Total Hand Score: {total_score}")
        return total_score


import random

# List of valid cards
valid_card_names = [
    "Rangers", "Elven Archers", "Dwarvish Infantry", "Light Cavalry", "Knights",
    "Rune Of Protection", "World Tree", "Book of Changes", "Shield of Keth", "Gem of Order",
    "War Horse", "Unicorn", "Hydra", "Dragon", "Basilisk", "Candle", "Fire Elemental", "Forge", "Lightning", "Wildfire",
    "Fountain of Life", "Water Elemental", "Island", "Swamp", "Great Flood",
    "Earth Elemental", "Underground Caverns", "Forest", "Bell Tower", "Mountain",
    "Princess", "Warlord", "Queen", "King", "Empress",
    "Magic Wand", "Elven Longbow", "Sword of Keth", "Warship", "War Dirigable",
    "Air Elemental", "Rainstorm", "Whirlwind", "Smoke", "Blizzard",
    "Shapeshifter", "Mirage", "Doppelganger", "Necromancer", "Elemental Enchantress",
    "Collector", "Beastmaster", "Warlock Lord"
]



import random

def reset_card_values(player_hand):
    for card in player_hand:
        card.bonus = 0
        card.penalty = 0
        card.rank = 0
        card.is_blanked = 1
        card.bonus_flag = 1
        card.penalty_flag = 1
        card.army_flag = 1
        card.flame_flag = 1
        card.leader_flag = 1
        card.beast_flag = 1

    print("Card values have been reset.")

# List of valid cards
valid_card_names = [
    "Rangers", "Elven Archers", "Dwarvish Infantry", "Light Cavalry", "Knights",
    "Rune Of Protection", "World Tree", "Book of Changes", "Shield of Keth", "Gem of Order",
    "War Horse", "Unicorn", "Hydra", "Dragon", "Basilisk", "Candle", "Fire Elemental", "Forge", "Lightning", "Wildfire",
    "Fountain of Life", "Water Elemental", "Island", "Swamp", "Great Flood",
    "Earth Elemental", "Underground Caverns", "Forest", "Bell Tower", "Mountain",
    "Princess", "Warlord", "Queen", "King", "Empress",
    "Magic Wand", "Elven Longbow", "Sword of Keth", "Warship", "War Dirigable",
    "Air Elemental", "Rainstorm", "Whirlwind", "Smoke", "Blizzard",
    "Shapeshifter", "Mirage", "Doppelganger", "Necromancer", "Elemental Enchantress",
    "Collector", "Beastmaster", "Warlock Lord"
]

import random
from itertools import combinations
# Function to initialize the deck with user input or default cards
def initialize_deck(deck):

    return deck
# Function to get available cards not in use
def get_available_cards(deck, table_cards, players_hands):
    used_cards = table_cards + [card.name for hand in players_hands for card in hand]
    return [card for card in deck.cards if card.name not in used_cards]

# Function to distribute cards to players by user input
def get_player_hands(deck, num_players):
    players_hands = []
    for i in range(1, num_players + 1):
        while True:
            player_cards = input(f"Enter 7 cards for Player {i} (comma-separated): ").strip().split(",")
            player_cards = [card.strip() for card in player_cards]

            accepted_cards = [deck.get_card(card) for card in player_cards if deck.get_card(card)]
            rejected_cards = [card for card in player_cards if not deck.get_card(card)]

            if len(player_cards) != 7:
                print("Invalid selection. You must enter exactly 7 cards.")
            elif rejected_cards:
                print("The following cards are not in the deck:", rejected_cards)
            else:
                players_hands.append(accepted_cards)
                for card in accepted_cards:
                    deck.cards.remove(card)
                print(f"Player {i}'s hand accepted: {[card.name for card in accepted_cards]}")
                break

    return players_hands, deck

# Function to initialize the table with user input or start empty
def initialize_table(deck):
    user_input = input("\nEnter cards to start on the table (comma-separated) or press Enter to start with an empty table: ").strip()
    if user_input:
        table_cards = [deck.get_card(card.strip()) for card in user_input.split(",") if deck.get_card(card.strip())]
    else:
        table_cards = []

    print(f"Table initialized with {len(table_cards)} cards.")
    return table_cards

# Function to recommend the best 7-card combination after drawing a random card
def recommend_best_seven(deck, player_hand, random_card):
    """
    Given a player's hand (7 cards) and a drawn random card, recommend the best 
    7-card combination that maximizes the player's score.
    """
    best_score = float('-inf')
    best_hand = None
    best_card_to_discard = None

    # Combine player's current hand with the new drawn card (total 8 cards)
    temp_hand = player_hand + [random_card]

    # Generate all possible 7-card combinations
    score = 0
    best_score= 0
    for seven_card_combo in combinations(temp_hand, 7):
        seven_card_combo = list(seven_card_combo)

        reset_card_values(seven_card_combo)

        # Apply scoring functions
        deck.PreProcessing(seven_card_combo)
        deck.card_effect(seven_card_combo)
        deck.card_Bonus_Penalty(seven_card_combo)

        # Calculate score
        score = deck.score(seven_card_combo)

        # Ensure score is valid
        if score is None:
            score = float('-inf')

        # Track the best hand
        if score > best_score:
            best_score = score
            best_hand = seven_card_combo
            best_card_to_discard = next(card for card in temp_hand if card not in seven_card_combo)


    print(f"\n🔥 Best Possible Score: {best_score}")
    # Ensure we return a valid best hand
    if best_hand is None:
        best_hand = player_hand  # Default to the original hand
        best_card_to_discard = random_card  # Default to discarding the drawn card
        best_score = deck.score(player_hand) or 0

    return best_hand, best_card_to_discard, best_score

# Function to take a random card from the deck and discard one based on the optimal scoring system
def take_random_card(player_hand, deck, table_cards, players_hands):
    """
    Player takes a random card from the remaining deck and discards one based on the optimal scoring system.
    """
    available_cards = [
        card for card in deck.cards
        if card not in table_cards and all(card not in player for player in players_hands)
    ]

    if not available_cards:
        print("No cards left in the deck to draw.")
        return

    # Draw a random card
    random_card = random.choice(available_cards)
    print(f"\n🔹 Random card drawn: {random_card.name}")

    # Get the best combination of 7 cards
    best_hand, best_card_to_discard, best_score = recommend_best_seven(deck, player_hand, random_card)

    # Ensure best_hand is valid
    if best_hand is None:
        print("\n⚠️ Error: Could not determine the best hand. Keeping the original hand.")
        return

    # Decide whether to keep the random card or discard it
    if random_card in best_hand:
        print(f"\n✅ Recommended: **Keep {random_card.name}**")
        print(f"❌ Discard **{best_card_to_discard.name}** to maximize score.")
    else:
        print(f"\n❌ Recommended: **Do not keep {random_card.name}**")
        best_card_to_discard = random_card

    print(f"🔥 **New Best Hand:** {[card.name for card in best_hand]}")
    print(f"💯 Best Possible Score: {best_score}")


    # Ask the player which card to discard
    while True:
        card_to_discard_name = input(
            f"Enter the name of the card to discard (recommended: {best_card_to_discard.name}): "
        ).strip()

        # Check if the card is in the player's hand or if they want to discard the drawn random card
        card_to_discard = next(
            (card for card in player_hand if card.name == card_to_discard_name), None
        )

        if card_to_discard or (random_card.name == card_to_discard_name):
            # Remove the selected card
            if card_to_discard:
                player_hand.remove(card_to_discard)
            else:  # Player chose to discard the random card
                card_to_discard = random_card

            # Only add the random card if it was not discarded
            if card_to_discard != random_card:
                player_hand.append(random_card)

            # Add discarded card to the table
            table_cards.append(card_to_discard)

            print(f"✅ **{card_to_discard.name}** was discarded.")
            if card_to_discard != random_card:
                print(f"🔥 **{random_card.name}** added to your hand.")
            break
        else:
            print("❌ Invalid selection. Please enter a valid card name from your hand or the drawn random card.")


def recommend_best_swap(deck, player_hand, table_cards):
    """Recommend the best swap by evaluating all possible swaps and selecting the one with the highest score."""
    best_score = float('-inf')
    best_table_card = None
    best_hand_card = None
    best_new_hand = None

    for table_card in table_cards:
        for hand_card in player_hand:
            temp_hand = [card for card in player_hand if card != hand_card]  # Remove hand card
            temp_hand.append(table_card)  # Add table card

            # Reset and compute the score for this swap
            reset_card_values(temp_hand)
            deck.PreProcessing(temp_hand)
            deck.card_effect(temp_hand)
            deck.card_Bonus_Penalty(temp_hand)
            current_score = deck.score(temp_hand)

            if current_score > best_score:
                best_score = current_score
                best_table_card = table_card
                best_hand_card = hand_card
                best_new_hand = temp_hand.copy()

    return best_table_card, best_hand_card, best_new_hand, best_score



def swap_card_with_table(player_hand, table_cards, deck):
    """Allow player to swap a card from their hand with a card from the table, with a recommendation for best move."""
    if not table_cards:
        print("Table is empty. You can only take a random card.")
        return take_random_card(player_hand, deck, table_cards, players_hands)

    print(f"\nCards available on the table: {[card.name for card in table_cards]}")
    print(f"Your current hand: {[card.name for card in player_hand]}")

    # Recommend best swap
    best_table_card, best_hand_card, best_new_hand, best_score = recommend_best_swap(deck, player_hand, table_cards)

    if best_table_card and best_hand_card:
        print(f"\n✅ Recommended Swap: Take **{best_table_card.name}** from the table and discard **{best_hand_card.name}**")
        print(f"💯 Best Possible Score After Swap: {best_score}")

    # Double check for selecting a valid card from the table
    while True:
        table_card_name = input(f"\nEnter the name of the table card to take (recommended: {best_table_card.name}): ").strip()
        table_card = next((card for card in table_cards if card.name == table_card_name), None)
        if table_card:
            break
        print(f"❌ Invalid selection. '{table_card_name}' is not on the table. Please try again.")

    # Double check for selecting a valid card from the hand
    while True:
        hand_card_name = input(f"Enter the name of the card to swap from your hand (recommended: {best_hand_card.name}): ").strip()
        hand_card = next((card for card in player_hand if card.name == hand_card_name), None)
        if hand_card:
            break
        print(f"❌ Invalid selection. '{hand_card_name}' is not in your hand. Please try again.")

    # Perform the swap
    table_cards.remove(table_card)
    player_hand.remove(hand_card)

    table_cards.append(hand_card)
    player_hand.append(table_card)

    print(f"\n🔄 Swapped **{hand_card.name}** from your hand with **{table_card.name}** from the table.")
 

# Function to handle a player's turn
def player_turn(player_name, player_hand, deck, table_cards, players_hands):
    print(f"\n--- Table cards: {len(table_cards)}/10 ---")
    print(f"Cards available on the table: {[card.name for card in table_cards]}")

    print(f"\n{player_name}'s turn")

    if not table_cards:
        print("Table is empty. You can only take a random card.")
        take_random_card(player_hand, deck, table_cards, players_hands)
    else:
        print("Options: ")
        print("1. Take a random card and discard one (discarded card goes to table)")
        print("2. Swap a card with the table")

        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice == "1":
                take_random_card(player_hand, deck, table_cards, players_hands)
                break
            elif choice == "2":
                swap_card_with_table(player_hand, table_cards, deck)
                break
            else:
                print("Invalid choice, try again.")

    reset_card_values(player_hand)

    # Calculate and display player's score after the turn
    deck.PreProcessing(player_hand)
    deck.card_effect(player_hand)
    deck.card_Bonus_Penalty(player_hand)
    deck.score(player_hand)

    print(f"{player_name}'s hand after turn: {[card.name for card in player_hand]}")


# Main game setup
deck = Deck()
deck = initialize_deck(deck)
num_players = int(input("Enter the number of players: "))


# Get cards for each player from user input
players_hands, deck = get_player_hands(deck, num_players)


# Initialize the table with user input or empty
table_cards = initialize_table(deck)

# Game loop until table has 10 cards
while len(table_cards) < 10:
    for i in range(num_players):
        print(f"\n--- Table cards: {len(table_cards)}/10 ---")
        player_turn(f"Player {i + 1}", players_hands[i], deck, table_cards, players_hands)
        if len(table_cards) >= 10:
            break

# Display final hands and table
print("\nFinal hands:")
for i, hand in enumerate(players_hands):
    print(f"Player {i + 1}: {[card.name for card in hand]}")

print("Cards on table:", [card.name for card in table_cards])
print("Cards remaining in deck:", [card.name for card in get_available_cards(deck, table_cards, players_hands)])
