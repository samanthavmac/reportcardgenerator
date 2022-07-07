# Module Library
# Final GUI Report Card Generator
# Samantha Mac
# ICS2O1

import random

# Basic Info
def randomize_OEN():
    OEN_1 = random.randint(100, 999)
    OEN_2 = random.randint(100, 999)
    OEN_3 = random.randint(100, 999)
    # Concatenate
    return (str(OEN_1) + '-' + str(OEN_2) + '-' + str(OEN_3))

def select_possessive_pronoun(pronoun_get):
    # Use if statements to assign pronoun types
    if pronoun_get == 1:
        possessive_pronoun = 'her'
    elif pronoun_get == 2:
        possessive_pronoun = 'his'
    else:
        possessive_pronoun = 'their'
    return possessive_pronoun

def select_verb_pronoun(pronoun_get):
    if pronoun_get == 1:
        verb_pronoun = 'She is'
    elif pronoun_get == 2:
        verb_pronoun = 'He is'
    else:
        verb_pronoun = 'They are'
    return verb_pronoun

def select_grade(grade_get):
    if grade_get == 4:
        grade = '9'
    elif grade_get == 5:
        grade = '10'
    elif grade_get == 6:
        grade = '11'
    elif grade_get == 7:
        grade = '12'
    return grade

# Average
def calculate_average(course_1_average, course_2_average, course_3_average, course_4_average):
    return (course_1_average + course_2_average + \
            course_3_average + course_4_average) / 4

# Skills
def select_responsibility_rating(responsibility_get):
    if responsibility_get == 8:
        responsibility_rating = 'E'
    elif responsibility_get == 9:
        responsibility_rating = 'G'
    elif responsibility_get == 10:
        responsibility_rating = 'S'
    elif responsibility_get == 11:
        responsibility_rating = 'N'
    return responsibility_rating

def select_organization_rating(organization_get):
    if organization_get == 8:
        organization_rating = 'E'
    elif organization_get == 9:
        organization_rating = 'G'
    elif organization_get == 10:
        organization_rating = 'S'
    elif organization_get == 11:
        organization_rating = 'N'
    return organization_rating

def select_independent_work_rating(independent_work_get):
    if independent_work_get == 8:
        independent_work_rating = 'E'
    elif independent_work_get == 9:
        independent_work_rating = 'G'
    elif independent_work_get == 10:
        independent_work_rating = 'S'
    elif independent_work_get == 11:
        independent_work_rating = 'N'
    return independent_work_rating

def select_collaboration_rating(collaboration_get):
    if collaboration_get == 8:
        collaboration_rating = 'E'
    elif collaboration_get == 9:
        collaboration_rating = 'G'
    elif collaboration_get == 10:
        collaboration_rating = 'S'
    elif collaboration_get == 11:
        collaboration_rating = 'N'
    return collaboration_rating

def select_initiative_rating(initiative_get):
    if initiative_get == 8:
        initiative_rating = 'E'
    elif initiative_get == 9:
        initiative_rating = 'G'
    elif initiative_get == 10:
        initiative_rating = 'S'
    elif initiative_get == 11:
        initiative_rating = 'N'
    return initiative_rating

def select_self_regulation_rating(self_regulation_get):
    if self_regulation_get == 8:
        self_regulation_rating = 'E'
    elif self_regulation_get == 9:
        self_regulation_rating = 'G'
    elif self_regulation_get == 10:
        self_regulation_rating = 'S'
    elif self_regulation_get == 11:
        self_regulation_rating = 'N'
    return self_regulation_rating

# Generate comment
def select_average_statement(final_average, first_name):
    if final_average >= 75:
        # Concatenate name and statement
        average_statement = (first_name
                             + ' meets all academic requirements.')
    else:
        average_statement = (first_name
                             + ' doesn\'t meet academic requirements.')
    return average_statement

def select_responsibility_statement(responsibility_rating, possessive_pronoun, verb_pronoun):
    # Selecting randomized statement 
    # Assign statement to number using if statements
    rand_num = random.randint(0,1)
    # Assign based on randomized number and rating
    if (responsibility_rating == 'E' or responsibility_rating == 'G') and rand_num == 0:
        # Concatenate strings with pronouns
        responsibility_statement = (verb_pronoun + ' always finishing '
                           + possessive_pronoun + ' work on time.')
    elif (responsibility_rating == 'E' or responsibility_rating == 'G') and rand_num == 1:
        responsibility_statement = (verb_pronoun + ' committed to learning '
                           + 'as much as possible by completing '
                           + possessive_pronoun + ' given classwork.')
    elif (responsibility_rating == 'S' or responsibility_rating == 'N') and rand_num == 0:
        responsibility_statement = (verb_pronoun + ' irresponsible and '
                           + 'constantly claims that '
                           + possessive_pronoun + ' dog ate '
                           + possessive_pronoun + ' homework.')
    else:
        responsibility_statement = (verb_pronoun + ' not fulfilling '
                           + possessive_pronoun + ' classroom '
                           + 'commitments. ' + verb_pronoun +
                           ' usually falling asleep in class.')
    return responsibility_statement

def select_organization_statement(organization_rating, possessive_pronoun, verb_pronoun):
    rand_num = random.randint(0,1)
    if (organization_rating == 'E' or organization_rating == 'G') and rand_num == 0:
        organization_statement = (verb_pronoun + ' so organized (aka '
                           + 'the next Marie Kondo)!')
    elif (organization_rating == 'E' or organization_rating == 'G') and rand_num == 1:
        organization_statement = (verb_pronoun + ' more organized than I am! '
                           + verb_pronoun + ' keen on developing a '
                           + 'plan and priorities for large assignments.')
    elif (organization_rating == 'S' or organization_rating == 'N') and rand_num == 0:
        organization_statement = ('I would hire a professional cleaner '
                           + 'because ' + possessive_pronoun + ' desk '
                           + 'looks like a black hole.')
    else:
        organization_statement = (verb_pronoun + ' studying on a bird\'s '
                           + 'nest rather than a desk. It\'s too messy!')
    return organization_statement

def select_independent_work_statement(independent_work_rating, possessive_pronoun, verb_pronoun):
    rand_num = random.randint(0,1)
    if (independent_work_rating == 'E' or independent_work_rating == 'G') and rand_num == 0:
        independent_work_statement = (verb_pronoun + ' using class time '
                           + 'appropriately without direct supervision.')
    elif (independent_work_rating == 'E' or independent_work_rating == 'G') and rand_num == 1:
        independent_work_statement = (verb_pronoun + ' always focusing on the '
                           + 'task at hand.')
    elif (independent_work_rating == 'S' or independent_work_rating == 'N') and independent_work_rating == 0:
        independent_work_statement = (verb_pronoun + ' always off-task.')
    else:
        independent_work_statement = (verb_pronoun + ' constantly disrupting class '
                           + 'and it\'s distracting hardworking '
                           + 'students such as Samantha Mac.')
    return independent_work_statement

def select_collaboration_statement(collaboration_rating, possessive_pronoun, verb_pronoun):
    rand_num = random.randint(0,1)
    if (collaboration_rating == 'E' or collaboration_rating == 'G') and rand_num == 0:
        collaboration_statement = (verb_pronoun + ' able to work well in '
                           + 'a group and independent setting. '
                           + verb_pronoun + ' a certified '
                           + 'team leader!')
    elif (collaboration_rating == 'E' or collaboration_rating == 'G') and rand_num == 1:
        collaboration_statement = (verb_pronoun + ' excellent at resolving '
                           + 'conflict and thinking critically.')
    elif (collaboration_rating == 'S' or collaboration_rating == 'N') and rand_num == 0:
        collaboration_statement = (verb_pronoun + ' unable to build healthy '
                           + 'peer relationships.')
    else:
        collaboration_statement = (verb_pronoun + ' negatively expressing '
                           + possessive_pronoun + ' ideas and values.')
    return collaboration_statement

def select_initiative_statement(initiative_rating, possessive_pronoun, verb_pronoun):
    rand_num = random.randint(0,1)
    if (initiative_rating == 'E' or initiative_rating == 'G') and rand_num == 0:
        initiative_statement = (verb_pronoun + ' excited to find new '
                           + 'opportunities outside of the classroom.')
    elif (initiative_rating == 'E' or initiative_rating == 'G') and rand_num == 1:
        initiative_statement = (verb_pronoun + ' more curious than Curious George! '
                           + verb_pronoun + ' always eager to learn more!')
    elif (initiative_rating == 'S' or initiative_rating == 'N') and rand_num == 0:
        initiative_statement = (verb_pronoun + ' encouraged to take more risks.')
    else:
        initiative_statement = (verb_pronoun + ' demonstrating absolutely no '
                           + 'capacity for innovation...no offence.')
    return initiative_statement

def select_self_regulation_statement(self_regulation_rating, possessive_pronoun, verb_pronoun):
    rand_num = random.randint(0,1)
    if (self_regulation_rating == 'E' or self_regulation_rating == 'G') and rand_num == 0:
        self_regulation_statement = (verb_pronoun + ' consitent with monitoring '
                           + possessive_pronoun + ' own progress towards\n'
                           + 'achieving ' + possessive_pronoun
                           + ' goals (yahoo!).')
    elif (self_regulation_rating == 'E' or self_regulation_rating == 'G') and rand_num == 1:
        self_regulation_statement = (verb_pronoun + ' not afraid to ask for '
                           + 'assistance when needed.')
    elif (self_regulation_rating == 'S' or self_regulation_rating == 'N') and rand_num == 0:
        self_regulation_statement = (verb_pronoun + ' unable to critically '
                           + 'reflect on ' + possessive_pronoun + ' work '
                           + 'with an open mindset.')
    else:
        self_regulation_statement = (verb_pronoun + ' unmotivated when '
                           + 'it comes to overcoming challenges.')
    return self_regulation_statement

# Select 3 random statements for the final comment
def select_skill(responsibility_statement, organization_statement, \
                 independent_work_statement, collaboration_statement, \
                 initiative_statement, self_regulation_statement):
    # Select random int
    rand_num_1 = random.randint(0,5)

    # Assign each learning skill to an int
    # Statement will be selected accordingly
    # based on random int
    if rand_num_1 == 0:
        skill_statement_1 = responsibility_statement
    elif rand_num_1 == 1:
        skill_statement_1 = organization_statement
    elif rand_num_1 == 2:
        skill_statement_1 = independent_work_statement
    elif rand_num_1 == 3:
        skill_statement_1 = collaboration_statement
    elif rand_num_1 == 4:
        skill_statement_1 = initiative_statement
    elif rand_num_1 == 5:
        skill_statement_1 = self_regulation_statement

    rand_num_2 = random.randint(0,5)
    # Validation loop to ensure there are no duplicates
    while rand_num_2 == rand_num_1:
        # Select new number until all numbers are different
        rand_num_2 = random.randint(0,5)

    if rand_num_2 == 0:
        skill_statement_2 = responsibility_statement
    elif rand_num_2 == 1:
        skill_statement_2 = organization_statement
    elif rand_num_2 == 2:
        skill_statement_2 = independent_work_statement
    elif rand_num_2 == 3:
        skill_statement_2 = collaboration_statement
    elif rand_num_2 == 4:
        skill_statement_2 = initiative_statement
    elif rand_num_2 == 5:
        skill_statement_2 = self_regulation_statement       

    rand_num_3 = random.randint(0,5)
    while (rand_num_3 == rand_num_1) or (rand_num_3 == rand_num_2):
        rand_num_3 = random.randint(0,5)

    if rand_num_3 == 0:
        skill_statement_3 = responsibility_statement
    elif rand_num_3 == 1:
        skill_statement_3 = organization_statement
    elif rand_num_3 == 2:
        skill_statement_3 = independent_work_statement
    elif rand_num_3 == 3:
        skill_statement_3 = collaboration_statement
    elif rand_num_3 == 4:
        skill_statement_3 = initiative_statement
    elif rand_num_3 == 5:
        skill_statement_3 = self_regulation_statement

    return skill_statement_1, skill_statement_2, skill_statement_3



