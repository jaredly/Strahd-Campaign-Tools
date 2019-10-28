from specialRolls import iRoll, sRoll
import dice

def advRoll():
    return max(dice.roll('2d20'))

def disadvRoll():
    return min(dice.roll('2d20'))

perceptionDC = 0

playerPerceptionTrigger = 0

class character:
    def __init__(self, charName = "", initial = "", modifier = 0, adv = False, disadv = False):
        self.charName = charName # The character's full first name
        self.initial = initial # The Initial to signify the character, the first letter of the character's name
        self.modifier = modifier # The character's perception modifier (positive or negative)
        self.adv = adv # Whether or not the character has advantage
        self.disadv = disadv # Whether or not the character has disadvantage
    
        def characterPerceptionRoll(): 
            if self.adv == True and self.disadv == True: # Accidentally gave a character advantage AND disadvantage, so the two cancel out
                self.adv == False # Disadvantage cancels out advantage
                self.disadv == False # Advantage cancels out the disadvantage
            if self.adv == True: # Character has advantage
                self.percRoll = int(advRoll) +  self.modifier
            elif self.disadv == True: # Character has disadvantage
                self.percRoll = int(disadvRoll) + self.modifier
            else: # Just a straight-across perception roll 
                self.percRoll = iRoll('1d20') + self.modifier
            return self.percRoll # Returns the rolled perception to the rest of the program
        
        def perceptionDifficultyClassCheck():
            if self.percRoll >= perceptionDC:
                perceptionDC += 1
                print(charName + "perceived something!")

ashe = character("Ashe", "a", 0)
charles = character("Charles", "c", 3)
selamin = character("Selamin", "s", 3)
vye = character("Vye", "v", 2)

playerParty = [ashe, charles, selamin, vye]

def perceptionDCprompt():
    perceptionDc = int(input("The DC of the Perception Check: "))
    return perceptionDC

def advantagePrompt():
    charactersWithAdvantage = [input("Which characters (if any) have advantage: ")]
    if playerParty(character.initial) in charactersWithAdvantage:
        character.adv = True
    charactersWithDisadvantage = [input("Which characters (if any) have disadvantage: ")]
    if playerParty(character.initial) in charactersWithDisadvantage:
        character.disadv = True
    return charactersWithAdvantage
    return charactersWithDisadvantage

def partyPerceptionCheck():
    playerPerceptionTrigger = 0
    perceptionDCprompt()
    advantagePrompt()
    for characters in playerParty:
        character.characterPerceptionRoll()
        character.perceptionDifficultyClassCheck()
    if playerPerceptionTrigger == 0:
        print("No one perceived anything...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    partyPerceptionCheck()