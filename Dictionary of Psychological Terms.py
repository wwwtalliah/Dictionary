# Psychology Dictionary Program in Python

# Initialize a dictionary with some psychology terms and definitions
psychology_dict = {
    'Altruism': 'Selfless concern for the well-being of others.',
    'Anxiety': 'A feeling of worry, nervousness, or unease, typically about an imminent event or something with an uncertain outcome.',
    'Attachment': 'A deep and enduring emotional bond that connects one person to another across time and space.',
    'Behaviorism': 'A theory of learning which states that all behaviors are acquired through conditioning, and that our responses to environmental stimuli shape our behavior.',
    'Classical Conditioning': 'A learning process that occurs when two stimuli are repeatedly paired; a neutral stimulus becomes associated with a response through conditioning.',
    'Cognitive Bias': 'A systematic pattern of deviation from norm or rationality in judgment.',
    'Cognitive Dissonance': 'The mental discomfort or tension that a person experiences when they hold two or more contradictory beliefs, values, or attitudes.',
    'Conformity': 'The act of matching attitudes, beliefs, and behaviors to group norms or societal expectations.',
    'Defense Mechanism': 'Psychological strategies used by individuals to cope with reality and maintain self-image.',
    'Depression': 'A mood disorder characterized by persistent feelings of sadness, hopelessness, and loss of interest in activities.',
    'Dopamine': 'A neurotransmitter associated with pleasure, reward, and motivation.',
    'Ego': 'The rational part of the mind that mediates between the desires of the id and the moral constraints of the superego.',
    'Empathy' : 'The ability to understand and share the feelings of another.',
    'Id': 'In Freudian theory, the part of the mind that contains our basic instinctual drives and desires, seeking immediate gratification.',
    'Locus of Control': 'The degree to which individuals believe they have control over the outcome of events in their lives.',
    'Mindfulness': 'The practice of being fully present and engaged in the moment, without judgment.',
    'Motivation': 'The process that initiates, guides, and sustains goal-oriented behavior.',
    'Neuroplasticity': 'The ability of the brain to change and adapt as a result of experience.',
    'Neurotransmitter': 'Chemicals that transmit signals across synapses from one neuron to another, influencing mood, thoughts, and behaviors.',
    'Operant Conditioning': 'A method of learning that occurs through rewards and punishments for behavior, which influences the likelihood of that behavior being repeated.',
    'Operant Extinction': 'The gradual weakening and disappearance of a behavior when it is no longer reinforced.',
    'Perception': 'The process of organizing, identifying, and interpreting sensory information to understand the environment.',
    'Personality': 'The combination of characteristics or qualities that form an individual’s distinctive character.',
    'Psychopathy': 'A personality disorder characterized by persistent antisocial behavior, impaired empathy, and bold, disinhibited, and egotistical traits.',
    'Reciprocity': 'The practice of exchanging things with others for mutual benefit.',
    'Schemas': 'Mental structures or frameworks that organize and interpret information.',
    'Self-esteem': 'One’s sense of self-worth or personal value.',
    'Social Influence': 'The way people are affected by others’ opinions and behaviors.',
    'Stereotype': 'A widely held but oversimplified and generalized belief about a particular group of people.',
    'Superego': 'The part of the mind that represents internalized moral standards and ideals that we acquire from society and our parents.',
}

# Function to search for a psychological term
def search_term(term):
    if term in psychology_dict:
        print(f"{term}: {psychology_dict[term]}")
    else:
        print(f"Sorry, '{term}' is not in the psychology dictionary.")

# Function to add a new term to the dictionary
def add_term(term, definition):
    psychology_dict[term] = definition
    print(f"'{term}' has been added to the psychology dictionary.")

# Function to display the entire psychology dictionary
def display_dictionary():
    if psychology_dict:
        print("\nPsychology Dictionary:")
        for term, definition in psychology_dict.items():
            print(f"{term}: {definition}")
    else:
        print("The dictionary is empty.")
# Main program loop
def main():
    while True:
        print("\n--- PSYCHOLOGY DICTIONARY MENU ---")
        print("1. Search Term")
        print("2. Add Term")
        print("3. Display Dictionary")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            term = input("Enter the psychology term: ")
            search_term(term)
        elif choice == '2':
            term = input("Enter the psychology term: ")
            definition = input("Enter the definition: ")
            add_term(term, definition)
        elif choice == '3':
            display_dictionary()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
