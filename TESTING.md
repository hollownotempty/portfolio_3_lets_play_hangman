# Testing

## User Stories Tested

*numbers correspond to the relevant user story in [README.md](README.md)

1. Selection of an easy or hard word.

![1.1](assets/images/user_stories/user_story_1.1.png)
---
![1.2](assets/images/user_stories/user_story_1.2.png)

*Expected result: Player will press E or H and the corresponding difficulty will be used in game.*

2. Being able to see the played letters.

![2.1](assets/images/user_stories/user_story_2.1.png)

*After every guess, the list of letters is appended with the latest guess if it is new.*

3. Graphical hangman displayed 

![3.1](assets/images/user_stories/user_story_3.1.png)

*As displayed above, hangman states are updated with each wrong guess until the end of the game.*

4. Game restart capability.

![4.1](assets/images/user_stories/user_story_4.1.png)

*Expected result: player presses either Y or N and the game restarts if the input is Y.*

5. Random words are generated for the game by using the Random-Word package, using the CorpusCount parameter to decide if the word is common or uncommon (depending on the chosen difficulty).

## Bugs
<Details>
    <summary>View bugs here.</summary>
    
1. Bug: After deployment, the program would fail to run and would throw an error 
    ```
    ModuleNotFoundError: No module named 'yaml'
    ```

    ![name_error](assets/images/screenshots/yaml_module.png)

    Fix: This was fixed by doing some research and discovering that a module named [PyYAML](https://pypi.org/project/PyYAML/) was needed to run the app on Heroku.

2. Bug: After deployment, input requests would not appear in the mock terminal but input could still be given, only showing the request after input was given. 

    ![mock_terminal](assets/images/screenshots/mock_terminal.png)

    Fix: After consulting the Slack community i found this could be solved by adding a ``` \n ``` to the end of any input.

3. Bug: Debugger throwing ```EOFError``` on all inputs.

    Fix: Add a ```Try/Except``` statement on all the inputs, this prevents the error being thrown and doesn't change the output. 
</details>

